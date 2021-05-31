def people(age):
    
    if age < 10:
        print("Children")
    if age > 60:
        print("Senior citizen")
    if (age>10 and age<60):
        print("Normal citizen")
    people(8)
    people(70)
    people(30)


def train(age):
    ticket_cost=100
    
    if (age>=60):
        print("Male train ticket price is" +" "+ str(ticket_cost * 0.30))
        print("Female train ticket price is" + str(ticket_cost * 0.50))
    else:
        print("Male train ticket price is" +" "+ str(ticket_cost * 1))
        print("Female train ticket price is" +" " + str(ticket_cost * 0.30))
train(50)
train(65)



def check(num):
    
    if (num<0):
        print("its not positive")
    else:
        print("its a positive")
    if (num%5==0):
        print("its divisible by 5")
    else:
        print("its not divisible 5")
check(-5)
check(5)
