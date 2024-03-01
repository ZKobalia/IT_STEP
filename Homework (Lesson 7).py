"""1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას."""

def generate_fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n + 1:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        count += 1

n = 8
generate_fibonacci(n)


"""2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები. (ანაგრამი არის სიტყვა ან შესიტყვება, 
რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: `race` და `care` ანაგრამებია."""

def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        print(f"'{str1}' and '{str2}' are anagrams!")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams!")

str1 = "ani"
str2 = "INA"
check_anagrams(str1,str2)


"""3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს."""

def factorial(n):
    if n < 0:
        print("Enter positive number!")
    elif n == 0:
        print(1)
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        print(result)

n = 8
factorial(n)


"""4. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში 
რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა."""

def count_symbol (string, symbol):
    count = 0
    for i in string:
        if i == symbol:
            count += 1
    print(count)

string = "Python is funny!"
symbol = "n"
count_symbol (string, symbol)