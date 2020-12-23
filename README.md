## Sandro's Waypoints Repository

### DISCLAIMER: use at your own risk

I have set up this repositoritory to maintain my own set of waypoints and facilitate the exchange of information **you are wlcome to use the data and the scripts, but this is at your own risk: there is no explicit nor implicit guarantee of the correctness, the safety nor the security of the data and the programs presented here**

### The reason for this Repository


### My naming conventions
I think it is important to be able to assess rhe quality and the reliability of an outlanding right from its name. First, because I tend to forget. Secondly, because bedore entering a zone I am not familiar with, I like to review the options I have. To this end, I use the following peefixes:


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
- [SanAlps21.kml](./SanAlps21.kml) corresponding kml file for Google Earth 

My file for the Rieti and the neigboorhood

#### Wrong Outlandings

One of the main problems in maintaining an up-to-date collection of outlandings is that it is difficult to eliminate from the waypoint files of those outlandings that are not up-to-date any longer. Old ultralight fields, for example, but also fields that are not suitable any longer because of new crops (also fields that were never meant to be a decent outplanding are commonly found in waypoint files). When you merge waypoints from different sources it these "deprecated" fields have the tendency to sneak in again. To this end, I maintain a list of "wrong" waypoints; that is, outlandings that I suspect are not suitable (any longer). 

- [wrong_waypoints.cup](./wrong_waypoints.cup)

If you have python, to find out whether your waypoint file contains any of the deprecated waypoints according to my list, you can use (at your own risk) the script `wptool.py` with the command `python wptool.py diff wrong_waypoints.cup yourfilename.cup`. See section "My script" below. 

### My scritpt - USE AT YOUR OWN RISK


You can use the [editor on GitHub](https://github.com/setalle/waypoints.github.io/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.


