## Sandro's Waypoints Repository: The Source files

##### DISCLAIMER: USE AT YOUR OWN RISK!
##### DISCLAIMER 2: all statements are "IMHO"

This directory contains the sources I have used to distill my own WP files. I have added the suffix SAN after converting a file to the new seeyou format and adapting it to my own labeling method. 

##### Enemonzo
Excellent repository you can find at [CVNE](http://www.cvne.it/). They even have "factsheets" and videos. NOTE: I have added two fields that were not in the .cup file but were present in the  the factsheets ("schede") they posted. Their .cup file contains many mire landables than their factsheets.

##### Valbrembo
Another excellent repository from the site [AVA Valbrembo](http://www.ava-valbrembo.it).

##### Soaring Web France
This is excellent, from the [site](https://soaringweb.org/TP/AP_alpes), updated in 2020. There is a google earth at the [site](http://www.planeur.net/_download/divers/TERRAINS%20VACHABLES%20-%20ALPES%20FRANCAISES.kmz)
In the file `apalpsv3SAN2020.cup` I have added two fields wrt the original and changed a couple of coordinates after checking them on google earth. 

##### AVS
This is the file I got in 2020 from my friends in Verona. Lots of good stuff, but I am not sure how updated it is. I consider it a less trustworthy source. 

##### Seeyou
Generated in November 2020 using the seeyou waypoint generator. My feeling is that the quality is very good (I haven't found any incorrect field); but  there are only very few outlandings here. 

##### XCsoar
These are the points downloaded from [https://www.xcsoar.org/download/waypoints/](https://www.xcsoar.org/download/waypoints/)I don't trust them: I found too many 'old' fields. The other source XCsoar refers to is the one of [soaringweb](https://soaringweb.org/), which contains a bunch of different files, mostly outdated  (but not all outdated: the French file there is excellent).

##### ulm.it
This is still TBD, it should be a good file for the ultralight fields

##### My own notes (in Italian), regarding intermediate files etc. 


```

**** WP 2020 ****

TBD: Aggiungere germania e Olanda a Seeyou2020
seeyou2020 contiene pochi punti
notazione: NF = new format

#### SORGENTI

SanAlps20NOENENOVAL.cup: SanAlps 2020 in cui ho tolto Valbrembo e Enemonzo. Da usare come sorgente futuro
SanAlps21.cup trimmato sanalps20, aggiunto Enemonzo, Valbrembo
SanAlps21v2.cup aggiunto i Francesi
SanAlps21v3.cup aggiunto quelli di AVS preventivamente trimmati e in cui si vede nel label che sono AVS
TBD: decidere cosa fare con i files di SeeYou e come fare il merging con quelli del sud


ENEMONZO: www.cvne.it hanno 
- un file .cup per gli outlandings (orografia.3.4.2020.cup mantenuto regolarmente, copre solo la parte EST), 
- un file per l'orografia (non e' uguale a quello dell'AVS TBD: vedere quale e' meglio)
- schede per gli atterraggi
- file loro landing_near_ene_13.3.2020.cup CHE PERO' HA COSE CHE
MANCANO DALLE SCHEDE (Armentarola, Campitello di Fassa) e un sacco di
punti di cui non ci sono le schede
Fatti due file:
- Enemonzo20schedaSAN.cup: file di Enemonzo di quelli con la scheda,
in cui ho aggiunto (incluso Armentarola e Campitello di Fassa)
- Enemonzo20noscheda.cup (che sono ancora da controllare, e sono quasi
tutti buoni)
- Enemonzo20noschedaSAN.cup (Enemonzo senza scheda controllati e
numerati da me
- ricombinati insieme nel file Enemonzo20totalSAN.cup)

VALBREMBO http://www.ava-valbrembo.it
- hanno 44 campi con le schede
- sembra ci siano tutti nel file dell'AVS (non ho un file separato, magari bisogna farlo)
- c'e' un aggiornamento nel 2016 che indica 4 campi brutti
- i punti sono tutti nel file AVS. Molti mancano da me
- Valbrembo_originals.cup: presi quelli dall'AVS che appaiono nelle schede e messi qui (non avevo il file originale Vlabrembo, l'ho ricreato in questa maniera).
- ValbremboSAN.cup: tradotti nel mio linguaggio



AVS
AVS_4.4.2016_NF_outlandings_trimmed.cup: preso il file AVS, messo nel nuovo formato e tolto quello in SanAlps, Enemonzo, Valbrembo e DAI FRANCESI


XCSOAR ha due sorgenti:
a) quello a https://www.xcsoar.org/download/waypoints/ (che e'
organizzato bene, ma i waypoints non sono aggiornato e
b) quello di soaringweb soaringweb.org, dove c'e' di tutto e qualcuno
e' buono

SOARINGWEBFRANCE
Ottima, solo per la francia
https://soaringweb.org/TP/AP_alpes
Aggiornato al 2020
fantastica il file per google earth che si scarica a:
http://www.planeur.net/_download/divers/TERRAINS%20VACHABLES%20-%20ALPES%20FRANCAISES.kmz
file
apalpsv3SAN2020.cup: mess nel nuovo formato, aggiunto due campi, cambiato un paio di coordinate, messe nel mio codice


AVIOSUPERFICI: C'E UNA LISTA AGGIORNATA A http://www.ulm.it/hangar/campi/default.htm, ci sono due formati: WPT (mapsource.wpt piatto) e gpx (tipo xml). TBD: controllare se la wpt funziona bene 

I files che hanno il suffisso GD vuol dire che quelli in SBAD sono
stati eliminati, e che sono nel nuovo formato (2020) TBD


NOTA: la lista aggiornata dei campi di volo si trova a 


*** IN SBAD:
Arcisate Brezzo di Bedero Parè Sondalo: see http://www.ava-valbrembo.it/campi-atterrabili/

**** PER IL NORD ****

Sandro_Alps.cup ->
(ex Alp_wps_Sandro_based_on_TZiarko.cup)
Preso il file di Tomek Ziarko (fatto abbastanza da lui, molto buono) Alp_wps_Tomek_Ziarko_good.cup confrontato con (e a volte aggiunto qualcosa) "Scheda CVA http://www.ava-valbrembo.it" e CVNE (che sono entrambe un po' vecchie).
Alcune locazioni erano sbagliate. 
I campi con davanti un * sono quelli che ho controllato/aggiungo
I label sono: AE UL: ovvio
Numeri: 9: aeroporto, 8,7: molto buoni e buoni, 6,5: lasciare perdere
?: vuol dire che sarebbe da verificare
NBL Per Tomek e' un "A" (il massimo), per quanto vedo io e' un 2 (non il massimo). 

Alp_wps_Tomek_Ziarko_short.cup -> il file di Tomek Zlarko, in cui ho rimosso quelli che ho messo in Sandro_Alps.cup, e ho rimosso anche alcuni che non funzionavano piu'. 

Seeyou_land.cup -> i landables da Seeyou per Italia e dintorni, in cui
pero' mancano tanti landables listati da Ziarko.

Seeyou_land_short.cup -> i landables da Seeyou in cui
- ho tolto quelli che overlappano con Sandro_Alps.cup e Sandro_Rieti.cup 
- quelli verificati, li ho spostati in Sandro-???.cup
- DA RIMETTERE A POSTO

NB: PER IL NORD: l'idea e' quella di usare Sandro_Apls.cup +
SeeyouWP_short.cup. Eventualmente si possono integrare in futuro

Italy19_from_XCSoar.cup (aka Italy.cup)-> 
       fatta con Italy.cup di XCSOAR e cambiato l'header per farlo digerire a seeyou
       - ci sono (pochi) fuoricampo (manca il barone, per esempio),
       sono da verificare
       - ci sono UN SACCO DI AVIOSUPERFICI SBAGLIATE e VECCHIE
Italy19_Sandro_out.cup _>
    Preso Italy.cup, selezionato gli outlandings e verificato con (per ora) cnve.it
    Aggiunto campi dal CVA, TBD Bisuschio, Bormio, Giustino, Iseo,Muscoline,Pasturo    

Italy19_fromXCSoar_short.cup -> Col file di cui sopra in cui
- tolto molti degli overlapping con Sandro.cup
- tolto molte aviosuperfici inesistenti

**** PER IL SUD ****

Agosto 2020

(siccome continuano a cambiare il files, adesso abbiamo due files):
- Rieti2020+v3+SAN.cup versione del Rieti 2020v3 con i labels "sandrizzati"
- SanRietiAdd_1.0.cup : file di sandro con degli atterraggi aggiuntivi (Salto + altre aviosuperfici "lontane") + i keypoints (che adesso non servono piu')

Sandro_Rieti_out.cup:
Nel 2019
- preso il file Rieti2018_turnpoint_V2.cup
- fatto il check si TUTTE le aviosuperfici e aeroporti (con avioportolano), corretti un tot di errori e rimossi alcuni outlandings che secondo me non esistono piu' (SI VEDA LISTA SOTTO, INCOMPLETA)
- aggiunto diverse aviosuperfici che mancavano
- a tante aviosuperfici ho cambiato il nome per rispecchiare quello in uso adesso
- le aviosuperfici e gli aeroporti adesso hanno il nome NOME-NUMERO, dove NUMERO=9 se e' larga e lunga abbastanza, 8 - 7 ... 5 se si fa piu' fatica, per esempio: DELFINA-9, ma CIANNOCIO-5 (perche' e' larga solo 15 metri)
- alcuni degli outlandings hanno il numero come le aviosuperfici: es. GUALDO-7
- gli outlanding non testati (pochi) sono rimasti con la dicitura vecchia NOME-X


** ALCUNE DELLE COSE CAMBIATE:
"CAMOC-X" -> Volo molise
"CARSOL-X" -> Aviosup il Pratone
"CASCIA-A" -> Avios S Rita, stretta
PEALA-X -> ASCANIO "Aviolanno Corradino d'Ascanio"
CASTELVISCA-A -> ALFINA
"ALIIBE-X -> "9ALILIBERE"
"CALEDR-x" -> CALLEDRO 
"CIANOC-X" -> 5CIANNOCCIOUL STRETTA
"CiCASTELLO-X" -> Belardinelli
"CORFIN-X", -> Parchi d'abruzzo
"PEALA-X -> Ascanio
"ROCCAPI-X", -> piana 5 miglia
"SSEPOLCRO-A" -> palazzolo, strettina
"TODI-A" -> PANTALLA
"VALDICH-A" -> Valdichiana

** ALCUNE DELLE COSE RIMOSSE
"?BLUWIN-X",BLUWIN,,4201.000N,01354.000E,500.0m,3,0,0.0m,,"SECONDO ME NON ESISTE PIU' Rwy dir:    070 Rwy len:      0m  0.000"
"?LAPIAN-X",?LAPIAN,,4144.867N,01405.350E,820.0m,3,0,0.0m,,"SECONDO ME NON ESISTE PIU"
"?ACQASP-X",ACQASP,,4241.400N,01233.950E,300.0m,3,0,0.0m,"130.00","SECONDO ME NON ESISTE PIU = F-ACQASP        Rwy dir:    018 Rwy len:    300m 130.00"
"FIANOR-X", Rimossa, SECONDO ME O NON `ESISTE PIU' O NON E' MAI ESISTITA  ma ci sono 3 aviosuperfici nelle vicinanze (tra cui Tucano e Capena)
"PREZZA-X",PREZZA,,4204.100N,01350.383E,360.0m,3,0,0.0m,"SECONDO ME NON ESISTE PIU 130.000","F-PREZZA        Rwy dir:    030 Rwy len:    500m 130.000"
GRUMEN-A" -> coordinate sbagliate?


***** V 2.2, 2020
SanRieti2.1.cup := Sandro_Rieti_out.cup in cui ho aggiunto i tasks di Rieti2018_turnpoint_V2.cup, e poi aggiornato alla versione 2020 di Rieti2018_turnpoint_V2.cup
fondamentalmente aggiunta borgo San Lorenzo E POI SUBITO RIMOSSA, nella versione 2.2!
Gualdo Tadino l'ho lasciata con un 7, ma bisogna vedere se e' ancora buona. 


****** V3: 2020, basata su Rieti2020, mandata la mail agli organizzatori:
Ho rimesso anche i nomi simili a quelli di Rieti (eg, invertito i cambi come "CORFIN-X", -> Parchi d'abruzzo), in modo da rendere la manutenzione piu' semplice


1) Questo era un fuoricampo "ufficiale" fin o all'anno scorso, c'e' qualche ragione per averlo rimosso?
"SALTO-X?",SALTOX?,,4214.783N,01306.717E,562.0m,3,0,0.0m,,"X-SALTO - tolta nella versione 2020, ma io l'ho tenuta",,

2) QUESTA ERA LA PISTA DELL'ASSOCIAZIONE VOLO MOLISE, CHE ORA E' DISMESSA, io credo che le piste dismesse siano particolarmente "pericolose" come fuoricampo (ci puo' essere di tutto in quello che prima era una pista),
"CAMOCH",CAMOCH,,4127.600N,01432.067E,530.0m,3,0,0.0m,,"F-CAMOCH        Rwy dir:    120 Rwy len:    520m  0.000"

3) LE COORDINATE DI GRUMENTUM SONO SBAGLIATE:
"GRUMENA",GRUMENA,,4015.317N,01554.867E,610.0m,2,0,0.0m,,"Grumentum Aviosuperficie"
DOVREBBERO ESSERE: 
"GRUMEN9",GRUME9,IT,4016.200N,01554.840E,611.0m,5,70,1000.0m,,"17/25 Grumentum Aviosuperficie"

4) Problema a Borgo S Lorenzo:
"BORGOSL",BORGOSL,,4359.400N,01117.333E,300.0m,2,0,0.0m,,"Borgo San Lorenzo"
A queste coordinate c'e' un prato ma nessuna aviosuperficie (secondo l'Avioportolano). L'aviosuperficie di Borgo San Lorenzo e' COLLINA (coordinate sotto)(NB: qui uso il nuovo formato di seeyou)
"COLLIN-9",COLLN9,IT,4359.220N,01123.280E,290.0m,2,40,720.0m,,,"22/04 720X35 Collina Borgo San Lorenzo",
e vicino ce n'e' anche un'altra:(NB: qui uso il nuovo formato di seeyou)
"RSTORAI-9",RSTO9,IT,4357.914N,01127.492E,271.0m,2,20,600.0m,,,"02/20 600X30 Aviosuperficie Renzo Storai. Portolano da confermare",

4) Questa Non e' un'aviosuperficie (al massimo un prato) 
"PREZZA",PREZZA,,4204.100N,01350.383E,360.0m,3,0,0.0m,"130.000","F-PREZZA        Rwy dir:    030 Rwy len:    500m 130.000"

5) Questa non e' piu' un'aviosuperficie (secondo Avioportolano):
"FIANOR",FIANOR,,4208.800N,01237.783E,30.0m,3,0,0.0m,"130.00","Fiano Romano 130.00"
In compenso ce ne sono altre 3 vicinissime (NB: qui uso il nuovo formato di seeyou)
"TUCANO-9",TUCAN9,IT,4207.920N,01237.620E,23.0m,2,90,600.0m,"17/35 620x30 09/27 660x30 DUE PISTE radio 130.000 ",,,
"EASYFLY-9",EASYF9,IT,4207.573N,01236.591E,23.0m,2,90,310.0m,"09/27 310x22 grass avios. Easy Flyte Maremma",,,
"CAPENA-9",CAPEN9,IT,4207.200N,01236.300E,24.0m,2,120,740.0m,"12/30 740x20 aka Roma Nord-Capena",,,

6) Non capisco cosa ci sia qui, secondo me la zona e' inatterrabile
"BLUWIN",BLUWIN,,4201.000N,01354.000E,500.0m,3,0,0.0m,,"F-BLUWIN        Rwy dir:    070 Rwy len:      0m  0.000"

7) Qui secondo me (e secondo Avioportolano) non c’e’ nessuna aviosuperficie 
"ACQASP",ACQASP,,4241.400N,01233.950E,300.0m,3,0,0.0m,"130.00","F-ACQASP        Rwy dir:    018 Rwy len:    300m 130.00”

Rimossa:
"ACQASP",ACQASP,,4241.400N,01233.950E,300.0m,3,0,0.0m,"130.00","F-ACQASP        Rwy dir:    018 Rwy len:    300m 130.00"
"BLUWIN",BLUWIN,,4201.000N,01354.000E,500.0m,3,0,0.0m,,"F-BLUWIN        Rwy dir:    070 Rwy len:      0m  0.000"
"FIANOR",FIANOR,,4208.800N,01237.783E,30.0m,3,0,0.0m,"130.00","Fiano Romano 130.00"



****** SOURCES ******

campi_estesa.gpx e campi_estesa.cup: sono i campi scaricati da ulm.it as of 05 2019,
- buoni ma non buonissimi, per esempio l'aviosiperficie VIDOR e' ancora
contata.
- Tradotta in campi_estesa.cup usando gpsbabel pero' si perde
l'elevation, e la MA RIMANE UNA BUONA SORGENTE di dati

Rieti_outlanding -> forse vecchia, mancano Delfina e Celano. Ci sono atterraggi al limite (e.g. val Nerina) 

Rieti2018_turnpoint_V2.cup -> sembra buona, ci sono atterraggi al limite (e.g. val Nerina) manca Leonessa.
       
```

