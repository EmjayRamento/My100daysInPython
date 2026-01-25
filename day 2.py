#Exercise 1 from day 1

# print ('Welcome to Day 1 of Python!\n Lets start coding.')

# #Exercise 2

# name = input('Name:')
# prog = input('what is your favorite programming language?:')

# print('Hello '+ name + ' You love '+ prog)

# #Exercise 3

# a = input('a: ') 
# b = input('b: ') 

# b1 = a
# a = b 

# print('a =', a)
# print('b =', b1)

#Extra Exercise

# print('Welcome to Band Registration!\n')
# rock = input('what is your favorite rock?:')
# color = input ('what iss your favorite color:?')

# print('Your band name is:'+ rock  + color)

# age = 25
# name = "Alex"
# age1 = str(age)
# #pag + strings lang pwede then , pag int
# print('Age:' + age1)

# word = "Python"
# print(word[-7])

#Mini exercise for Dy 2

# num1 = input('number 1:')
# num2= input('number 2:')

# number1 = int(num1)
# number2 = int(num2)
# sum= number1 + number2
# print(sum)

# #Exercise 2
# name = input('name:')
# age = input('age:')

# print(f'My name is {name} and I am {age} years old')

# #Exercise 3
# word= input('Your fav word:')

# print(word[0])
# print(word[-1])
# print(word*3)

#Tip Calculator
print('WELCOME TO TIP CALCULATOR!')
bill = float(input('What is the total bill amount?\n$:'))
tip = float(input('How much tip would you like to give?\npercent:'))
people= int(input('How many people to split the bill?\nPeople:'))

# bill1= float(bill)
# tip1= float(tip)
# people= int(people)
# per = bill1/tip1*100
# per1 = per*100
decimal= tip/100
total_bill = bill + (bill * decimal)
pay= total_bill/people

pay=round(pay,2)
#sa lst idevide kung ilan sila
print('Each person should pay:', pay)