DailyPayment = 505000
salary=0
kabiseyear=1398
currentyear=1402
currentmonth=4
off=[1,2,3,0,2,4,2,1,2,3,0,2]
count=0

if currentmonth<=6:
    day=31
elif currentmonth<=11:
    day=30
else:
    if (currentyear-kabiseyear)%4 == 0:
        day=30
    else:
        day=29
for i in range(day):
    if (i+1)%7 !=0:
        count=count+1
salary=(count*DailyPayment)-(off[currentmonth-1]*DailyPayment)
print(currentmonth,":",salary)

