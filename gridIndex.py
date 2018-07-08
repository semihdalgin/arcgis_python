#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LerchM
#
# Created:     09.07.2015
# Copyright:   (c) LerchM 2015
# Licence:     PNE Wind internal
#-------------------------------------------------------------------------------

import arcpy, os
from arcpy import env

mxd = arcpy.mapping.MapDocument(r"X:\01_Projekte_Deutschland\PR Nordrhein-Westfalen\Rhein-Sieg-Kreis\150702_Rhein-Sieg-Kreis_tmp.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]


arcpy.env.workspace = r"X:\01_Projekte_Deutschland\PR Nordrhein-Westfalen\Rhein-Sieg-Kreis\01 - Geodatabase\Rhein_Sieg_Kreis.gdb"
arcpy.env.overwriteOutput = True
outFC = "grid_index"
inFC = "Rhein_Sieg_Kreisgrenze_150702"
width = 10000
height = 10000
arcpy.GridIndexFeatures_cartography(outFC, inFC, "INTERSECTFEATURE", "", "", width, height)

