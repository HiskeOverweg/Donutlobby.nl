Title: Halen we het Parijsakkoord met het VVD programma?
lang: nl
Date: 2021-01-24 10:00


 Het experiment

Deze blogpost is een gedachte-experiment. Stel dat de hele wereld het beleid uit [het concept-verkiezingsprogramma](https://www.vvd.nl/content/uploads/2020/11/Verkiezingsprogramma-concept-VVD-2021-2025.pdf) van de VVD van 2021 zou uitvoeren. Wat zouden dan de gevolgen zijn voor het klimaat? Zijn de ambities van de VVD voldoende om onze beloftes uit het Parijsakkoord waar te maken?

Deze vraag probeer ik te beantwoorden met behulp van [de En-ROADS climate simulator](https://en-roads.climateinteractive.org/scenario.html?v=2.7.35), gemaakt door MIT Sloan School of Management en de denktank Climate Interactive. De simulator is gecalibreerd aan de hand van 6 "integrated assessment models", dit zijn de beste klimaatmodellen die er in de wetenschap ontwikkeld zijn.

### Disclaimer - my best guesstimate

Om het VVD beleid te vertalen naar maatregelen die in de simulator worden ingevoerd, heb ik aannames moeten maken. Die zijn **dikgedrukt**. Ik ben ook maar een mens, dus deze aannames zijn per definitie niet objectief. Gelukkig is de En-ROADS climate simulator gratis beschikbaar, ik nodig je uit om de scenario's die ik hieronder deel naar eigen inzicht aan te passen.

### De status quo

![]({static}/images/parijs/1.png)

In deze figuur zien we de huidige stand van zaken in de wereld ([scenario link](https://en-roads.climateinteractive.org/scenario.html?g0=2&g1=62&v=2.7.35)). Links het verwachte energieverbruik van de hele wereld in de komende 80 jaar. Rechts zien we de bijbehorende (equivalente) CO<sub>2</sub>-uitstoot. Als we niets doen, leidt dit tot een temperatuurstijging ten opzichte van de 19e eeuw van 3.6°C. [Het Parijsakkoord](https://unfccc.int/process-and-meetings/the-paris-agreement/the-paris-agreement) stelt dat een temperatuurstijging van ruim onder de 2°C en liefst onder de 1.5°C wenselijk is. Tijd voor actie dus!
<side-ref><side-content>Gelukkig is Mark Rutte het hier [mee eens](https://www.cas2021.com/documents/videos/2021/01/11/mp-video-message).</side-content></side-ref>
Laten we het VVD programma eens onder de loep nemen.

### Het verkiezingsprogramma van de VVD

#### Kolen

De VVD schrijft: _In 2030 is het verboden om kolen te gebruiken om elektriciteit op te wekken. Oude, vervuilendere kolencentrales sluiten we eerder. Carbon Capture and Storage (CCS), (...) \[komt\] in aanmerking voor de stimuleringsregeling voor duurzame energietransitie._

In En-ROADS heb ik dit als volgt ingevoerd: 100% reductie in kolengebruik in 2030, **2%** versnelling van het sluiten van kolencentrales en een kostenvermindering voor CCS onderzoek van **5%**. Het effect op kolengebruik en de globale CO<sub>2</sub>-uitstoot zie je hier. We voorkomen zo 0.4°C temperatuurstijging - geen slechte start!
<side-ref><side-content>Op de En-ROADS website kun je meer lezen over [de andere positieve effecten](https://docs.climateinteractive.org/projects/en-roads/en/latest/guide/coal.html#potential-co-benefits-of-discouraging-coal) die de reductie van kolengebruik meebrengt.</side-content></side-ref>
[Scenario link](https://en-roads.climateinteractive.org/scenario.html?p196=100&p202=2030&p4=2&p6=5&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/2.png)

#### Gas

_Afbouwen van gaswinning in Groningen en doorgaan met het importeren van buitenlands gas._

Goed nieuws voor de inwoners van Groningen! - maar voor de rest van ons
betekent dit behoud van de status quo.

#### Kernenergie

_Nieuwe kerncentrales in Nederland om op de lange termijn een betrouwbare en CO<sub>2</sub>-neutrale energievoorziening te garanderen. Kernenergie kan op overheidssteun rekenen, waaronder financiering uit het Groeifonds_. (...) _Kernenergie of de ontwikkeling van een Thoriumreactor komen daarom in aanmerking voor de stimuleringsregeling voor duurzame energietransitie (SDE++)._

Het [Groeifonds](https://www.rijksoverheid.nl/actueel/nieuws/2021/01/14/eerste-kamer-stemt-in-met-nationaal-groeifonds) bevat 20 miljard euro voor de komende vijf jaar. Op dit moment genereert [de kerncentrale in Borssele](https://www.rijksoverheid.nl/onderwerpen/duurzame-energie/opwekking-kernenergie) (de enige in Nederland) jaarlijks 3.3 miljoen MWh. Met een deel van het budget van het groeifonds zouden we dus een flinke subsidie op nucleaire energie van **0.07 $/kWh** kunnen instellen. Laten we bovendien aannemen dat het in 2040 lukt om een Thoriumreactor te ontwikkelen. Het effect op de temperatuur is slechts 0.1°C. Hier zijn twee verklaringen voor. Ten eerste duurt het ongeveer 10 jaar om nieuwe infrastructuur voor kerncentrales op te zetten. Ten tweede concurreert goedkope nucleaire energie op de markt met hernieuwbare energiebronnen. In ons huidige scenario leidt meer gebruik van kernenergie tot minder gebruik van hernieuwbare energiebronnen, terwijl ons doel juist was om fossiel brandstofgebruik te verminderen.
<side-ref><side-content>Meer informatie over de mogelijkheden en gevaren van nucleaire energie kun je [hier](https://docs.climateinteractive.org/projects/en-roads/en/latest/guide/nuclear.html) vinden.</side-content></side-ref>

![]({static}/images/parijs/3.png)

#### Waterstof

_Grootschalige productie, gebruik en export van (groene) waterstof. Hiervoor kan energie uit kerncentrales en hernieuwbare energiebronnen worden ingezet._

Waterstof kan worden gebruikt voor energieopslag. Het kan als brandstof voor vervoersmiddelen dienen en [het kan kolen vervangen in grootschalige industriële processen](https://www.rechargenews.com/transition/-world-first-as-hydrogen-used-to-power-commercial-steel-production/2-1-799308), zoals staalproductie. In En-ROADS zijn er diverse mogelijkheden om dit
te simuleren:

- Elektrificering van voertuigen, (door gebruik te maken van een waterstofbatterij) laten we zeggen **1%** van de voertuigen per jaar. Dat betekent dat we jaarlijks 1% van alle auto's vervangen door auto's op waterstof. Dit is vrij ambitieus aangezien normaal gesproken jaarlijks ongeveer 3% van de auto's wordt vervangen.
- Electrificering van de industrie, laten we zeggen met **1%** per jaar.
- Onderzoek naar waterstofopslag zou kunnen leiden tot een doorbraak die een sterke kostenverlaging met zich mee brengt. Laten we aannemen dat waterstofopslag **10%** goedkoper wordt.

Hiermee komen we weer 0.1°C dichter bij ons doel. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p210=1&p196=100&p202=2030&p4=2&p6=5&p21=10&p30=-0.07&p36=2040&p53=1&p55=1&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/4.png)

#### Hernieuwbare energie

_Substantiële uitbreiding van het aandeel duurzame energie._

Dit is lastig te kwantificeren zonder verdere uitleg van de strategie. Wat mij betreft kan het verkiezingsprogramma op dit punt dus wel wat verduidelijking gebruiken. Laten we aannemen dat het gaat om een subsidie op duurzame energie van **0.02 $/kWh** (een dergelijk effect bereik je natuurlijk ook indirect door infrastructuur voor energieopwekking te financieren). **0.02 $/kWh** is iets meer dan 10% van [de prijs die de consument voor een kWh betaalt](https://www.consumentenbond.nl/energie-vergelijken/kwh-prijs). De opwarming van de aarde neemt met 0.1°C af. We zien een toename in het totale energieverbruik, omdat energie op deze manier goedkoper wordt.<side-ref><side-content>Benieuwd naar de positieve neveneffecten van investeringen in hernieuwbare energie? [Hier](https://docs.climateinteractive.org/projects/en-roads/en/latest/guide/renewables.html#potential-co-benefits-of-encouraging-renewables) vind je er een aantal.</side-content></side-ref>
[Scenario link](https://en-roads.climateinteractive.org/scenario.html?p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p30=-0.07&p36=2040&p53=1&p55=1&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/5.png)

#### Biomassa

_Stopzetten van nieuwe subsidies voor het verbranden van biomassa uit hout voor elektriciteitsopwekking. Voor lopende subsidies geldt als voorwaarde dat resthout wordt gebruikt en dat er geen oerbossen worden gekapt om biomassa te produceren. De normen voor de uitstoot van fijnstof door kleine biomassacentrales worden aangescherpt_.

Er is geen mogelijkheid in En-ROADS om de normen voor biomassacentrales aan te passen, maar laten we zeggen dat dit een vergelijkbaar effect heeft met een heffing op biomassa van **$10 per vat olie-equivalent** (fun fact: in het Engels heet deze eenheid "boe" - barrel of oil equivalent). Verder leidt deze maatregel tot verminderde ontbossing, laten we zeggen met **2% per jaar**. De totale hoeveelheid gebruikte bio-energie neemt daarmee op de lange termijn enigszins af, maar dit is niet genoeg om significante temperatuurverandering te bewerkstelligen. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p53=1&p55=1&p57=-2&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/6.png)

#### Elektrische auto's

Tja, de VVD zou de VVD niet zijn als ze niet minstens een halve bladzij over auto's zouden uitweiden (en opmerken dat benzinemotoren wel heel stoer klinken). Gelukkig gaat het wel over elektrificering van auto's. Laten we uitgaan van een elektrificering
<side-ref><side-content>De gevolgen van lithiumwinning voor automotoren in Chili zijn goed [gedocumenteerd door de NTR.](https://www.ntr.nl/Bodem-in-zicht/384/detail/Lithium/VPWON_1309236) Verduurzaming van lithiumwinning verdient meer aandacht.</side-content></side-ref>
van ongeveer **1%** van de gehele vloot per jaar. Dit komt bovenop de auto's die we al met waterstof van brandstof hebben voorzien. De hoeveelheid olie die wordt gebruikt neemt enigszins af, maar niet genoeg voor een significante verandering van de temperatuur. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p53=2&p55=1&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/7.png)

#### CO<sub>2</sub> heffing

_Een lagere energiebelasting voor huishoudens en kleinverbruikers. (...) Invoeren van een CO<sub>2</sub>-heffing voor de zware industrie. (...) Aanscherpen van het Europese emissiehandelssysteem ETS door meer CO<sub>2</sub>-rechten uit de markt te halen_

Op Europees niveau is ongeveer [26% van het energieverbruik industrieel](https://www.sciencedirect.com/topics/engineering/industrial-energy-consumption). De huidige prijs die de industrie in Europa betaalt voor uitstoot, is [€30 per ton](https://www.reuters.com/article/eu-carbon-idUSL5N2EK1E6). Laten we aannemen dat de VVD van plan is deze prijs te verhogen naar €50 per ton. Aangezien het om een kwart van de totale energie gaat, is dit effectief een prijs van €12.5 per ton. Bovendien wil de VVD energie voor huishoudens en het MKB goedkoper maken. Laten we zeggen dat we effectief
een heffing van **€8 per ton** overhouden. We zijn weer 0.1°C dichter bij ons doel, het aandeel hernieuwbare energie iets groter wordt. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p53=2&p55=1&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/8.png)

#### Verduurzaming gebouwen

_Toegang van het (kleine) mkb tot het warmtefonds dat nu al huiseigenaren financieel ondersteunt om te verduurzamen, zodat hun energierekening omlaag kan.(...) Fiscaal aftrekbaar maken van verduurzaming van de eigen woning via het eigenwoningforfait. (...) In stand houden van de lagere verhuurdersheffing voor woningcorporaties die hun woningvoorraad verduurzamen._

Ik voer dit in En-ROADS in als verduurzaming van **2%** van alle gebouwen per jaar. Met deze maatregel neemt de opwarming van de aarde weer met 0.1°C af. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=2&p53=2&p55=1&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/9.png)

#### Recycling

_Verduurzaming van onze economie door het bevorderen van hoogwaardige recycling, hergebruik en langer productgebruik_

Dit leidt tot een efficiënter energiegebruik in de industrie (laten we zeggen met **1%** per jaar) én tot een kleinere uitstoot van afval (ik heb met **2%** per jaar gerekend). Langzaam maar gestaag komen we dichter bij ons doel, weer 0.1°C eraf. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p209=1&p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=3&p53=2&p55=1&p60=-2&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/10.png)

#### Methaan en andere broeikasgassen

_Op Europees niveau geleidelijk stoppen met het gebruik van niet-essentiële, gevaarlijke stoffen, zoals PFAS. (...) Verminderen van de uitstoot van broeikasgassen en stikstof in de landbouw door middel van innovatieve technieken zoals precisielandbouw en emissiearme stalsystemen. (...) Verhogen van de grondwaterstand onder veenweidegebieden om de natuurlijke uitstoot van broeikasgassen te reduceren._ _(...)_ _Afspraken met producenten van levensmiddelen en supermarkten over het gezonder maken van producten én het meer promoten van gezonde producten._ (...) _Vermindering van schadelijke emissies voor de omgeving en natuur als gevolg van veeteelt._ (...) _Boeren in gebieden met een hoge veedichtheid die willen stoppen met hun bedrijf, kunnen rekenen op steun van de overheid. Financiële ondersteuning voor boeren om emissiearm te produceren._

PFAS vallen onder de zogenaamde [PFCs](https://www.epa.gov/pfas/what-are-pfcs-and-how-do-they-relate-and-polyfluoroalkyl-substances-pfass). Laten we uitgaan van een vermindering van het gebruik van methaan, stikstofoxide, PFCs en HFCs van **10%**, en een verminderde uitstoot van de landbouw van **10%**. Dit brengt ons weer 0.1°C dichter bij het Parijsakkoord. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p209=1&p210=1&p196=100&p202=2030&p4=2&p6=5&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=3&p53=2&p55=1&p60=-12&p61=-10&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/11.png)

#### Verduurzaming mobiliteit en transport

In het VVD programma wordt een reeks maatregelen voor duurzamer transport voorgesteld, zoals strengere normen voor fabrikanten van personenauto's en vrachtwagens, een belasting op kerosine en schonere motoren voor binnenvaartschepen. Verder is er sprake van verbetering van van auto-, spoor-, vaar- en fietswegen, verbetering van reistijden van internationale treinen en mobility as a service. Tegelijkertijd wordt de hubfunctie van Schiphol versterkt en wordt er gekeken naar efficiëntere vliegroutes om uitstoot te verminderen.

Toename van de efficiëntie van voertuigen met **2% per jaar** (ten opzichte van de huidige toename van 0.5% per jaar) en een heffing op kerosine van **$10 per vat olie-equivalent** zou ons weer 0.1°C dichter bij ons doel brengen. Qua efficiëntie van vliegroutes is er zeker voor de korte vluchten weinig te winnen, omdat de meeste energie vrijkomt bij [het opstijgen en landen](https://www.natuurenmilieu.nl/themas/mobiliteit/projecten-mobiliteit/luchtvaart/het-probleem/). Dit lijken me essentiële onderdelen van een vlucht. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p209=1&p210=1&p196=100&p202=2030&p4=2&p6=5&p7=10&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=3&p50=2.5&p53=2&p55=1&p60=-12&p61=-10&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/12.png)

#### Behoud gasnetwerken

_Zoveel mogelijk behouden van het bestaande gasnetwerk als de energievoorziening in wijken verandert, omdat het met aanpassingen in de toekomst mogelijk waterstof of groen gas kan transporteren._

Om huizen met waterstof van gas te voorzien, moet eerst elektriciteit worden omgezet in waterstof. Hierbij gaat ongeveer 20% van de elektriciteit verloren. Het is dus efficiënter om een huis elektrisch te verwarmen. Wat betreft vergroening is het enige voordeel de mogelijkheid tot het opslaan in tanks, wat tot een grotere buffercapaciteit leidt. Maar je kunt er geen temperatuurstijging mee voorkomen.

#### Bos

_Aanplanten van nieuwe hectares bos binnen natuurnetwerken._

[54 %](https://www.cbs.nl/nl-nl/nieuws/2016/08/minder-landbouw-meer-natuur) van de Nederlandse grond is landbouwgrond. Laten we aannemen dat we **1%** van het landoppervlak herbebossen (dat hoeft natuurlijk niet per se ten koste van landbouwgrond te gaan, we zouden bijvoorbeeld ook voor een IJsselmoerasbos kunnen kiezen). Als we dit wereldwijd willen opschalen, komen we voor grote uitdagingen te staan in gebieden met onregelmatige neerslag en of met toenemende behoefte aan landbouwgrond of met Jair Bolsonaro als president. Om een idee van de omvang van deze onderneming te geven, 1% op wereldwijde schaal betekent bebossing van ongeveer 2 keer India!
<side-ref><side-content>Lees meer over [de positieve effecten op biodiversiteit en luchtkwaliteit](https://docs.climateinteractive.org/projects/en-roads/en/latest/guide/afforestation.html#potential-co-benefits-of-increasing-afforestation)</side-content></side-ref>
 Helaas is bomen planten een beetje een hype, en is de uitstoot van de energiesector vele malen groten dan wat we kunnen bijplanten. Deze megalomane onderneming brengt ons slechts 0.1°C dichter bij ons doel. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p209=1&p210=1&p196=100&p202=2030&p4=2&p6=5&p7=10&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=3&p50=2.5&p53=2&p55=1&p60=-12&p61=-10&p65=100&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/13.png)

#### Innovatie

_Zo versterken we ook innovatieve regionale centra zoals Brainport Eindhoven en de Foodvalley rond Wageningen. (…) Proeftuinen waarin onderwijs, bedrijfsleven en overheid samenwerken aan oplossingen die bijdragen aan een gezonde bodem, duurzame bemesting en duurzame voedselproductie._

Innovaties in de landbouw (denk ook aan ontwikkeling van meer vleesvervangers en eventueel kweekvlees) zouden kunnen leiden tot een lagere uitstoot van methaan en stikstofoxide, bijvoorbeeld een reductie van **5%**. Daarnaast zouden we technologische innovaties kunnen doen op het gebied van koolstofverwijdering (denk aan [biochar](https://www.american.edu/sis/centers/carbon-removal/fact-sheet-biochar.cfm), [regeneratieve landbouw](https://www.american.edu/sis/centers/carbon-removal/fact-sheet-soil-carbon-sequestration.cfm) <side-ref><side-content>["Kiss the ground"](https://kissthegroundmovie.com/) is een mooie documentaire over regeneratieve landbouw</side-content></side-ref>
 en [mineralisatie](https://www.american.edu/sis/centers/carbon-removal/fact-sheet-enhanced-mineralization.cfm)). Laten we ervan uitgaan dat deze technologieën allemaal **33%** van hun geschatte potentiaal bereiken (ze bestaan ten slotte nog niet op grote schaal!). Dit doet de opwarming van de aarde met nog 0.2oC afnemen. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?p208=2&p209=1&p210=1&p196=100&p202=2030&p4=2&p6=5&p7=10&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=3&p50=2.5&p53=2&p55=1&p57=-2&p60=-17&p61=-10&p65=100&p72=33&p74=33&p76=33&p77=2030&g0=2&g1=62&v=2.7.35)

![]({static}/images/parijs/14.png)

### Conclusie

Ik schat dat het door de VVD voorgestelde beleid, zou leiden tot een temperatuurstijging van ongeveer 2.2°C (houd wel de [disclaimer]("#h5") in je achterhoofd!). Dit zou desastreuze gevolgen hebben.<side-ref><side-content>Lees meer over [het verschil tussen 1.5°C en 2°C](https://www.wri.org/blog/2018/10/half-degree-and-world-apart-difference-climate-impacts-between-15-c-and-2-c-warming) opwarming</side-content></side-ref> Toch zijn er meerdere redenen voor voorzichtig optimisme:

* De VVD regeert meestal met partijen die vooruitstrevender zijn op klimaatgebied

* Het gaat hier om een concept-verkiezingsprogramma, er is dus nog ruimte voor verbetering (hier schrijf ik binnenkort meer over in [een nieuwe blogpost](/posts/het-vvd-klimaatbeleid-suggesties-voor-verbetering/))

* Als we zo veel mogelijk mensen laten zien wat er nodig is op klimaatgebied (bijvoorbeeld met de (gratis!) [En-ROADS climate workshop](https://www.climateinteractive.org/tools/en-roads/the-en-roads-climate-workshop/)), komt er wellicht meer maatschappelijk draagvlak voor een progressiever klimaatbeleid.

### Feedback

Laat me weten welke aannames volgens jou niet kloppen! Pas [het eindscenario](https://en-roads.climateinteractive.org/scenario.html?p208=2&p209=1&p210=1&p196=100&p202=2030&p4=2&p6=5&p7=10&p16=-0.02&p21=10&p23=10&p30=-0.07&p36=2040&p39=8&p47=3&p50=2.5&p53=2&p55=1&p57=-2&p60=-17&p61=-10&p65=100&p72=33&p74=33&p76=33&p77=2030&g0=2&g1=62&v=2.7.35) zelf aan. Heb ik belangrijke punten uit het VVD programma onbenoemd gelaten? Je kunt me bereiken via _enroads \[at\] his.ke_ of via LinkedIn.

### Meer informatie over En-ROADS

Ben je benieuwd naar de En-ROADS climate workshop? Volg de workshop [op de En-ROADS website](https://www.climateinteractive.org/get-involved/webinars/) (in het Engels), bekijk een [lange](https://www.youtube.com/watch?v=R9W_KEXNzm4&t=0s) of een [korte](https://www.youtube.com/watch?v=u5mrnkOJdso) opname ervan op YouTube of doe mee met Het grote VN klimaatsimulatiespel van De Donutlobby!
