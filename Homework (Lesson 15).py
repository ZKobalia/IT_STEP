"""
შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

id,name,age,grade,subject_name,marks
1,string,0,string,string,0
2,string,0,string,string,0

1. დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას `(id,name,age,grade,subject_name,marks)` და თქვენ სტუდენტს დაამატებთ csv ფაილში.
2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული  სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
3. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს 
და განახლებულ ქულას.
"""

import os, csv

def create_csv_file(path, csv_file):
    try:
        os.makedirs(path, exist_ok=True)
    except FileExistsError:
        pass

    file_path = os.path.join(path, f"{csv_file}.csv")

    try:
        with open(file_path, mode='x', encoding='utf-8', newline='') as file:
            pass
    except FileExistsError:
        print(f"File '{file_path}' exists! Keep Going! \n")

    return file_path


def  create_csv_data():
    data = ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
    id = 1

    while True:
        name = input("Name [ENTER -- exit]: ")

        if not name:
            print()
            break
        
        age = int(eval(input("Age: ")))
        grade = input("Grade: ")
        subject_name = ("Subject: ")
        marks = int(eval(input("Mark: ")))

        data.append([id, name, age, grade, subject_name, marks])

        id += 1
        print(data)

    return data

def write_data_into_csv_file(path, csv_data):
    with open(path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, dialect='my_dialect')
        writer.writerows(csv_data)

def read_data(path,student_name=''):
    with open(path, mode='r', encoding='utf-8') as file:
        reader = list(csv.reader(file, delimiter='|'))

        if not student_name:
            return reader
        
        st_row = ['id', 'name', 'age', 'grade', 'subject_name', 'marks']

        for row in reader:
            if row[1] == student_name:
                st_row.append(row)

        return st_row
    
def append_data(path, row_data):
    data = read_data(path)
    row_data.insert(0, int(data[-1][0])+1)

    with open(path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, dialect='my_dialect')
        writer.writerow(row_data)

def update_data(path, id, subject_name, mark):
    data = read_data(path)

    for row in data[1:]:
        if int(row[0]) == id and row[4] == subject_name:
            row[3] = mark
            break
    else:
        print("Can't update")

    write_data_into_csv_file(path, data)
    


path = 'Hw 15'
file_name = 'Hw (Lesson 15)'

file_path = create_csv_file(path,file_name)

csv.register_dialect ('my_dialect', delimiter= '|', quoting= csv.QUOTE_NONNUMERIC)

data = create_csv_data()
print(data)

write_data_into_csv_file(file_path,data)

file_content = read_data(file_path, 'Tim')
print(file_content)

row_data = ['Magnus', 26, 'B', 'Math', 82]
append_data(file_path, row_data)

id = 11
subject_name = 'Math'
mark = 100
update_data(file_path, id, subject_name, mark)