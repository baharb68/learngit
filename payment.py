DailyPayment = 50500
salary=0
for i in range(12):
    i=i+1
    if (i % 2) != 0:
        off=2
    else:
        off=3
    if i<=6:
        salary=(31*DailyPayment)-(off*DailyPayment)
    elif i<=11:
        salary=(30*DailyPayment)-(off*DailyPayment)
    else:
        salary=(29*DailyPayment)-(off*DailyPayment)
    print("month",i,":",salary)
