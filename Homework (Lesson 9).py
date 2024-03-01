"""1. დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
params: [1, 2, 3], ['a', 'b', 'c']  
outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"] """

arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']

print(list(zip(arr1,arr2)))


"""2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), 
თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  
params:[1, 2, 3, 4, 5] 
output: 120 """

from functools import reduce
arr = [1, 2, 3, 4, 5]

try:
    multiply_arr = reduce(lambda x, y: x * y, arr)
    print(multiply_arr)
except Exception as e:
    print(f"Error: {e}")
print("END")


"""3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
params: [1, 2, 3, 4, 5, 6, 7]
outputs: [1, 3, 5, 7] """

arr3 = [1, 2, 3, 4, 5, 6, 7]
odds= list(filter(lambda x: x % 2 != 0, arr3))
print(odds)


"""4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, 
მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), 
თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...
params: ['hello', 'world', 'coding', 'nod'], 'ing'  
outputs: ['coding'] """

string_list = ['hello', 'world', 'coding', 'nod']
substring = 'ing'

try:
    filtered_strings = list(filter(lambda x: substring in x, string_list))
    print(filtered_strings)
except Exception as e:
    print(f"Error: {e}")