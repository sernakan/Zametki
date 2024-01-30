import json
from datetime import datetime
ind = []
z = "Zametka.json"
def write_json(new_data, filename='Zametka.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
for i in range(1,10):
    ind.append(i)
def CreateZametka():
    b = ""
    y= datetime.now()
    b = y.strftime("%m") +"/"+  y.strftime("%d") +"/"+  y.strftime("%Y")  +" "+ y.strftime("%H") +":"+ y.strftime("%M") +":"+ y.strftime("%S")
    y = y.isoformat()
    Zagolovok = input("Введите заголовок - ")
    Zametka = input("Введите тело заметки - ")
    for i in range(11):
        a = {"name": Zagolovok,
         "body": Zametka,
         "date": b,
         "Index": i}
        write_json(a)
def delete():
    a = int(input("Какую заметку вы хотите удалить? - "))
    obj = json.load(open("Zametka.json"))   
    for i in range(11):
        if obj[i]["Index"] == a:
            obj.pop(i)
            print("Сделано")
            break

        print("Нет такой заметки")
            
    open("Zametka.json", "w").write(
    json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )
    


def SpisokZametok():
    y = json.load(open("Zametka.json"))
    for i in range(len(y)):
        print(y[i])

def Izmena():
    a = int(input("Какую заметку вы хотите изменить? - "))
    file_path = "Zametka.json"
    with open(file_path, 'r', encoding='utf-8') as json_file:
        list = json.load(json_file)
    c = input("На какой текст вы бы хотели поменять записку? - ")
    list[a]["body"] = c
    y= datetime.now()
    b = y.strftime("%m") +"/"+  y.strftime("%d") +"/"+  y.strftime("%Y")+" "+ y.strftime("%H") +":"+ y.strftime("%M") +":"+ y.strftime("%S")
    list[a]["date"] = b
    
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(list, json_file)
    print("Успешно изменено")
while True:
    input1 = input("Что вы хотите сделать? (Создать заметку - create; Удалить заметку - del; Список заметок - list; Изменить заметку - change; Выйти - exit) - ")
    input1.lower()
    if input1 == "create":
        CreateZametka()
    elif input1 == "del":
        delete()
    elif input1 == "list":
        SpisokZametok()
    elif input1 == "change":
        Izmena()
    elif input1 =="exit":
        quit()
    else:
        print("Вы ввели неправльную функцию.")