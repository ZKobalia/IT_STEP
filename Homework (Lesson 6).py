"""1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; 
თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:
a - append
r - remove
e - exit
მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება."""

my_list = []

while True:
    ask = input ("Enter 'a' or 'r' for append or remove number (with space), 'e' for exit: ").split()
    
    if ask[0] == "a":
        number = eval(ask[1])
        my_list.append(number)
        print(my_list)

    elif ask[0] == "r":
        number = eval(ask[1])
        if number in my_list:
            my_list.remove(number)
        else:
            print(f"{number} not in {my_list}")
        print(my_list)

    elif ask[0] == "e":
        print(my_list)
        break

"""2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას `my_list = [43, '22', 12, 66, 210, ["hi"]`, და შეასრულებს შემდეგ ნაბიჯებს:
a. დაბეჭდავს `210`-ის ინდექსს;
b. დაამატებს ბოლო ელემენტში ტექსტს `"hello"`;
c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
d. შექმენით ახალი სია `my_llist_2`, რომელსაც ექნება `my_llist`-ის მნიშვნელობა, გაასუფთავეთ `my_llist_2`-ის მნიშნველობა და დაბეჭდეთ ორივე სია."""

my_list = [43, '22', 12, 66, 210, ["hi"]]

"a"
print(my_list.index(210))

"b"
my_list.append("hello")

"c"
my_list.pop(2)
print(my_list)

"d"
my_list_2 = my_list.copy()
my_list_2.clear()

print(my_list)
print(my_list_2)

"""3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა  "(123) 456-789" ფორმატს, 
თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი."""

import re
pnumber = input("Enter phone number: ")
pattern = r"\([0-9]{3}\)\s[0-9]{3}-[0-9]{3}"

if (re.match(pattern, pnumber)) is None:
    print("Invalid Format")
else:
    print("Phone number is: ", pnumber)