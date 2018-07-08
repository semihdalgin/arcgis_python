#Import der notwendigen Bibliotheken
import arcpy
import os

#Begruessung
print("***     Kachelexport mit MaxLike-Clas. und Raster To Polygon V.1.0     ***\n\n")

#Initialisierung des Projekts
projektpfad = raw_input ("Projektdatei mit Pfad und Endung: ")
mxd = arcpy.mapping.MapDocument(projektpfad)
df = arcpy.mapping.ListDataFrames(mxd)[0]



#Abfrage Ausdehnung und Massstab
xausdehnung = input ("Breite der benoetigten Ausdehnung (x-Ausdehnung) [m]: ")
yausdehnung = input ("Hoehe der benoetigten Ausdehnung (y-Ausdehnung) [m]: ")
massstab = input ("Massstabszahl: ")
df.scale = 50000
df.scale = massstab


#Berechnung des Bildausschnitts
breite = df.extent.XMax - df.extent.XMin
hoehe = df.extent.YMax - df.extent.YMin

#Speichern der Start-x-Koordinaten
startextent = df.extent
startextent.XMin = df.extent.XMin
startextent.XMax = df.extent.XMax
startextent.YMin = df.extent.YMin
startextent.YMax = df.extent.YMax
df.panToExtent(startextent)

#Initialisieren der x/y-Kachelzaehler und der Kachelliste
kachelx = 1
kachely = 1
kacheln = []

#Abfrage Ausgabeordner und Erstellung des selbigen
ausgabepfad = raw_input ("Ausgabepfad: ")
if not os.path.exists(ausgabepfad): #Abfrage ob Ordner bereits existiert
        os.mkdir(ausgabepfad)       #Pfad erstellen

#Abfrage des *.gsg-Files
gsgfile = raw_input ("Pfad und Dateiname des *.gsg-Files fuer die MLC: ")


#Berechnung der benoetigten Kachelzahl mittels Ganzzahldivision
anzkachelnx = int(xausdehnung) / int(breite) + 1
anzkachelny = int(yausdehnung) / int(hoehe) + 1

print ("Es werden " + str(anzkachelnx) + " x " + str(anzkachelny) + " (=" + str(anzkachelny * anzkachelnx) + ") Kacheln exportiert.")
print ("Breite je Kachel: " + str(breite) + ", Hoehe je Kachel: " + str(hoehe))


#Hauptschleife (Export)
while kachely <= anzkachelny:   #Zaehler fuer Zeilen
    while kachelx <= anzkachelnx:   #Zaehler fuer Spalten
        pfad = os.path.join(ausgabepfad, (r"Export_y%02d_x%02d.png" % (kachely, kachelx)))  #Berechnung des Pfads
        arcpy.mapping.ExportToPNG(mxd, pfad, df, int(breite) , int(hoehe) ,96,True)    #Export in Pfad
        kacheln.append(pfad)    #Einfuegen des Pfads in die Liste
        print (pfad)    #Anzeige der bearbeiteten Kacheln

        #Berechnung der neuen Kachel
        newextent = df.extent
        newextent.XMin = df.extent.XMin + breite
        newextent.XMax = df.extent.XMax + breite
        newextent.YMax = df.extent.YMax
        newextent.YMin = df.extent.YMin
        df.extent = newextent
        df.panToExtent(newextent)   #zur neuen Kachel schwenken
        kachelx = kachelx + 1   #Spaltenzaehler erhoehen
    #Sprung in neue Zeile
    newextent.XMin = startextent.XMin
    newextent.XMax = startextent.XMax
    newextent.YMax = df.extent.YMax - hoehe
    newextent.YMin = df.extent.YMin - hoehe
    df.extent = newextent
    df.panToExtent(newextent)   #zur neuen Kachel schwenken
    kachelx = 1 #Spaltenzaehler zuruecksetzen
    kachely = kachely + 1 #Reihenzaehler erhoehen


#MLClassification durchfuehren
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
a = 1
polyList = []
print ("MaxLikeClassification...")
for kachel in kacheln:
        mlcOut = MLClassify(kachel, gsgfile ,"","","","")
        polyPfad = os.path.join(ausgabepfad, (r"MLC_%03d.shp" % a))
        polyList.append(polyPfad)
        arcpy.RasterToPolygon_conversion(mlcOut, polyPfad, "NO_SIMPLIFY", "")
        print (a)
        a = a + 1
print ("Merging...")
arcpy.Merge_management(polyList, os.path.join(ausgabepfad, r"mergedPolygon"))
print ("Fertig.")
warte = input()




