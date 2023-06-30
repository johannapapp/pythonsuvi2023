x = float(input("ütle üks arv"))
if x == round(x):
    print("tegemist on täisarvuga")
    y = x/2
    if y == round(x/2):
        print("tegemist on paarisarvuga")
    elif y != round(x/2):
        print("tegemist on paaritu arvuga")
elif x != round(x):
    print("tegemist on murdarvuga")
    if x > 0:
        print("tegemist on positiivse arvuga")
    elif x < 0:
        print("tegemist on negatiivse arvuga")