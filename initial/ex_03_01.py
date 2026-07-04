hrs = input("Enter Hours: ")
h = float(hrs)
pay_rate = input ("Enter Pay Rate: ")
pr = float(pay_rate)

if h <= 40: 
    pay = h * pr
    
else: 
    pay = 40 * pr + (h-40) * pr * 1.5


print("Pay: ",pay )