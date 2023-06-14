'''
Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
функционал для изменения и удаления данных'''

import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name,"r") as file:

        data=file.readlines()
        for contact in data:
            print(contact,end="")
    input('\npress any key')


def add_contact(file_name):
    os.system('CLS')
    with open(file_name,"a") as file:
        res=''
        res+=input('Введите фамилию: ')+' '
        res+=input('Введите имя: ')+' '
        res+=input('Введите телефон: ')
        
        file.write(res+'\n')
    input('\npress any key')
    

def search_contact(file_name):
    os.system('CLS')
    target=input('Введите имя для поиска: ')

    
    with open(file_name,'r') as file:
        contacts=file.readlines()
       
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print("Not found!")

    input('\npress any key')

def drawing():
    os.system('CLS')
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - edit contact')
    print('5 - delete contact')
    print('6 - exit')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice=int(input('Input a number: '))

        if user_choice==1:
            show_contacts(file_name)
        elif user_choice==2:
            add_contact(file_name)
        elif user_choice==3:
            search_contact(file_name)
        elif user_choice==4:
            edit_contact(file_name)
        elif user_choice==5:
            delete_contact(file_name)
        elif user_choice==6:
            return
        
def edit_contact(file_name): #c 76 по 87 строку функция delete_contact, далее функция add_contact
    os.system('CLS')
    target=input('Введите имя для изменения: ')
    with open(file_name,'r') as file:
        contacts=file.readlines()
    for contact in contacts:
        if target in contact:
            contacts.pop(contacts.index(contact))
            with open(file_name,"w") as file:
                file.writelines(contacts)
            break
    else:
        print("Not found!")
        input('\npress any key')
        return
    
    res=input('Введите фамилию: ')+' '
    res+=input('Введите имя: ')+' '
    res+=input('Введите телефон: ')
    with open(file_name,"a") as file:    
        file.write(res+'\n')
    input('\npress any key')


def delete_contact(file_name):  # основана на функции search_contact
    os.system('CLS')
    target=input('Введите имя для удаления: ')

    
    with open(file_name,'r') as file:
        contacts=file.readlines()
       
    for contact in contacts:
        if target in contact:
            contacts.pop(contacts.index(contact))
            with open(file_name,"w") as file:
                file.writelines(contacts)
            break
    else:
        print("Not found!")

    input('\npress any key')

main("python_seminars/test.txt")