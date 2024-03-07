print("This is the fail calculator")
print("It calvulates whether you failed the assignment and gives you the percent")
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
