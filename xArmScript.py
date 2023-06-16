import sys
import math
import time
import datetime
import random
import traceback
import threading

try:
    from xarm.tools import utils
except:
    pass
from xarm import version
from xarm.wrapper import XArmAPI

def pprint(*args, **kwargs):
    try:
        stack_tuple = traceback.extract_stack(limit=2)[0]
        print('[{}][{}] {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1], ' '.join(map(str, args))))
    except:
        print(*args, **kwargs)

pprint('xArm-Python-SDK Version:{}'.format(version.__version__))

arm = XArmAPI('10.2.172.20')
arm.clean_warn()
arm.clean_error()
arm.motion_enable(True)
arm.set_mode(0)
arm.set_state(0)
time.sleep(1)

variables = {}
params = {'speed': 100, 'acc': 2000, 'angle_speed': 20, 'angle_acc': 500, 'events': {}, 'variables': variables, 'callback_in_thread': True, 'quit': False}

#errors handelen
def error_warn_change_callback(data):
    if data and data['error_code'] != 0:
        params['quit'] = True
        pprint('err={}, quit'.format(data['error_code']))
        arm.release_error_warn_changed_callback(error_warn_change_callback)
arm.register_error_warn_changed_callback(error_warn_change_callback)

#status van de robot tracken idle, running, paused en error
def state_changed_callback(data):
    if data and data['state'] == 4:
        if arm.version_number[0] > 1 or (arm.version_number[0] == 1 and arm.version_number[1] > 1):
            params['quit'] = True
            pprint('state=4, quit')
            arm.release_state_changed_callback(state_changed_callback)
arm.register_state_changed_callback(state_changed_callback)


# hoeveelheid bewegingen van elke aparte motor van de robot bijhouden
if hasattr(arm, 'register_count_changed_callback'):
    def count_changed_callback(data):
        if not params['quit']:
            pprint('counter val: {}'.format(data['count']))
    arm.register_count_changed_callback(count_changed_callback)


# stuurt een bericht wanneer de connection status veranderd naar disconnected bv. en gaat het programma dan quitten.
def connect_changed_callback(data):
    if data and not data['connected']:
        params['quit'] = True
        pprint('disconnect, connected={}, reported={}, quit'.format(data['connected'], data['reported']))
        arm.release_connect_changed_callback(error_warn_change_callback)
arm.register_connect_changed_callback(connect_changed_callback)
    
#Methode gemaakt om de robot te laten bewegen, met als parameter de X, Y en Z waarden.    
#Met Wait
def move_to_position(position):
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*position, speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=True)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
def move_to_position_zonder_wait(position):
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*position, speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
#Dictionary met coordinaten 
positions = {
    'bovenBordPositie': [256.0, -13.0, 120.0, 180.0, 0.0, 0.0],
    'opBordPositie': [256.0, -13.0, 10.8, 180.0, 0.0, 0.0],
    'tussenPositie': [256.0, -344.0,  60.0, 180.0, 0.0, 0.0],
    'neerleggenPositie': [260.0, -375.0,  -92.0, 180.0, 0.0, 0.0],
    'schuiven':[260.0, -424.0,  -92.0, 180.0, 0.0, 0.0],
    'trekken': [260.0, -424.0,  -25.0, 180.0, 0.0, 0.0],
}
    #Elke beweging van de robot
if not params['quit']:
    params['speed'] = 150
if not params['quit']:
    params['acc'] = 10000
    #Begin positie
if arm.error_code == 0 and not params['quit']:
    arm.reset()
#    Bord Oppakken
move_to_position(positions['bovenBordPositie']) 
move_to_position_zonder_wait(positions['opBordPositie']) 
move_to_position(positions['bovenBordPositie']) 
#    Bord Neerleggen
move_to_position_zonder_wait(positions['tussenPositie']) 
move_to_position_zonder_wait(positions['neerleggenPositie']) 
move_to_position_zonder_wait(positions['schuiven']) 
move_to_position_zonder_wait(positions['trekken']) 
move_to_position_zonder_wait(positions['tussenPositie']) 
if arm.error_code == 0 and not params['quit']:
    arm.reset()


#if arm.error_code == 0 and not params['quit']:
#    arm.reset()

# zet alle geregistreerde callback functies op stop zodat de robot niet meer beweegt
if hasattr(arm, 'release_count_changed_callback'):
    arm.release_count_changed_callback(count_changed_callback)
arm.release_error_warn_changed_callback(state_changed_callback)
arm.release_state_changed_callback(state_changed_callback)
arm.release_connect_changed_callback(error_warn_change_callback)
