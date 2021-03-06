#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      LerchM
#
# Created:     17.07.2015
# Copyright:   (c) LerchM 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Importiere arcpy- und os-Module
import arcpy, os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

kacheln = []

#Setze Standardwerte für Variablen
page = 1    #Grid-Feature-Zähler

#Begruessung
print(r"*** Kachelexport V 1 ***")

#Abfrage des mxd-Pfads
mxd_pfad = raw_input(r"Pfad der mxd-Datei (Kopieren aus Map Document Properties): ")

#Abfrage des Augabenamens
ausgabename = raw_input(r"Wie lautet der Ausgabename? (Kachelnumer wird automatisch ergaenzt) ")
ausgabename = str.rstrip(str(ausgabename), "_")  #Manipulations des Ausgabenamens um doppelte Unterstriche zu vermeiden

#Abfrage der Kachelausdehnung in Pixeln: Breite
ew = raw_input (u"Breite der Kacheln [Pixel] - 0/k.A. für Standard 3200: ")
if ew == '':
    ew = 3200
elif int(ew) == 0:
    ew = 3200
else:
    ew = int(ew)

#Abfrage der Kachelausdehnung in Pixeln: Breite
eh = raw_input (u"Hoehe der Kacheln [Pixel] - 0/k.A. für Standard 2400: ")
if eh == '':
    eh = 2400
elif int(eh) == 0:
    eh = 2400
else:
    eh = int(eh)

#Abfrage der Kachelausdehnung in Pixeln: Aufloesung
res = raw_input (u"Aufloesung [dpi] - 0/k.A. für Standard 300: ")
if res == '':
    res = 300
elif int(res) == 0:
    res = 300
else:
    res = int(res)

#Hauptschleife
while True:
    #Erstellen des Mapdocuments aus Pfad
    mxd = arcpy.mapping.MapDocument(mxd_pfad)
    #Definieren des Dataframes
    df = arcpy.mapping.ListDataFrames(mxd, "Layer")[0]
    #Definieren des Layerfiles
    lyr = arcpy.mapping.ListLayers(mxd, "grid_index", df)[0]
    #Definieren der SQL-Abfrage um das jeweilige Grid-Feature zu selektieren
    wherecl = '"PageNumber" = ' + "%s" %page
    #Selektion durchfuehren
    arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", wherecl)
    #Berechnen, wie viele Features selektiert wurden
    no_selected = arcpy.GetCount_management(lyr)
    #Check, ob 1 Feature selektiert wurde, ansonsten Abbruch
    if str(no_selected) == "0":
        break
    else:
        print (r"Grid-Feature Nr. %02d wurde gefunden und selektiert." %page)

    #Zoom auf Selektion
    df.zoomToSelectedFeatures()


    #Exportpfad berechnen
    exp_pfad = os.path.join(r"X:\09_Python_Skripte\Kachelausgabe", (ausgabename + "_%02d.png" %page))

    #Export durchfuehren
    arcpy.mapping.ExportToPNG(mxd, exp_pfad, df, df_export_width=ew, df_export_height=eh, resolution=res, world_file=True)
    #Ausgabe, wenn Export erfolgt ist
    print exp_pfad + " exportiert."

    kacheln.append(exp_pfad)    #Einfuegen des Pfads in die Liste

    #Clear the selection and refresh the active view
    arcpy.SelectLayerByAttribute_management(lyr, "CLEAR_SELECTION")
    arcpy.RefreshActiveView()
    #mxd-Variable resetten
    del mxd
    #Grid-Feature-Zähler hochsetzen
    page = page + 1

print (kacheln)

ausgabepfad = r"X:\09_Python_Skripte\Kachelausgabe"
gsgfile = r"X:\09_Python_Skripte\bebauung.gsg"


#MLClassification durchfuehren
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
a = 1
polyList = []
confList = []
print ("MaxLikeClassification...")
for kachel in kacheln:
        polyPfad = os.path.join(ausgabepfad, (r"MLC_%03d.shp" % a))
        confPfad = os.path.join(ausgabepfad, (r"MLCConf_%03d" % a))
        polyList.append(polyPfad)
        confList.append(confPfad)
        mlcOut = MLClassify(kachel, gsgfile ,"","","", confPfad)
        arcpy.RasterToPolygon_conversion(mlcOut, polyPfad, "NO_SIMPLIFY", "")
        print (a + " fertig!")
        a = a + 1

print ("Merging...")
arcpy.Merge_management(polyList, os.path.join(ausgabepfad, r"mergedPolygon"))
print ("Fertig.")



#Export-Ordner öffnen
os.startfile(r"X:\09_Python_Skripte\Kachelausgabe")
