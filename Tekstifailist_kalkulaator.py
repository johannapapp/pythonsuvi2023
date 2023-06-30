ava = open("Kalkulaatoryl_fail")
rida1 = ava.readline().strip()
arv1 = int(ava.readline())
arv2 = int(ava.readline())
if rida1 == "liitmine":
    print(arv1+arv2)
elif rida1 == "lahutamine":
    print(arv1-arv2)
elif rida1 == "korrutamine":
    print(arv1*arv2)
elif rida1 == "jagamine":
    print(arv1/arv2)
ava.close()

