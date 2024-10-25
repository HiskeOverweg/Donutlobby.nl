Title: Klimaatdoel 2030 in Nederland
slug: klimaatdoel-2030-in-Nederland
lang: nl
Date: 2024-10-25 10:00

# Doelen ver weg

<side-block>
  <side-content>
![Alt Text]({static}/images/ci.png)
De En-ROADS simulator is ontwikkeld door de denktank [Climate Interactive](https://climateinteractive.org) en [MIT Sloan Sustainability initiative](https://mitsloan.mit.edu/sustainability-initiative/welcome).
![Alt Text]({static}/images/mit.png)
  </side-content>
</side-block>

Het PBL waarschuwde gisteren in [een persbericht](https://www.pbl.nl/actueel/nieuws/klimaatdoel-2030-raakt-uit-zicht-extra-beleid-met-snel-effect-nodig) dat het erg onwaarschijnlijk is dat Nederland het emissiereductiedoel, 55% minder uitstoot in 2030 ten opzichte van 1990, gaat halen. Als we doorgaan zonder verdere beleidswijzigingen, is de uitstoot in 2030 nog ongeveer 16 - 24 megaton te hoog. De NOS [stelde een aantal maatregelen voor](https://specials.app.nos.nl/tool-maatregelen-klimaatdoelen/) om te kijken in hoeverre die zouden kunnen bijdragen om dit gat op te vullen. Laten we eens kijken of we de impact van een aantal van de voorgestelde maatregelen ook met de En-ROADS klimaatsimulator kunnen herproduceren.

## Extra bomen planten

<side-block>
    <side-content>
      ![]({static}/images/nos/bosoppervlak.png)
      Wereldwijd bosoppervlak gedurende deze eeuw in verschillende scenario's.
    </side-content>
</side-block>

Wat als we 19,000 hectare aan bomen planten? vraagt de NOS. In de En-ROADS simulator kunnen we dat op iets grotere schaal uittesten. Het maximale oppervlak wat je in deze simulator wereldwijd kunt beplanten is 550 megahectare , oftewel ongeveer 2 keer de oppervlakte van India. Hiernaast zie je een grafiekje van het wereldwijde bosoppervlak gedurende deze eeuw. Als we zo doorgaan als vandaag de dag, neemt dat oppervlak gestaag af, dat is het zwarte lijntje. Als we 550 Mha bijplanten, zien we in plaats daarvan een toename van het bosoppervlak (het blauwe lijntje).

<side-block>
    <side-content>
      ![]({static}/images/nos/co2_bos.png)
      Extra CO<sub>2</sub> die wordt opgenomen bij het planten van 550 megahectare aan bomen.
    </side-content>
</side-block>

Hiernaast staat een grafiekje van de extra CO<sub>2</sub> die dan door het bos wordt opgenomen. De aannames die hier gedaan zijn, is dat het ongeveer 10 jaar kost om alle benodigde grond aan te kopen, en vervolgens ongeveer 10 jaar om alle bomen te planten. Op lange termijn, zo rond 2090 is het bos dan flink gegroeid en wordt er ongeveer 5 Gton aan CO<sub>2</sub> per jaar opgenomen door de bomen. De oppervlakte voor beplanting die de NOS voorstelt, is ongeveer 0,003% daarvan, dus dat zou leiden tot een koolstofopslag van 0,17 megaton. Die schatting komt aardig in de buurt van de schatting van de NOS van 0,1 megaton. Wellicht kan het verschil verklaard worden door het feit dat bomen in sommige regio's van de wereld sneller groeien dan in Nederland en daarme wat sneller CO<sub>2</sub> opnemen.

De tijdschaal is hier wel belangrijk: het kost zo'n 65 jaar voordat de bomen bovenstaande opslagcapaciteit bereiken. Voor het halen van klimaatdoelen in Nederland in 2030, kunnen we dus concluderen dat als we in 1965 hadden bedacht om extra bos te gaan planten, we in 2030 deze opslagcapaciteit gehaald zouden hebben. Tja. Een beetje laat om die conclusie nu te trekken...

## De veestapel halveren
Volgens een [lijst](https://en.wikipedia.org/wiki/List_of_countries_by_meat_production) gemaakt door Our World in Data, produceerde Nederland in 2022 ongeveer 0,8% van het vlees wereldwijd. Laten we er voor het gemak vanuit gaan dat we ongeveer eenzelfde fractie van de wereldwijde zuivel produceren. Een halvering van de veestapel zou dus neerkomen op een afname van de consumptie van dierlijk eiwit met 0,4%. Als we dat in En-ROADS invoeren, vinden we dat de uitstoot in 2030 met 20 megaton afneemt. Dat is fors hoger dan de 4,9 megaton die de NOS noemt.

![]({static}/images/nos/vlees.png)


Waarom dit verschil? Er is een groot verschil in uitstoot per kg product (vlees en zuivel) tussen verschillende landen. Een [paper](https://link.springer.com/article/10.1007/s10584-014-1197-x) uit 2014 laat zien dat dit verschil  tussen het mondiale Noorden en het mondiale Zuiden grofweg een factor twee is. Als je kijkt naar 1% van de wereldwijde producten en je neemt alleen producten uit het mondiale Zuiden mee, dan is de uitstoot daarvan 38 megaton (cijfers uit 2010). Als je alleen naar producten uit het mondiale Noorden kijkt, dan is de uitstoot van 1% van de wereldwijde producten 19 megaton. De schatting van het En-ROADS model komt dus te hoog uit, omdat het model ervan uit gaat dat de 0,4% afname deels in het mondiale Zuiden plaatsvindt, terwijl wij geïnteresseerd zijn in het halveren van de veestapel in Nederland. Met de gegevens uit het paper komen we voor Nederland op een reductie van 7,6 megaton. Dat is nog steeds iets hoger dan de schatting van de NOS, maar het komt al meer in de buurt. Ik zou me kunnen voorstellen dat het resterende verschil verklaard wordt door het feit dat de uitstoot per kg product in Nederland zelfs ten opzichte van het gemiddelde van het mondiale Noorden nog wel wat lager ligt.

## Alle bestelauto's elektrisch
<side-block>
    <side-content>
      ![]({static}/images/nos/aantal_autos.png)
      De hoeveelheid elektrische auto's in twee verschillende scenario's.
    </side-content>
</side-block>

Wereldwijd zijn er zo'n 1,4 miljard auto's en andere voertuigen [(bron)](https://hedgescompany.com/blog/2021/06/how-many-cars-are-there-in-the-world/). Het aantal busjes in Nederland is ongeveer één miljoen volgens het [CBS](https://www.cbs.nl/nl-nl/visualisaties/verkeer-en-vervoer/vervoermiddelen-en-infrastructuur/bestelautos), dus 0,06% van het totaal. Zulke kleine getallen zijn een beetje lastig te bekijken met een wereldwijde simulator, dus laten we eens kijken wat er gebeurt als we het aantal elektrische auto's met 6% vergroten in 2040. De bijbehorende vermindering van de uitstoot in dat jaar is dan 210 megaton, zoals in de onderstaande grafiek is te zien.

![]({static}/images/nos/uitstoot_autos.png)

 Dat zou voor de Nederlandse bestelbusjes (een groep die 100x zo klein is) dus resulteren in een uitstootreductie van 2,1 megaton. Dat komt aardig in de buurt van het getal wat de NOS vindt: 3,6 megaton. De NOS merkt op dat zij er bij de berekening van uit zijn gegaan dat alle elektrische busjes op groene energie rijden, en dus effectief niets uitstoten bij het rijden. De En-ROADS simulator gaat uit van de wereldwijde energiemix, die ook in 2040 nog voor een groot deel fossiele brandstoffen bevat. Het is dus logisch dat we met de berekening met de En-ROADS simulator op een kleinere besparing uitkomen.

## Conclusie

De schattingen van de NOS komen redelijk goed overeen met de schattingen uit de En-ROADS klimaatsimulator. De afwijkingen kunnen grotendeels worden verklaard door verschillen tussen de uitvoering op nationale of wereldwijde schaal.

De besparing van 16-24 megaton in Nederland voor 2030 gaat nog een flinke kluif worden. Ben je benieuwd welke maatregelen op wereldwijde schaal de grootste impact zouden kunnenen hebben? Kijk op mijn [agenda]({filename}../pages/agenda.md) voor workshops met de En-ROADS simulator of mail naar [info@donutlobby.nl](mailto:info@donutlobby.nl) op om een workshop te plannen.
