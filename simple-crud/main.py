def read_file():
    file = open('data.txt', 'r')
    data = [i.split(',') for i in file.readlines()]
    file.close()
    return data


def menu() -> int:
    try:
        print('=================================================================')
        print('STUDENT\'S DATABASE')
        print("""
 1: Add new data
 2: Search data
 3: Edit existing data
 4: Delete existing data
-1: Quit""")
        return int(input('Your chocie : '))
    except Exception as e:
        print('Invalid input')


def add(name: str, grade, age):
    if name.upper() not in [i[0] for i in read_file()]:
        file = open('data.txt', 'a')
        file.writelines(f'{name.upper()},{grade},{age}\n')
        file.close()
        return 'Data added successfully'
    else:
        return 'Data is already exist, please try editing data instead'


def search(name: str):
    r = read_file()
    for data in r:
        if data[0] == name.upper():
            return f"""Data found
Name  : {name.upper()}
Grade : {data[1]}
Age   : {data[2]}"""
    return "Data not found"


def edit(name: str):
    datas = read_file()
    for data in datas:
        if data[0] == name.upper():
            try:
                key = input('Data to edit(name, grade, age) : ').lower()
                if key == 'name':
                    new_name = input('New name : ').upper()
                    if new_name.isalpha():
                        datas[datas.index(data)][0] = new_name
                    else:
                        return 'Invalid name'
                elif key == 'grade':
                    new_grade = int(input('New grade : ').upper())
                    datas[datas.index(data)][1] = new_grade
                elif key == 'age':
                    new_age = int(input('New age : ').upper())
                    datas[datas.index(data)][2] = new_age + '\n'
            except Exception as e:
                print('Invalid input')
            file = open('data.txt', 'w')
            file.writelines(','.join(i) for i in datas)
            file.close()
            return 'Data edited'
    return 'Data not found'


def delete(name: str):
    datas = read_file()
    for data in datas:
        if data[0] == name.upper():
            del datas[datas.index(data)]
            file = open('data.txt', 'w')
            file.writelines(','.join(i) for i in datas)
            file.close()
            return 'Data deleted'
    return 'Data not found'


run = True
while run:
    choice = menu()

    if choice == -1:
        run = False

    if choice == 1:
        print('\nAdd new data')
        try:
            print(add(input('Student\'s name : '), int(input('Student\'s grade: ')), int(input('Student\'s age  : '))))
        except Exception as e:
            print('Invalid input')
    elif choice == 2:
        print('\nSearch data')
        print(search(input("Student\'s name : ")))
    elif choice == 3:
        print('\nEdit data')
        print(edit(input('Student\'s name : ')))
    elif choice == 4:
        print('\nDelete data')
        print(delete(input('Student\'s name : ')))
