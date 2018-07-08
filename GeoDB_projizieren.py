#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LerchM
#
# Created:     04.05.2015
# Copyright:   (c) LerchM 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
arcpy.SetProduct("ArcView")
ws = arcpy.env.workspace = r"X:\05_Basisdaten\Rauhigkeiten\Corine2006_V17.gdb"
featureclasses = arcpy.ListFeatureClasses()
outCS = arcpy.SpatialReference('ETRS 1989 UTM Zone 32N')
for fc in featureclasses:
    #print fc, fc+"UTM32"

    arcpy.Project_management(fc, "UTM32_"+fc, outCS)
