GPX_file = "ut-no_kalhovd-turisthytte.gpx"
Type = "DNT"
Stafftype = "Betjent"
Beds = 10
Area = "Hardangervidda"
Lock = "Åpen"
Season = "2. jun til 10. aug"

from xml.dom import minidom
import datetime

root = minidom.Document()
  
# Set header data
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



  
wpt = root.createElement('wpt')
wpt.setAttribute('lat', '62.53192138671875')
wpt.setAttribute('lon', '8.206787109375')
xml.appendChild(wpt)

now = datetime.datetime.now()
date = root.createElement("time")
txt = root.createTextNode(str(now.strftime("%Y-%m-%dT%H:%M:%SZ"))) 
date.appendChild(txt)
wpt.appendChild(date)  

x = root.createElement("name")
txt = root.createTextNode("Solheimstulen")  
x.appendChild(txt) 
wpt.appendChild(x) 
  
x = root.createElement("cmt")  
txt = root.createTextNode("testdesc") 
x.appendChild(txt)
wpt.appendChild(x)

x = root.createElement("desc")  
txt = root.createTextNode("testdesc") 
x.appendChild(txt)
wpt.appendChild(x)

x = root.createElement('link')
x.setAttribute('href', 'http://vg.no')
wpt.appendChild(x)

x = root.createElement("sym")  
txt = root.createTextNode("Lodge") 
x.appendChild(txt)
wpt.appendChild(x)

x = root.createElement("type")  
txt = root.createTextNode("user") 
x.appendChild(txt)
wpt.appendChild(x)

ext = root.createElement("extensions")  
wpt.appendChild(ext)

gpxx_ext = root.createElement("gpxx:WaypointExtension")  
ext.appendChild(gpxx_ext)

x = root.createElement("gpxx:DisplayMode")  
txt = root.createTextNode("SymbolAndName") 
x.appendChild(txt)
gpxx_ext.appendChild(x)

gpxx_cat = root.createElement("gpxx:Categories")  
gpxx_ext.appendChild(gpxx_cat)

x = root.createElement("gpxx:Category")  
txt = root.createTextNode("Hardangervidda") 
x.appendChild(txt)
gpxx_cat.appendChild(x)

x = root.createElement("gpxx:Category")  
txt = root.createTextNode("Betjent") 
x.appendChild(txt)
gpxx_cat.appendChild(x)

wptx1_ext = root.createElement("wptx1:WaypointExtension")  
ext.appendChild(wptx1_ext)

x = root.createElement("wptx1:DisplayMode")  
txt = root.createTextNode("SymbolAndName") 
x.appendChild(txt)
wptx1_ext.appendChild(x)

wptx1_cat = root.createElement("wptx1:Categories")  
wptx1_ext.appendChild(wptx1_cat)

x = root.createElement("wptx1:Category")  
txt = root.createTextNode("Hardangervidda") 
x.appendChild(txt)
wptx1_cat.appendChild(x)

x = root.createElement("wptx1:Category")  
txt = root.createTextNode("Betjent") 
x.appendChild(txt)
wptx1_cat.appendChild(x)

ctx_ext = root.createElement("ctx:CreationTimeExtension")  
ext.appendChild(ctx_ext)

x = root.createElement("ctx:CreationTime")  
txt = root.createTextNode(str(now.strftime("%Y-%m-%dT%H:%M:%SZ"))) 
x.appendChild(txt)
ctx_ext.appendChild(x)


xml_str = root.toprettyxml(indent ="\t") 
  
save_path_file = "testfile.gpx"
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
