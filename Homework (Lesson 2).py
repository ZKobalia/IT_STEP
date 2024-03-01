"""1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს შორის შესრულებული 
არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება)."""

x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y} = {x % y}")
print(f"{x} ** {y} = {x ** y}")


"""2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე."""

p = eval(input("Enter first diagonal length: "))
q = eval(input("Enter second diagonal length: "))

print(f"Area of Rhombus is: {p} * {q} / 2 = {p * q / 2}")


"""3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში."""

z = eval(input("Enter the value in meters: "))

# print(f"{z} meters is {z * 100} centimeters")
# print(f"{z} meters is {z * 10} decimeters")
# print(f"{z} meters is {z * 1000} millimeters")
# print(f"{z} meters is {z / 1609} miles")

print(f"{z} meters is: \n {z * 100} centimeters \n {z * 10} decimeters \n {z * 1000} millimeters \n {z / 1609} miles")

"""4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა 
და ფუძის მნიშვნელობა."""

h = eval(input("Enter triangle height length: "))
b = eval(input("Enter triangle base length: "))

print(f"Area of Triangle is: {h} * {b} / 2 = {h * b / 2}")