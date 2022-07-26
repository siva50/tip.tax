order=int(input("enter cost of the meal:"))
tax=order*0.18
tip=order*0.16
total=order+tax+tip
print("the tax is:",tax)
print("the tip is:",tip)
print("the total is:",total)
print("for the order amount of {} repees,tax is {},and tip is {}, total bill is {}",format(order,tax,tip,total))