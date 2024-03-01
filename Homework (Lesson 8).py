"""1. შექმენით გლობალური ცვლადი `int_list = [10,20,30,40]` და დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად 
და გლობალურ `int_list` სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს."""

def add_number (a):
    global int_list
    int_list.append(a)

int_list = [10,20,30,40]
print(int_list)

add_number(7)
print(int_list)


"""2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. 
პარამეტრად უნდა მიიღოს შემდეგი სია `[100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]`."""

arr = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def sum_func ():
    list_sum = sum(arr)
    print (list_sum)

sum_func ()


"""3. შექმენით გლობალური ცვლადი `gl_str = "Global"` და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით 
რაც გლობალურ ცვლადს აქვს  `(gl_str)` და აბრუნებს ლოკალური ცვლადის მნიშვნელობას"""

def new_str():
    gl_str = "Local"
    print(gl_str)

gl_str = "Global"

new_str()


"""4. რეკურსიის გამოყენებით  დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს `number` და დააბრუნებს  ციფრების ჯამს 
(მაგალითად თუ ფუნქციამ მიიღო რიცხვი `12345`, უნდა დააბრუნოს `15`. რადგან `1+2+3+4+5`  უდრის `15`-ს)."""

def sum_of_digits(number):
    if number < 10:
        return number
    
    return number % 10 + sum_of_digits(number // 10)

number = 12345
result = sum_of_digits(number)
print("Sum of digits in", number, "=", result)


"""5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს 
(მაგალითად  `input: Hello   Output: olleH`)"""

def revers_str(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + revers_str(s[:-1])

string = "Hello"
result = revers_str(string)
print(f"Original String is: {string}. Reversed String is: {result}.")