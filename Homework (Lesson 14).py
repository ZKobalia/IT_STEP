"""
chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

1. დაწერეთ პითონის ფუნქცია, რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.
2. დაწერეთ პითონის ფუნქცია, რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.
3. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.
4. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს
[
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია
"""

import json

def create_jason_file(path, file_name):
    file_path = f"{path}/{file_name}.jason"
    try:
      file = open(file_path, mode= 'x', encoding= 'utf-8')
      file.close()
    except FileExistsError:
       print(f"File {file_name} Exists in {path}!")
       print("Keep Working!" + "\n")
    return file_path

def insert_data_into_Jason_file(path, data):  
    with open(path, mode= 'w', encoding= 'utf-8') as file:
       file.write(json.dumps(data))

def read_json_file(path):
   with open(path, mode= 'r', encoding= 'utf-8') as file:
      return json.loads(file.read())
   
def update_json_file (path, data):
   chess_players = read_json_file(path)
   chess_players.extend(data)
   insert_data_into_Jason_file(path,chess_players)
    

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

chess_players_2 = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

file_path = create_jason_file("d:/Python ZK/საშინაო დავალება", "Homework (Lesson 14)")

insert_data_into_Jason_file(file_path, chess_players)
file_content = read_json_file(file_path)
print(file_content)

file_content = file_content[:2]
insert_data_into_Jason_file(file_path,file_content)
print(file_content)

update_json_file(file_path, chess_players_2)
file_content = read_json_file(file_path)
print(file_content)

for content in file_content:
   if 'country' in content and 'Georgia' in content['country']:
      content['rating'] = 3000

insert_data_into_Jason_file(file_path, file_content)

for content in file_content:
   print(content)