print("This is the grade calculator")
print("It calvulates your letter grade and gives you the percent")
xx=float(input("Total number of points possibble"))
yy=float(input("How many points you got"))
#x= float(xx)
#y= float (yy)
zz= float(yy/xx)
print(zz*100)
z= float(zz*100)
if (z<60):
    print("You failed")
else:
    print("You passed")
if (z>=90):
    print("A")
elif (z>=80):
    print("B")
elif (z>=70):
    print("C")
elif (z>=60):
    print("D")
else:
    print("F")
