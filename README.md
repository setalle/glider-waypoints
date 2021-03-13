## Sandro's Gliding Waypoints Repository

### The reason for this Repository

The internet is full of files of waypoints containing 'outlandings' that are wrong or old. Even reasonably trustworthy sources like xcsoar are IMHO not trustworthy enough when it comes to possible outlanding fields in the mountains. So, what I do is **I distill my own waypoint file using the sources that *I hope* are more trustworthy**.  So - having during the lockdown more time than I usually do -  I have set up this repositoritory to maintain my own set of waypoints and facilitate the exchange of information.

### DISCLAIMER: use at your own risk **you are welcome to use the data and the scripts in this repository, but this is at your own risk: there is no explicit nor implicit guarantee of the correctness, the safety nor the security of the data and the programs presented here**


### My naming conventions
I think that when using an instrument like the OUDIE, it is important to be able to assess the quality and the reliability of an outlanding right from the waypoint's name. First, because I tend to forget how good an outlanding is. Secondly, because bedore entering a zone I am not completely familiar with, I like to review the options I have by looking at the list of reachable landables, and having an (**albeit with no guarantee**) indication of the nature of the outlandings in the list is an extra step towards safer flying. 

- ```_9 _8 .... _4```: the number indicates the quality of a field, where 9 is an airfield, 8 is easy, 7 is ok, 6 is delicate, 4 and 5 are for emergency.
- ```_ul```: an ultralight field, they are good but often difficult to find  
- ```_?``` checked on Google Earth, but the source is not one one I consider reliable (see page on sources)
- ```_??``` unchecked, unreliable, to be verified
- ```_S```  is present in the list of  waypoints of seeyou (usually a pretty good source)

In some cases these symbols are combined: 
- ```_ul8``` ultralight field, but not ideal (e.g. very short or narrow)
- ```_8?```  should be an 8, but the source is not one I consider reliable

### My files - USE AT YOUR OWN RISK

- [SanAlps21.cup](./SanAlps21.cup) my file for the Alps
- [cu20san.cup](./cu20san.cup) file of Seeyou 2020 where I have removed the outlandings that are in SanAlps and/or wrong. 
- [SanAlps21.kml](./SanAlps21.kml) corresponding kml file for Google Earth (not necessarily very updated)

My file for the Rieti and the neigboorhood

#### Wrong Outlandings

One of the main problems in maintaining an up-to-date collection of outlandings is that it is difficult to eliminate from the waypoint files of those outlandings that are not up-to-date any longer. Old ultralight fields, for example, but also fields that are not suitable any longer because of new crops (also fields that were never meant to be a decent outplanding are commonly found in waypoint files). When you merge waypoints from different sources it these "deprecated" fields have the tendency to sneak in again. To this end, I maintain a list of "wrong" waypoints; that is, outlandings that I suspect are not suitable (any longer). 

- [wrong_waypoints.cup](./wrong_waypoints.cup)

If you have python, to find out whether your waypoint file contains any of the deprecated waypoints according to my list, you can use (at your own risk) the script `wptool.py` with the command `python wptool.py diff wrong_waypoints.cup yourfilename.cup`. See section "My script" below. 

### My scritpt - USE AT YOUR OWN RISK

The python script I have prepared is [wptool.py](./Python/wptool.py). You need to have python (v3, I think), and you can invoke it with 
``$python wptool.py`` (or replace the first line with your python path, if you know what you are doing).  
Typical usage is  ``$python wptool.py cmd file1.cup [file2.cup]``. To see the list of possible commands, invoke it with no arguments (``$python wptool.py`` ).

### My sources 

This directory contains the sources I have used to distill my own WP files. I have added the suffix SAN after converting a file to the new seeyou format and adapting it to my own labeling method. 

##### Enemonzo
Excellent repository you can find at [CVNE](http://www.cvne.it/). They even have "factsheets" and videos. NOTE: I have added two fields that were not in the .cup file but were present in the  the factsheets ("schede") they posted. Their .cup file contains many mire landables than their factsheets.
My local copy is [here] (./WP_Originals/Enemonzo/Enemonzo20totalSAN.cup)

##### Valbrembo
Another excellent repository from the site [AVA Valbrembo](http://www.ava-valbrembo.it).

##### Soaring Web France
This is excellent, from the [site](https://soaringweb.org/TP/AP_alpes), updated in 2020. There is a google earth at the [site](http://www.planeur.net/_download/divers/TERRAINS%20VACHABLES%20-%20ALPES%20FRANCAISES.kmz)
In the file `apalpsv3SAN2020.cup` I have added two fields wrt the original and changed a couple of coordinates after checking them on google earth. 

##### AVS
This is the file I got in 2020 from my friends in Verona. Lots of good stuff, but I am not sure how updated it is. I consider it a less trustworthy source. 
[Here is the local link of my AVS file](./WP_Originals/AVS/AVS4.4.2016.cup)

##### Seeyou
Generated in November 2020 using the seeyou waypoint generator. My feeling is that the quality is very good (I haven't found any incorrect field); but  there are only very few outlandings here. 

##### Rieti. Updated in 2020, the one given to participants to the CCR race.

##### XCsoar
These are the points downloaded from [https://www.xcsoar.org/download/waypoints/](https://www.xcsoar.org/download/waypoints/)I don't trust them: I found too many 'old' fields. The other source XCsoar refers to is the one of [soaringweb](https://soaringweb.org/), which contains a bunch of different files, mostly outdated  (but not all outdated: the French file there is excellent).

##### ulm.it
This is still TBD, it should be a good file for the ultralight fields

##### Notes
[My notes in Italian](./NOTE_WAYPOINTS.txt)




