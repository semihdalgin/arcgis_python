#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LerchM
#
# Created:     06.08.2015
# Copyright:   (c) LerchM 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, re, arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

liste1 = os.listdir(r"X:\09_Python_Skripte\Kachelausgabe")
liste2 = []
print liste1

for item in liste1:
    if re.search(r".png", item):
        liste2.append(item)

liste1 = liste2
del liste2

print ("neu")
print liste1

for item in liste1:
    a = MLClassify(str(item), r"X:\09_Python_Skripte\bebauung.gsg", "","","","")



