Nour Boulif en Quentin Testaferrata zijn studenten aan de EhB in Toegepaste Informatica.   
We hebben dit project gemaakt in opdracht van Mr. Quanter voor de cursus robotica. We hebben voor 
de xArm gekozen omdat het een leuke uitdaging bleek te zijn.

Verloop van het project: 
Ons oorspronkelijke doel was om de robotarm te programmeren zodat deze een tafel kon dekken. 
Hiervoor moesten we eerst leren omgaan met de robot, hoe deze aan te zetten en verbinding te maken 
met onze computers, en vervolgens de arm te laten bewegen. Daarna wilden we een grijper 3D-printen, 
omdat deze helaas niet bij de robot werd geleverd. Bij het printen van de grijper hebben we echter 
problemen ondervonden. Ten eerste werden de 30 onderdelen per ongeluk weggegooid na het printen. 
Het tweede probleem was dat nadat we het opnieuw hadden geprint, we de grijper niet aan de robot konden 
bevestigen. Uiteindelijk hebben we ervoor gekozen om met hulp van onze docent een alternatieve grijper 
te maken met de lasercutter en een zuignap. Om de robot te laten bewegen, moesten we eerst Python leren 
en vervolgens de Python xArm-bibliotheek gebruiken. Om de robot te laten bewegen, moesten we gebruikmaken 
van meerdere callback-functies, wat het ingewikkeld maakte om te gebruiken. We zaten meerdere keren vast met 
coderen en moesten op internet zoeken hoe we verder moesten. Uiteindelijk is het ons gelukt om werkende code 
te schrijven. Een van de grootste obstakels was dat de robot op school moest blijven, 
waardoor we er niet altijd toegang toe hadden, zoals tijdens de twee weken vakantie. 
Vooral wanneer we ter plaatse coördinaten moesten instellen, was dit een uitdaging.

Hoe de robot te gebruiken: 
1) Download uFactory Studio
1) Zet de xArm aan met de rode knop en sluit een Ethernet-kabel aan. 
2) Sluit vervolgens ook de computer aan op een Ethernet-kabel en zorg ervoor dat beide apparaten 
   zich in hetzelfde netwerk bevinden. Open de xArm Studio en voer het IP-adres van de robot in. 
3) Als het het juiste IP-adres is, kan je op 'connect' drukken op uFactory Studio en word je doorgestuurd 
   naar de hoofdpagina waar je de robot eenvoudig kunt besturen met X, Y en Z coördinaten en knopjes. 
   In deze app is er ook een codeeromgeving waarin je Python-scripts kunt schrijven en uitvoeren.

Manipulatie van de robot & code:
We hebben een functie gemaakt om de arm te bewegen, die een parameter accepteert waarbij je de coördinaten meegeeft. 
Daarna hebben we een dictionary gemaakt met namen en bijbehorende coördinaten, zoals "beginPositie", waardoor we
met onze methode om de arm te bewegen, "beginPositie" kunnen meegeven, om de arm naar deze positie te laten gaan.
Dit is het belangrijkste deel van onze code. Voor de rest staat er in de code zelf commentaar voor elke
methode met daarin de uitleg van de werking van de functie.

Conclusie:
Dit was een enorm leerrijke experience, we hebben veel bijgeleerd. Vooral met een robot van deze kwaliteit
werken was uitdagend maar ook leuk. Als we meer tijd hadden zouden we een home-made grijper hebben gemaakt
met een servo, om de robot nog meer functionaliteiten te geven.

