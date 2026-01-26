# number = 15
# print(type(number))

# print('SMART SPLIT CALCULATOR')

# name=input('Name:')
# ammount=float(input('Bill ammount:'))
# tip=float(input('Tip Percentage?:'))
# people=int(input('How many people?:'))

# total_tip=tip/100*ammount
# total_bill=ammount+total_tip
# people_pay=total_bill/people

# people_pay=round(people_pay,2)
# total_bill=round(total_bill,2)

# print(f'Hello {name}!')
# print(f'Your name starts with:{name[0]}')
# print(f'Bill: $ {ammount}')
# print(f'Tip: ${total_tip}')
# print(f'Total Bill: ${total_bill}')
# print(f'Each person should pay: ${people_pay}')

#exercise 1

# num=int(input("Number: "))
# if num % 2 == 0:
#     print('Even woww')
# else:
#     print('aww odd')
    
# #Exercise 2

# weight=float(input('What is your weight: '))
# height=float(input('what is your height?: '))

# BMI= weight/(height*height)

# if BMI < 18.5:
#     print('Underweight')
# elif BMI <25:
#     print('Noramal')
# elif BMI <30:
#     print('Overwieght')
# else:
#     print('Obese')
    
#Exercise 3

# age = int(input('Age:'))
# Student=input('Student?:')

# if Student == 'yes':
#     print('get 2$ discount')
#     if age < 12:
#      print('Price: $13')
#     elif age < 60:
#         print('Price: $8')
#     elif age > 60:
#         print('Price: $4')
# elif Student == 'no':
#     if age < 12:
#      print('Price: $15')
#     elif age < 60:
#         print('Price: $10')
#     elif age > 60:
#         print('Price: $6')

#exercise 3 corrected
age = int(input('Age:'))
Student=input('Student?:').lower()

if age < 12:
    price = 15
elif age< 60:
    price = 10
else:
    price = 6
    
if Student == 'yes':
    price -= 2
    
print(f'{price}')