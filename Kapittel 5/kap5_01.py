
scifi_vestlige = ["Isaac Asimov", "Arthr C. Clarke",
                  "Orson S. Card", "Neil Stephenson", "Ray Bradbury"]
scifi_asiatiske = ["Cixin Liu", "Ken Liu", "Ma Boyong",
                   "Tang Fei", "Chen Qiufan"]

kombinert = scifi_vestlige + scifi_asiatiske

del kombinert[0]
del kombinert[2]

indeks = kombinert.index("Cixin Liu")

ny = kombinert[1:4]

del kombinert[ kombinert.index("Ma Boyong") ]

kombinert.reverse()