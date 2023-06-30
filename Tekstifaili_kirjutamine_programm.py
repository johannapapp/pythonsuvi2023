x = input("mis on su isikukood")
if x[0:1] == "2" or x[0:1] == "4" or x[0:1] == "6" or x[0:1] == "8":
    sugu = "naine"
else:
    sugu = "mees"
if x[0:1] == "1" or x[0:1] == "2":
    y = "18"
elif x[0:1] == "3" or x[0:1] == "4":
    y = "19"
elif x[0:1] == "5" or x[0:1] == "6":
    y ="20"
elif x[0:1] == "7" or x[0:1] == "8":
    y = "21"
z = x[1:2]
n = x[2:3]
synniaasta = y + z + n
if x[3:5] == "01":
    kuu = "jaanuar"
elif x[3:5] == "02":
    kuu = "veebruar"
elif x[3:5] == "03":
    kuu = "märts"
elif x[3:5] == "04":
    kuu = "aprill"
elif x[3:5] == "05":
    kuu = "mai"
elif x[3:5] == "06":
    kuu = "juuni"
elif x[3:5] == "07":
    kuu = "juuli"
elif x[3:5] == "08":
    kuu = "august"
elif x[3:5] == "09":
    kuu = "september"
elif x[3:5] == "10":
    kuu = "oktoober"
elif x[3:5] == "11":
    kuu = "november"
elif x[3:5] == "12":
    kuu = "detsember"
kuupäev = x[5:7]
ava = open("tekstikirjutamine","w")
ava.write("sugu: " + sugu +"\n")
ava.write("sünnipäev: " + kuupäev + "." + kuu + " " + synniaasta)
ava.close()
