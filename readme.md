Repository voor Webots projecten bij OLOD Robot Design

2024 - 2025 Electronica-ICT, Cybersecurity & Cloud

# Projecten
## Project playfield
Jouw taak bestaat er in om een playfield te ontwerpen, in Webots, voor een e-puck wedstrijd.

### Doel
Het doel is om deze robot van een startlocatie autonoom te laten verplaatsen naar een andere locatie.

### Vereisten
Wat moet je realiseren?
* Een wedstrijdveld omringd door muren
* Het wedstrijdveld is 2 x 4 m groot
* Het bevat één startlocatie weergegeven met een rechthoek
* Bevat één eindlocatie weergegeven met een cirkel
* Moet bestaan uit verschillende lijntracks bevatten tussen de locaties
    - Er onderweg gekozen kan worden tussen verschillende alternatieven wegen die terug samenkomen op één punt
    - De tracklijn op één punt volledig onderbroken is gedurende een "grote" afstand. De robot dient hier muren te volgen.
    - De tracklijn op een bepaald gedeelte een stippellijn zijn
    - Op één punt moet de de lijn zichzelf haaks kruisen
    - Er minstens 1 bal en 2 dozen aanwezig zijn die verplaats kunnen worden. Je moet tijdens de simulatie de weg kunnen blokkeren.

# Webots tutorials
## Tutorial 6
In deze tutorial ga jij je eerste robot bouwen vanaf nul. De robot zal bestaand uit een robotframe, 4 wielen en 2 afstandssensoren. Het resultaat zie je hieronder.
![tutorial 6 robot](info/webots06_tutorial_4_wheels_robot.thumbnail.jpg)

### Stap 2
Voeg een robot node toe op het einde van de scene tree, welke vier **HingeJoint nodes** welke elk een **Solid node** hebben als **endPoint** (zie figuur hieronder). Voeg een **Shape node toe**, aan de Robot node, welke een **Box geometrie** bevat. Stel de kleur van de Shape in op **rood**. Gebruik deze Shape om het **boundingObject** veld te bepalen van de Robot node. Box afmetingen zijn `(0.2, 0.1, 0.05)`. Voeg een **Physics node** toe aan de Robot. De figuur toont alle nodes die samen de robot definiëren.  Enkel de directe children nodes van de root Robot node ontbreken nog.

### Stap 3
Voeg een **HingeJointParameters node** toe, en voeg de de waarden die hierboven omschreven zijn toe. Voer de andere wielen moet je uiteraard aangepaste waarden invoeren. Some signs obviously have to be updated for other wheels.

### Stap 4
Vervolledig door de ontbrekende nodes toe te voegen zodat je onderstaand geheel bekomt. Vergeet niet om de Physics nodes te bepalen.
![volledige nodetree](info/webots06_nodetree-volledig.png)

### Stap 5
Voeg  de twee afstandssensoren toe. Deze staan onder een hoek van 0.3 [rad] t.o.v. de Z-as van het robotlichaam. Stel de grafische en physical shape in op een kubus (Cube) waarbij elke zijde 0.01 [m] bedraagt. Stel de kleur in op blauw. Stel het name veld in op de tagnamen van de figuur in hoofdstuk doelstelling.

### Stap 6
Voeg een controller toe en noem deze `four_wheeled_collision_avoidance` welke de robot zal laten bewegen en botsingen zal vermijden m.b.v. de afstandssensoren.
