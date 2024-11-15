# 学生管理系统

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

STU_LIST = []
STU_FILE = "students.txt"


def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    with open(STU_FILE, "r", encoding="utf-8") as file:
        for line in file:
            print(line)
            
    pass


def get_choice():
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    get = int(input("请输入你想执行的操作的编号："))
    return get
    pass


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    print("------------------")
    print("欢迎使用我做的豆腐渣工程学生管理系统!<smile>")
    print("PS:修改完学生信息后别忘了保存到文件(按5)")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 保存学生信息至文件中")
    print("6. 查看已经保存在文件中的所有学生的信息")
    print("0. 退出学生管理系统")
    print("------------------")
    pass
    
def exec(choice):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if(choice == 1):
        stu_add()
    elif(choice == 2):
        stu_del()
    elif(choice == 3):
        stu_mod()
    elif(choice == 4):
        stu_sel()
    elif(choice == 0):
        pass
    elif(choice == 5):
        stu_save()
    elif(choice == 6):
        stu_init()
    else:
        print("输入有误, 请重新输入")
    pass
    
def stu_add():
    """此函数用于, 添加学生信息"""
    print("开始添加学生信息")
    global STU_LIST
    id = input("请输入该生的学号: ")
    name = input("请输入该生的姓名：")
    college = input("请输入该生所在学院：")
    major = input("请输入该生的专业：")
    gpa = input("请输入该生的GPA: ")
    stu = {"id": id, "name": name, "college": college,"major": major, "gpa": gpa}
    STU_LIST.append(stu)
    print("学生信息添加成功")
    pass

def stu_del():
    """此函数用于, 删除学生信息"""
    print("开始删除学生信息")
    global STU_LIST
    id = input("请输入要删除的学生的学号: ")
    for stu in STU_LIST:
        if stu["id"] == id:
            STU_LIST.remove(stu)
            return
    print("系统中不存在该学生的信息")


def stu_mod():
    """此函数用于, 修改学生信息"""
    print("开始修改学生信息")
    global STU_LIST
    id = input("请输入要修改的学生的学号: ")
    for stu in STU_LIST:
        if stu["id"] == id:
            stu["name"] == input("请输入该生的姓名：")
            input("是否继续修改？(y/n)")
            if input() == "n":
                print("修改成功")
                return
            elif input() == "y":
                stu["college"] = input("请输入该生的学院：")
                input("是否继续修改？(y/n)")
                if input() == "n":
                    print("修改成功")
                    return
                elif input() == "y":
                    stu["major"] = input("请输入该生的专业: ")
                    input("是否继续修改？(y/n)")
                    if input() == "n":
                        print("修改成功")
                    elif input() == "y":
                        stu["gpa"] = input("请输入该生的GPA: ")
                        print("修改成功")
                    return
    print("系统中不存在该学生的信息")            


def stu_sel():
    """此函数用于, 查询学生信息"""
    print("开始查询学生的信息")
    global STU_LIST
    id = input("请输入要查询的学生的学号: ")
    for stu in STU_LIST:
        if stu["id"] == id:
            print("该生的姓名是：", stu["name"])
            print("该生的学院是：",stu["college"])
            print("该生的专业是：", stu["major"])
            print("该生的GPA是: ", stu["gpa"])
            return
    print("系统中不存在该学生的信息")
    pass


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    print("开始将学生信息保存到文件中")
    with open(STU_FILE, "w", encoding="utf-8") as file:
        for stu in STU_LIST:
            file.write(stu["id"] + " " + stu["name"] + " " + stu["major"] + " " + stu["gpa"] + "\n")
            print("保存成功")
    pass


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    menu()
    user_choice = get_choice()
    while user_choice != 0:
        menu()
        exec(user_choice)
        user_choice = get_choice()
    pass


if __name__ == '__main__':
    main()
