#-------------------------------------------------------------------------------
# Name:        Extract Roughness polygons
# Purpose:     Extract Roughness polygons
#
# Author:      LerchM
#
# Created:     30.04.2015
# Copyright:   (c) LerchM 2015
# Licence:     PNE Wind AG internal
#-------------------------------------------------------------------------------

#Arcpy importieren
import arcpy

#Lizenz pruefen
arcpy.SetProduct("ArcView")

#Koordinaten festlegen
xmin = input("XMIN: ")
xmax = input("XMAX: ")
ymin = input("YMIN: ")
ymax = input("YMAX: ")


#Workspace festlegen
ws = arcpy.env.workspace = r"X:\05_Basisdaten\Rauhigkeiten\Corine2006_V17.gdb"

#Ausgabe Workspace festlegen
outfc = raw_input("Pfad und Name des Ausgabe Shapefiles: ")

#Spatial reference festlegen
sr = arcpy.SpatialReference(25832)

#Liste der RauhigkeitsFeatureClasses
rauhList = ["UTM32_clc06_c111_durchgaengigStaedtischePraegung_140807",
            "UTM32_clc06_c112_nichtdurchgaengigstaedtischePraegung_140807",
            "UTM32_clc06_c121_IndustrieGewerbeflaechen_140807",
            "UTM32_clc06_c122_StrassenEisenbahnnetze_140807",
            "UTM32_clc06_c123_Hafengebiete_140807",
            "UTM32_clc06_c124_Flughaefen_140807",
            "UTM32_clc06_c131_Abbauflaechen_140807",
            "UTM32_clc06_c132_DeponienAbraumhalden_140807",
            "UTM32_clc06_c141_staedtischeGruenflaechen_140807",
            "UTM32_clc06_c142_SportFreizeitanlagen_140807",
            "UTM32_clc06_c211_nichtbewaessertesAckerland_140807",
            "UTM32_clc06_c221_Weinbauflaechen_140807",
            "UTM32_clc06_c222_ObstBeerenobstbestaende_140807",
            "UTM32_clc06_c231_WiesenWeiden_140807",
            "UTM32_clc06_c242_Parzellenstruktur_140807",
            "UTM32_clc06_c243_landwirtschaftlichgenutztnatuerlicheBodenbedeckung_140807",
            "UTM32_clc06_c311_Laubwaelder_140807", "UTM32_clc06_c312_Nadelwaelder_140807",
            "UTM32_clc06_c313_Mischwaelder_140807",
            "UTM32_clc06_c321_NatuerlichesGruenland_140807",
            "UTM32_clc06_c322_HeidenMoorheiden_140807",
            "UTM32_clc06_c324_WaldStrauchUebergangsstadien_140807",
            "UTM32_clc06_c331_StraendeDuenenSandflaechen_140807",
            "UTM32_clc06_c332_Felsflaechen_140807",
            "UTM32_clc06_c333_spaerlicheVegetation_140807",
            "UTM32_clc06_c335_GletscherDauerschneegebiete_140807",
            "UTM32_clc06_c411_Suempfe_140807",
            "UTM32_clc06_c412_Torfmoore_140807",
            "UTM32_clc06_c421_Salzwiesen_140807",
            "UTM32_clc06_c423_Gezeitenzonenflaechen_140807",
            "UTM32_clc06_c511_Gewaesserlaeufe_140807",
            "UTM32_clc06_c512_Wasserflaechen_140807",
            "UTM32_clc06_c521_Lagunen_140807",
            "UTM32_clc06_c522_Muendungsgebiete_140807",
            "UTM32_clc06_c523_MeerOzean_140807"]

#Verarbeitungsausdehnung festlegen
arcpy.env.extent = arcpy.Extent(xmin, ymin, xmax, ymax, "ETRS_1989_UTM_Zone_32N")
#Mergen in aktueller Ausdehnung
arcpy.Merge_management(rauhList, "mergetemp", "")

#FeatureClass und Feature zum Ausschneiden erstellen
arcpy.CreateFeatureclass_management(r"X:\05_Basisdaten\Rauhigkeiten\Corine2006_V17.gdb", "cliptemp", "POLYGON", "", "", "", sr)

#Punkte zu Array
array = arcpy.Array([arcpy.Point(xmin, ymin),
                     arcpy.Point(xmin, ymax),
                     arcpy.Point(xmax, ymax),
                     arcpy.Point(xmax, ymin)])

#Polygon erstellen
clipPoly = arcpy.Polygon(array)

#InsertCursor erstellen
cur = arcpy.da.InsertCursor("cliptemp", ["Shape@"])

#Zeile einfuegen
cur.insertRow([clipPoly])

#Cursor loeschen
del(cur)

#Clippen
arcpy.Clip_analysis("mergetemp", "cliptemp", outfc)
#temporaere Dateien loeschen
arcpy.Delete_management("mergetemp")
arcpy.Delete_management("cliptemp")



