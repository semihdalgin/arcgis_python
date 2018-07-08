arazi="C:\\New folder\\sem.gdb\\sem"
features = arcpy.UpdateCursor(arazi)
for feature in features:
	if feature.MES_TIP=="Bk":
		feature.ana_sinif="6_Bataklık"
		features.updateRow(feature)
	if feature.MES_TIP=="Bk-1":
		feature.ana_sinif="6_Bataklık"
		features.updateRow(feature)
	if feature.MES_TIP=="Bk-2":
		feature.ana_sinif="6_Bataklık"
		features.updateRow(feature)
	if feature.MES_TIP=="Bk-3":
		feature.ana_sinif="6_Bataklık"
		features.updateRow(feature)
	if feature.MES_TIP=="Dp":
		feature.ana_sinif="6_Depo_Orman"
		features.updateRow(feature)
	if feature.MES_TIP=="E":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="E-1":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="E-2":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="E-3":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="F":
		feature.ana_sinif="6_Orman_Fidanlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Fd":
		feature.ana_sinif="6_Orman_Fidanlık"
		features.updateRow(feature)
	if feature.MES_TIP=="GÖ":
		feature.ana_sinif="6_Göl"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-1":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-10":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-11":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-12":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-13":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-14":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-15":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-2":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-3":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-4":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-5":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-6":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-7":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-8":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Ku-9":
		feature.ana_sinif="6_Kumsal_Alanlar"
		features.updateRow(feature)
	if feature.MES_TIP=="Md.Oc":
		feature.ana_sinif="6_Orman"
		features.updateRow(feature)
	if feature.MES_TIP=="Me":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-10":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-11":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-12":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-13":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-14":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-15":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-16":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-17":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-18":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-19":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-3":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-33":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-4":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-5":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-6":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-7":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-8":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-9":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Me-T":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="Mv":
		feature.ana_sinif="6_Meyvelik"
		features.updateRow(feature)
	if feature.MES_TIP=="Mv-1":
		feature.ana_sinif="6_Meyvelik"
		features.updateRow(feature)
	if feature.MES_TIP=="Mv-2":
		feature.ana_sinif="6_Meyvelik"
		features.updateRow(feature)
	if feature.MES_TIP=="Mz":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Mz-1":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Mz-2":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Mzl":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Mzl-1":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Mzl-2":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="Mzl-3":
		feature.ana_sinif="6_Mezarlık"
		features.updateRow(feature)
	if feature.MES_TIP=="OE":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="OE-1":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="OE-2":
		feature.ana_sinif="6_Erozyon"
		features.updateRow(feature)
	if feature.MES_TIP=="OT":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT OT-T T Me Z İs S":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT+Me":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT+Me-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT+Me-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT+Me-3":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-10":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-11":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-12":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-13":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-14":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-15":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-16":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-17":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-18":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-19":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-20":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-21":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-22":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-23":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-24":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-25":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-26":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-27":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-28":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-29":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-3":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-30":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-31":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-32":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-33":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-34":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-35":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-36":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-37":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-4":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-5":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-6":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-7":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-8":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-9":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-10":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-11":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-12":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-13":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-14":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-3":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-4":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-5":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-6":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-7":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-8":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-E-9":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-OE":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-OE-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-OE-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-OE-Z-İs-T":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-10":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-3":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-4":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-5":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-6":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-7":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-8":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-9":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-T-Z":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-1":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-2":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-3":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-4":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-5":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-6":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-7":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-8":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-9":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OT-Z-T":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="OY":
		feature.ana_sinif="6_Yol"
		features.updateRow(feature)
	if feature.MES_TIP=="OY-1":
		feature.ana_sinif="6_Yol"
		features.updateRow(feature)
	if feature.MES_TIP=="OY-2":
		feature.ana_sinif="6_Yol"
		features.updateRow(feature)
	if feature.MES_TIP=="OY-3":
		feature.ana_sinif="6_Yol"
		features.updateRow(feature)
	if feature.MES_TIP=="Oc":
		feature.ana_sinif="6_Maden"
		features.updateRow(feature)
	if feature.MES_TIP=="Oc-1":
		feature.ana_sinif="6_Maden"
		features.updateRow(feature)
	if feature.MES_TIP=="Oc-2":
		feature.ana_sinif="6_Maden"
		features.updateRow(feature)
	if feature.MES_TIP=="Oc-3":
		feature.ana_sinif="6_Maden"
		features.updateRow(feature)
	if feature.MES_TIP=="PLANDIŞI":
		feature.ana_sinif="6_Plandısı"
		features.updateRow(feature)
	if feature.MES_TIP=="Su":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="Su-1":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="Su-2":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="Su-3":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="Su-4":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="Su-5":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="Su-6":
		feature.ana_sinif="6_Sulak_Alan"
		features.updateRow(feature)
	if feature.MES_TIP=="T":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T+Me":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="T+Me-1":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="T+Me-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="T-1":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-10":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-11":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-12":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-13":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-14":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-15":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-16":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-17":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-18":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-19":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-2":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-3":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-4":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-5":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-6":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-7":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-8":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-9":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-OE":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-OT":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-OT-1":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="T-OT-2":
		feature.ana_sinif="6_Kayalık_Taslık"
		features.updateRow(feature)
	if feature.MES_TIP=="Ts":
		feature.ana_sinif="6_Diger_Tesisler"
		features.updateRow(feature)
	if feature.MES_TIP=="Ts-1":
		feature.ana_sinif="6_Diger_Tesisler"
		features.updateRow(feature)
	if feature.MES_TIP=="Ts-2":
		feature.ana_sinif="6_Diger_Tesisler"
		features.updateRow(feature)
	if feature.MES_TIP=="Ts-3":
		feature.ana_sinif="6_Diger_Tesisler"
		features.updateRow(feature)
	if feature.MES_TIP=="Ts-4":
		feature.ana_sinif="6_Diger_Tesisler"
		features.updateRow(feature)
	if feature.MES_TIP=="Ts-5":
		feature.ana_sinif="6_Diger_Tesisler"
		features.updateRow(feature)
	if feature.MES_TIP=="Z":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-1":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-10":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-11":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-12":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-13":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-14":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-15":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-16":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-17":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-18":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-19":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-2":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-20":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-21":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-22":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-23":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-24":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-25":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-26":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-27":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-28":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-29":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-3":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-30":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-31":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-32":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-33":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-34":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-35":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-36":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-37":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-38":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-39":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-4":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-40":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-41":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-42":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-43":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-44":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-45":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-46":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-47":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-48":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-49":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-5":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-50":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-51":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-52":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-53":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-54":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-55":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-56":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-57":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-58":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-6":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-7":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-8":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-9":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-BBt":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-BBt-1":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-BBt-2":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-1":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-10":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-11":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-2":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-3":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-4":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-5":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-6":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-7":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-8":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-OT-9":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-İs":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-İs-1":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-İs-2":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="Z-İs-3":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="ZA":
		feature.ana_sinif="6_Ziraat_Alanları"
		features.updateRow(feature)
	if feature.MES_TIP=="ot-2":
		feature.ana_sinif="6_Mera"
		features.updateRow(feature)
	if feature.MES_TIP=="İs":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-1":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-10":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-11":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-12":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-13":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-14":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-15":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-16":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-17":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-18":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-19":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-2":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-20":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-21":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-22":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-23":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-24":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-25":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-26":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-27":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-28":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-29":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-3":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-30":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-31":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-32":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-33":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-34":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-35":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-36":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-37":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-38":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-39":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-4":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-40":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-41":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-42":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-43":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-44":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-45":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-46":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-47":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-48":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-49":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-5":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-50":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-51":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-6":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-7":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-8":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
	if feature.MES_TIP=="İs-9":
		feature.ana_sinif="6_Yerlesim"
		features.updateRow(feature)
