# Author:zqbin
# @Time:2023/9/15 14:37
# @Author:14988
# @Site:
# @File:04_信息系统.py
# @Software:PyCharm


"""
函数演练: 学生信息管理系统
学生的信息包含: id(str, 唯一), name(str), phone(str)
系统具备的功能:
    1. 添加学生信息
    2. 修改学生信息(通过id选择学生进行修改)
    3. 删除学生信息(通过id删除)
    4. 通过id查询学生信息
    5. 查询所有学生信息
    6. 退出
"""

import os.path
import json

path = './studentInfo.json'
studentInfo = []


def getJson():
    global studentInfo
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write('[]')

    with open(path, 'r', encoding='utf-8') as f:
        studentInfo = json.load(f)


def print_info():
    info = """
    ============ 学生信息管理系统 ============
        1. 添加学生信息
        2. 修改学生信息(通过id选择学生进行修改)
        3. 删除学生信息(通过id删除)
        4. 通过id查询学生信息  
        5. 查询所有学生信息
        6. 退出
    ========================================
    """
    print(info)


def main():
    getJson()
    while 1:
        print_info()
        userInput = input("\t请输入您要进行的操作: ")
        if userInput == '1':
            addUser()
        elif userInput == '2':
            updateUser()
        elif userInput == '3':
            deleteUser()
        elif userInput == '4':
            showOne()
        elif userInput == '5':
            showAll()
        elif userInput == '6':
            exit()
        else:
            print("\t输入有误, 请重新输入")


def addUser():
    while True:
        id = input('请输入id：')
        isRepeat = False
        if id == '':
            print('id有误，请重新输入！')
            continue
        for item in studentInfo:
            if item.get('id') == id:
                print('id重复，请重新输入！')
                isRepeat = True
                break
        if isRepeat:
            continue

        name = input('请输入name：')
        if name == '':
            print('name有误，请重新输入！')
            continue

        phone = input('请输入phone：')
        if phone == '':
            print('phone有误，请重新输入！')
            continue

        studentInfo.append({'id': id, 'name': name, 'phone': phone})
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(studentInfo, f, ensure_ascii=False, indent=4)
            print('添加学生信息成功')

        isContiniu = input('是否继续添加？y/n:')
        if isContiniu.upper() == 'Y':
            continue
        else:
            break


def updateUser():
    if len(studentInfo) == 0:
        print('系统没有数据！')
        return

    while True:
        id = input('请输入要修改的学生id：')
        if id == '':
            print('id有误，请重新输入！')
            continue
        for index, item in enumerate(studentInfo):
            if item.get('id') == id:

                name = input('请输入name：')
                if name == '':
                    print('name有误，请重新输入！')
                    continue
                phone = input('请输入phone：')
                if phone == '':
                    print('phone有误，请重新输入！')
                    continue
                studentInfo[index] = {'id': id, 'name': name, 'phone': phone}
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(studentInfo, f, ensure_ascii=False, indent=4)
                    print(f'修改id为{id}的学生成功')
                    break
        else:
            print(f'没有找到id为{id}的学生！')

        isContiniu = input('是否继续修改？y/n:')
        if isContiniu.upper() == 'Y':
            continue
        else:
            break


def deleteUser():
    while True:
        if len(studentInfo) == 0:
            print('系统没有数据！')
            return

        id = input('请输入要删除的学生id：')
        if id == '':
            print('id有误，请重新输入！')
            continue
        for index, item in enumerate(studentInfo):
            if item.get('id') == id:
                studentInfo.pop(index)
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(studentInfo, f, ensure_ascii=False, indent=4)
                    print(f'删除id为{id}的学生成功')
                    break
        else:
            print(f'没有找到id为{id}的学生！')

        isContiniu = input('是否继续删除？y/n:')
        if isContiniu.upper() == 'Y':
            continue
        else:
            break


def showOne():
    if len(studentInfo) == 0:
        print('系统没有数据！')
        return

    while True:
        id = input('请输入id：')
        for i in range(len(studentInfo)):
            if studentInfo[i].get('id') == id:
                print('id'.center(10), 'name'.center(10), 'phone'.center(10))
                print(studentInfo[i].get('id').center(10), studentInfo[i].get('name').center(10),
                      studentInfo[i].get('phone').center(10))
                break
        else:
            print(f'没有找到id为{id}的学生！')

        isContiniu = input('是否继续查询？y/n:')
        if isContiniu.upper() == 'Y':
            continue
        else:
            break


def showAll():
    if len(studentInfo) == 0:
        print('系统没有数据！')
        return

    print(f'所有学生信息为：')
    print('id'.ljust(10), 'name'.ljust(10), 'phone'.ljust(15))
    for i in range(len(studentInfo)):
        print(studentInfo[i].get('id').ljust(10), studentInfo[i].get('name').ljust(10),
              studentInfo[i].get('phone').ljust(10))


main()
