# Ut.no GPX parser

In this repository have I created a Pythonscript for parsing GPX data downloaded from the Norwegian hikeplanningsite ut.no. The issue with the GPX files downloaded are that they do not interact that well with Garmins Basecamp or explorer wesite. For instance one of the issues are that the name of the cabin does not properly load. This program therefore converts the downloaded GPX files into files which can be read using Garmin Basecamp. However as I like to have certain metadata about the different cabins, this script also adds various metadata to the new GPX which then are added into the waypoint in Basecamp. Be adviced that some elements in the resulting GPX file is written in Norwegian.

## Metadata file
For easier creating the metadatafile, I use Google Sheets where multiple of the datafield are dropdown menys. This is to reduce the change of error as for instance writing Jotunheimen in two different ways; Jotunheimen and Kotunheimen would lead to the cabins being sorted differently.

The required metadata is given as a csv file with the following fields:
- Name: 
    - *Not actually used in the script, only used in the csv for knowing easier idetifying the cabin in the row*
- GPX_file: 
    - *GPX filename of the cabin withouth the .gpx file type identifier*
- Type: 
    - *Type of waypoint*
    - *This data gets added to the tagged categories of the waypoint*
    - *This value is linked to the type of icon the waypoint gets in Basecamp. Only a few icons are used, so the Depot type gets a type of crate, the Foodstore gets a type of shopping center icon and the rest gets a cabin icon*
    - *Examples: DNT, Private, Statsskog, Depot, Foodstore*
- Stafftype: 
    - *Type of staffing in the cabin*
    - *This data gets added to the tagged categories of the waypoint*
    - *Examples: Betjent, Selvbetjent, Ubetjent, Koie*
- Beds: 
    - *The amount of beds in the cabin*
    - *This data gets added to the description of the waypoint*
- Area: 
    - *Which mountain area the cabin is located in*
    - *This data gets added to the tagged categories of the waypoint*
    - *This data is linked to the filenames of the resulting GPX files. This scripts sort the huts into GPX files based on area, so that for instance the areas Hardangervidda and Jotunheimen would give the resulting GPX files: Hardangervidda.gpx and Jotunheimen.gpx containing the respective huts in that area* 
    - *Examples: Hardangervidda or Jotunheimen*
- Lock: 
    - *What type of lock it is in the cabin*
    - *This data gets added to the tagged categories of the waypoint*
    - *Examples: DNT-key, Specialkey, Open* 
- Season
    - *Season of the cabin, typically if there are some periods where the cabin is closed*
    - *This data gets added to the description of the waypoint*
- Other
    - *This is an open field for any other information it might be desirable to add*
    - *This data gets added to the description of the waypoint*

### Example csv
Name,GPX_file,Type,Stafftype,Beds,Area,Lock,Season,Other

Kalhovd Turisthytte,ut-no_kalhovd-turisthytte,DNT,Betjent,75,Hardangervidda,DNT-Nøkkel,Stengt mid okt til slutt feb,

Gjendebu,ut-no_gjendebu,DNT,Betjent,119,Jotunheimen,Betjent,Stengt mid okt til slutt feb,

Fondsbu,ut-no_fondsbu,DNT,Betjent,100,Jotunheimen,Åpen,Stengt mid okt til slutt feb,

Kljåen,ut-no_kljen,DNT,Selvbetjent,8,Skarvheimen,DNT-Nøkkel,Stengt mid okt til slutt feb,

Lågaros,ut-no_lgaros,DNT,Selvbetjent,38,Hardangervidda,DNT-Nøkkel,Stengt mid okt til slutt feb,

Ljosland Fjellstove,ut-no_ljosland-fjellstove,Privat,Betjent,48,Setesdalsheiene,Åpen,Hele året,

Solheimstulen,ut-no_solheimstulen,DNT,Betjent,60,Hardangervidda,Betjent,Usikkert,

## Using the script
1. Download the GPX files from ut.no and fill ou trequired metadata for all desired huts
2. Origanize the filestructure as shown in filestructure in section below
3. Change the three selection varaibles in the script: metadataFile, cabinGpxFolder and processedGpxFolder
4. Run the script

**How to import to Basecamp:**
1. In your collection in Basecamp, create a new folder. In Norwegian, it is called "Listemappe". Call it something resonable, for instance "Cabins"
2. Mark the new folder you created -> press "file" -> choose the option: "Import to 'Cabins'"
3. In the fileexplorer, mark all the new GPX files you want to import and press "open"
4. It should now have been created a new list for all the different areas where all the cabins for that area are placed within that list


### File structure when running script
|--- gpx_parser.py

|--- metadata.csv

|--- gpx_from_ut.no_folder

|---|--- my_cabin_1.gpx

|---|--- my_cabin_2.gpx

|---|--- my_depot_1.gpx

## DISCLAIMER: 
This is only a script I created before an expedition of walking across Norway, so it is only briefly tested and highly specialized on the current GPX format from ut.no and my metadata structure. So it may contain bugs and it is vulnerable if input data does not follow the same structure as my inputdata. So I guarantee nothing regarding functionallity, but at least there are no known bugs at the moment :)
