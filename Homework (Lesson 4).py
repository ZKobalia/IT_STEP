"""1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს."""

n = int(input("Enter Number: "))
total_sum = sum(range(1, n))  # თუ პირობა მოიაზრებს, რომ "n"-ის ჩათვლით ჯამი გვინდა, მაშინ გვექნება range(1,n+1).
print(f"The sum of numbers from 1 to {n} is: {total_sum}")


"""2. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად 
დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1"""

n2 = int(input("Enter Number: "))
while n2 > 0:
    print(n2)
    n2 -= 1


"""3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი. 
როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას."""

from random import randint
num = randint(1,100)

print("Guess the Number From 1 to 100!\n")

while True:
    guess = int(input("Your Guess: "))

    if num == guess:
        print(f"C o n g r a t u l a t i o n s !!!\nYou Won! It was: {num}\n")
        break
    elif guess > num:
        print("Too Great")
    else:
        print("Too Less")   
print("Game Over!")


"""4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, 
შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს პროცესი გაგრძელდეს იქამდე 
სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი."""

total_sum = 0

while True:
    num4 = input("Enter Positive Number: ")

    if num4.lower() == "sum":
        print(f"The sum of the positive numbers is: {total_sum}\n")
        break
    elif num4.isdigit() and int(num4) > 0:
        total_sum += int(num4)

# ეს დავალება თუ ძალიან ჩავხლართე და არსებობს უფრო მარტივი მეთოდი, გთხოვთ გამიზიაროთ.