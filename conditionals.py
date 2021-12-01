try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    if hours <= 40:
        pay = hours*rate
    else:
        pay = (40*rate) + ((hours-40)*(rate*1.5))
    print(pay)   
except:
    print('Error, please enter numeric input')

# if hours <= 40:
#     pay = hours*rate
# else:
#     pay = (40*rate) + ((hours-40)*(rate*1.5))
# print(pay) 
    