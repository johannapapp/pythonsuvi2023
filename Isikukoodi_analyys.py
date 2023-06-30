x = input("mis on su isikukood")
if x[0:1] == "2" or x[0:1] == "4" or x[0:1] == "6" or x[0:1] == "8":
    print("sugu on naine")
else:
    print("sugu on mees")
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
b = y + z + n
if x[3:5] == "01":
    m == "jaanuar"
elif x[3:5] == "02":
    m = "veebruar"
elif x[3:5] == "03":
    m = "märts"
elif x[3:5] == "04":
    m = "aprill"
elif x[3:5] == "05":
    m  = "mai"
elif x[3:5] == "06":
    m = "juuni"
elif x[3:5] == "07":
    m = "juuli"
elif x[3:5] == "08":
    m = "august"
elif x[3:5] == "09":
    m = "september"
elif x[3:5] == "10":
    m = "oktoober"
elif x[3:5] == "11":
    m = "november"
elif x[3:5] == "12":
    m = "detsember"
print("sünnikuupäev on " + x[5:7] +"." + m + " " + b)