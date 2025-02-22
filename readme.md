Repository voor Webots projecten bij OLOD Robot Design

2024 - 2025 Electronica-ICT, Cybersecurity & Cloud

<style>
    blib {
        color: pink;
    }
</style>

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

## Tutorial 7
### 1. Doelstelling
Doelstelling is om een PROTO bestand te ontwerpen voor de 4 wielen van de vorige tutorial.

### 2. Kopieer de robot definitie
De robot uit de vorige tutorial is volledig gedefinieerd in het world bestand. Door dit te verplaatsen naar een PROTO bestand kan je een robot importeren in andere wereld.

#### Hands-on #1:
Open het world bestand van vorige tutorial in een teksteditor (bijv. kladblok) . Maak een nieuw leeg tekstbestand (.txt) aan in de <blib>protos</blib> map van je project en noem deze <blib>FourWheelsRobot.proto.</blib> Open dit bestand in de teksteditor.

De structuur van een PROTO bestand ziet eruit als volgt

    #VRML_SIM R2023b utf8
    PROTO protoName [
        protoFields
    ]
    {
        protoBody
    }

De <blib>protoName</blib> moet de naam zijn van jouw PROTO bestand (<blib>FourWheelsRobot</blib> in dit geval), in <blib>protoFields</blib> defineer je de aanpasbare velden van de PROTO node (laten we nog even leeg) en de protoBody is de definitie van de root node (i.e. the Robot node in this case).

#### Hands-on #2:
Schrijf de standaard structuur in het PROTO bestand met de correcte <blib>protoName</blib>. Van het <blib>4_wheels_robot.wbt</blib> wereld bestand kopieer je de robot node (start met <blib>Robot {</blib> en eindigt met het laatste <blib>}</blib>) en plak je het in jouw PROTO bestand in plaats van het <blib>protoBody</blib>. Bewaar tot slot het PROTO bestand.

Oplossing: Deze zou er zo moeten uitzien:

    #VRML_SIM R2023b utf8
    PROTO FourWheelsRobot [

    ]
    {
        Robot {
            # list of fields
    }
    }

### 3. PROTO gebruiken
De nieuwe PROTO node is nu beschikbaar voor elke wereld in je huidig project.
![thumbnail](info/tutorial7_proto.thumbnail.jpg)</br>
De PROTO is nu zichtbaar in het "Add a node" venster.

#### Hands-on #3:
Open de <blib>4_wheels_robot.wbt</blib> wereld in Webots en voeg de <blib>FourWheelsRobot</blib> node toe (welke je net hebt aangemaakt). Je vindt het bestand in <blib>PROTO nodes (Current Project) / FourWheelsRobot (Robot)</blib>.

### 4. Velden toevoegen
Je zal al gemerkt hebben dat deze nieuwe PROTO node geen enkel veld heeft waardoor het niet mogelijk is om translate, rotate of controller wijzigingen uit te voeren. It is very easy to add new fields to a PROTO node and to link them with internal fields. This should be done in the PROTO interface part (part between the <blib>[</blib> and the <blib>]</blib>).

#### Hands-on #4:
Bewerk je PROTO bestand in een teksteditor en voeg de definities toe van de translation, rotation en <blib>bodyMass</blib> velden in hte PROTO interface gedeelte:

    field SFVec3f    translation  0 0 0
    field SFRotation rotation     0 0 1 0
    field SFFloat    bodyMass     1

Je PROTO node heeft nu twee open velden maar deze zijn niet gelinkt naar enig intern veld. Om deze link te maken gebruik he het IS keyword. Vervang het <blib>translation x y z</blib> en <blib>rotation x y z</blib> angle velden van de Robot node:

    translation IS translation
    rotation IS rotation

Voeg het <blib>mass</blib> veld aan de Physics node van de Robot node toe:

    mass IS bodyMass   

Bewaar je PROTO bestand, welke er ongeveer uitziet als volgt:

    #VRML_SIM R2023b utf8
    PROTO FourWheelsRobot [
        field SFVec3f    translation  0 0 0
        field SFRotation rotation     0 0 1 0
        field SFFloat    bodyMass     1
    ]
    {
        Robot {
            translation IS translation
            rotation IS rotation
            children [
            # list of children nodes
            ]
            boundingObject USE BODY
            physics Physics {
            density -1
            mass IS bodyMass
            }
            controller "four_wheels_collision_avoidance"
        }
    }

Je kan nu je simulatie bewaren. De <blib>translation</blib>, <blib>rotation</blib> en <blib>bodyMass</blib> van de <blib>FourWheelsRobot</blib> node kan je nu aanpassen (in de scene tree of via het 3D venster).

Hetzelfde mechanisme kan je gebruiken voor het <blib>controller</blib> veld van de Robot node.</br>
De oplossing kan je [hier](info/tutorial7-oplossing-FourWheelsRobot.proto.txt) terugvinden.

### 5. Project bewaren
Bewaar je project, back-up je volledige projectstructuur in één zip bestand en laad dit op in de Uploadzone.
