#######################################################################
# FILENAME : gpx_parser.py
#
# DESCRIPTION : This script parses GPX files from ut.no and 
#   merges data from those files with metadata stored in a 
#   csv file. The data is parsed into a new GPX file whilch 
#   is readable by Garmins Basecamp
#
# NOTES :
#    The script requires 3 inputs in the code:

metadataFile = 'testfile2.csv'  # Filename of the csv file containing metadata
cabinGpxFolder = 'GPX_from_UT'  # Foldername of the folder where the GPX files from ut.no is stored
processedGpxFolder = 'fixedGPX' # Foldername for where the new processed GPX files will be stored

#
# AUTHOR :    Markus Rud        Initially released: XX.XX.2023
#
# CHANGES :
#
#######################################################################

from xml.dom import minidom
from xml.etree import cElementTree as ET
import datetime
import os, glob
import csv

def createHeaderData(root):
    xml = root.createElement('gpx') 
    xml.setAttribute('creator', 'Garmin Desktop App')
    xml.setAttribute('version', '1.1')
    xml.setAttribute('xsi:schemaLocation', 'http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/ActivityExtension/v1 http://www8.garmin.com/xmlschemas/ActivityExtensionv1.xsd http://www.garmin.com/xmlschemas/AdventuresExtensions/v1 http://www8.garmin.com/xmlschemas/AdventuresExtensionv1.xsd http://www.garmin.com/xmlschemas/PressureExtension/v1 http://www.garmin.com/xmlschemas/PressureExtensionv1.xsd http://www.garmin.com/xmlschemas/TripExtensions/v1 http://www.garmin.com/xmlschemas/TripExtensionsv1.xsd http://www.garmin.com/xmlschemas/TripMetaDataExtensions/v1 http://www.garmin.com/xmlschemas/TripMetaDataExtensionsv1.xsd http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensions/v1 http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensionsv1.xsd http://www.garmin.com/xmlschemas/CreationTimeExtension/v1 http://www.garmin.com/xmlschemas/CreationTimeExtensionsv1.xsd http://www.garmin.com/xmlschemas/AccelerationExtension/v1 http://www.garmin.com/xmlschemas/AccelerationExtensionv1.xsd http://www.garmin.com/xmlschemas/PowerExtension/v1 http://www.garmin.com/xmlschemas/PowerExtensionv1.xsd http://www.garmin.com/xmlschemas/VideoExtension/v1 http://www.garmin.com/xmlschemas/VideoExtensionv1.xsd')
    xml.setAttribute('xmlns', 'http://www.topografix.com/GPX/1/1')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xmlns:wptx1', 'http://www.garmin.com/xmlschemas/WaypointExtension/v1')
    xml.setAttribute('xmlns:gpxtrx', 'http://www.garmin.com/xmlschemas/GpxExtensions/v3')
    xml.setAttribute('xmlns:gpxtpx', 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1')
    xml.setAttribute('xmlns:gpxx', 'http://www.garmin.com/xmlschemas/GpxExtensions/v3')
    xml.setAttribute('xmlns:trp', 'http://www.garmin.com/xmlschemas/TripExtensions/v1')
    xml.setAttribute('xmlns:adv', 'http://www.garmin.com/xmlschemas/AdventuresExtensions/v1')
    xml.setAttribute('xmlns:prs', 'http://www.garmin.com/xmlschemas/PressureExtension/v1')
    xml.setAttribute('xmlns:tmd', 'http://www.garmin.com/xmlschemas/TripMetaDataExtensions/v1')
    xml.setAttribute('xmlns:vptm', 'http://www.garmin.com/xmlschemas/ViaPointTransportationModeExtensions/v1')
    xml.setAttribute('xmlns:ctx', 'http://www.garmin.com/xmlschemas/CreationTimeExtension/v1')
    xml.setAttribute('xmlns:gpxacc', 'http://www.garmin.com/xmlschemas/AccelerationExtension/v1')
    xml.setAttribute('xmlns:gpxpx', 'http://www.garmin.com/xmlschemas/PowerExtension/v1')
    xml.setAttribute('xmlns:vidx1', 'http://www.garmin.com/xmlschemas/VideoExtension/v1')
    root.appendChild(xml)
    return xml

def createLevel(root, levelName, appenTo):
    level = root.createElement(levelName)  
    appenTo.appendChild(level)
    return level

def createElementAndAppend(root, elementName, elementText, appendTo):
    elementHeader = root.createElement(elementName)
    txt = root.createTextNode(elementText)  
    elementHeader.appendChild(txt) 
    appendTo.appendChild(elementHeader)


def addExtensionData(root, data, elementHeader, appendTo):
    extension = createLevel(root, elementHeader + ":WaypointExtension", appendTo)
    createElementAndAppend(root, elementHeader + ":DisplayMode", "SymbolAndName", extension)
    category = createLevel(root, elementHeader + ":Categories", extension)
    createElementAndAppend(root, elementHeader + ":Category", data['Type'], category)
    createElementAndAppend(root, elementHeader + ":Category", data['Stafftype'], category)
    createElementAndAppend(root, elementHeader + ":Category", data['Lock'], category)
    createElementAndAppend(root, elementHeader + ":Category", data['Area'], category)


def main():

    root_arr = {}
    xml_arr = {}
    filelist = []

    with open(metadataFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            try:
                if not line['Area'] in root_arr:
                    root = minidom.Document()
                    xml = createHeaderData(root)
                    root_arr[line['Area']] = root
                    xml_arr[line['Area']] = xml

                filelist.append(line['GPX_file'])

                try:
                    gpxfile = open(os.path.join(cabinGpxFolder, line['GPX_file'] + '.gpx'), newline='')        
                except FileNotFoundError:
                    print("WARNING: Metadata filename was not found in directory: " + line['GPX_file'])
                    continue

                name = ""
                link = ""
                lat = 0
                lon = 0

                tree = ET.parse(gpxfile)
                for elem in tree.iter():
                    if(elem.tag.find("name") != -1):
                        name = elem.text
                    if(elem.tag.find("link") != -1):
                        link = elem.get("href")
                    if(elem.tag.find("wpt") != -1):
                        lat = elem.get("lat")
                        lon = elem.get("lon")

                gpxfile.close()

                wpt = root_arr[line['Area']].createElement('wpt')
                wpt.setAttribute('lat', lat)
                wpt.setAttribute('lon', lon)
                xml_arr[line['Area']].appendChild(wpt)

                now = datetime.datetime.now()
                desc = "Senger: " + line['Beds'] + " | Sesong: " + line['Season'] + " | Annet: " + line['Other']
                createElementAndAppend(root_arr[line['Area']], "time", str(now.strftime("%Y-%m-%dT%H:%M:%SZ")), wpt)
                createElementAndAppend(root_arr[line['Area']], "name", name, wpt)
                createElementAndAppend(root_arr[line['Area']], "cmt", desc, wpt)
                createElementAndAppend(root_arr[line['Area']], "desc", desc, wpt)

                x = root_arr[line['Area']].createElement('link')
                x.setAttribute('href', link)
                wpt.appendChild(x)

                if (line['Type'] == "Depo"):
                    createElementAndAppend(root_arr[line['Area']], "sym", "Geocache", wpt)
                elif (line['Type'] == "Butikk"):
                    createElementAndAppend(root_arr[line['Area']], "sym", "Shopping Center", wpt)
                else:
                    createElementAndAppend(root_arr[line['Area']], "sym", "Lodge", wpt)
                    
                createElementAndAppend(root_arr[line['Area']], "type", "user", wpt)

                extensions= createLevel(root_arr[line['Area']], "extensions", wpt)

                addExtensionData(root_arr[line['Area']], line, "gpxx", extensions)
                addExtensionData(root_arr[line['Area']], line, "wptx1", extensions)

                ctx_ext= createLevel(root_arr[line['Area']], "ctx:CreationTimeExtension", extensions)

                createElementAndAppend(root_arr[line['Area']], "ctx:CreationTime", str(now.strftime("%Y-%m-%dT%H:%M:%SZ")), ctx_ext)
            except:
                print("WARNING: Some error processing data from:", line['GPX_file'])

    if not os.path.exists(processedGpxFolder):
            os.makedirs(processedGpxFolder)

    for key in root_arr:
        xml_str = root_arr[key].toprettyxml(indent ="\t")     

        save_path_file = os.path.join(processedGpxFolder, key + '.gpx')
            
        with open(save_path_file, "w") as f:
            f.write(xml_str) 

    for filename in glob.glob(os.path.join(cabinGpxFolder, '*.gpx')):
        normalized_filename = os.path.normpath(filename)
        onlyFileNameAndType = normalized_filename.split(os.sep)[1]
        onlyFileName = (os.path.splitext(onlyFileNameAndType)[0])
        
        try:
            filelist.index(onlyFileName)
        except ValueError:
            print("WARNING: GPX file not found in metadata: " + onlyFileName)

if __name__ == "__main__":
    main()
  
