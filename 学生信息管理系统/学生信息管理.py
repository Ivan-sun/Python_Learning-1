
import os
filename='student.txt'

def main():
    while True:
        menu()
        try:
            #choice=int(input('请选择对应的功能'))              # 需要考虑进行输入文本的判定，其他无效输入报错   
            choice=input_func()   
        except Exception as r:
            print('你输入错误 %s' %r)
            continue
       
        if choice in [0,1,2,3,4,5,6,7]:               
            if choice==0:
                answer=input('您确定要退出系统吗？y/n  ')
                if answer=='y' or answer=='Y':
                    print('感谢您的使用！！！')
                    print('已退出系统')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert()    #录入学生信息
            elif choice==2:
                search()    #查找学生信息
            elif choice==3:
                delete()    #删除学生信息
            elif choice==4:
                modify()    #修改学生信息
            elif choice==5:
                sort()      #排序
            elif choice==6:
                total()     #统计学生总数
            elif choice==7:
                show()      #显示所有学生信息

def input_func():
    choice=input('请选择对应功能！！！')    
    return int(choice)

def menu():
    print('========================================学生信息管理系统========================================')
    print('----------------------------------------功能菜单-----------------------------------------------')
    print('\t\t\t\t  1.录入学生信息')
    print('\t\t\t\t  2.查找学生信息')
    print('\t\t\t\t  3.删除学生信息')
    print('\t\t\t\t  4.修改学生信息')
    print('\t\t\t\t  5.排序')
    print('\t\t\t\t  6.统计学生总数')
    print('\t\t\t\t  7.显示所有学生信息')
    print('\t\t\t\t  0.退出系统')
    print('-----------------------------------------------------------------------------------------------')

def insert():
    student_list=[]
    while True:
        id = input('请输入ID:')
        if not id:
            break
        name= input('请输入姓名：')
        if not name:
            break
        
        try:
            english=float(input('请输入英语成绩:'))
            python=float(input('请输入Python成绩:'))
            java=float(input('请输入Java成绩:'))
        except:
            print('输入无效，不是数字类型，请重新输入')
            continue

        #将录入的学生信息保存到字典中
        student={'id':id,'name':name,'English':english,'Python':python,'Java':java}
        #将学生信息添加到列表当中
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #调用save()函数，保存列表
    save(student_list)
    print('学生信息录入完毕！！！')

def new_func():
    id=input('请输入ID：')
    return id

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for i in lst:
        stu_txt.write(str(i)+'\n')
    stu_txt.close()

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode = input('按ID查找-->输入1 \n按姓名查找-->输入2 \n')
            if mode == '1':
                id = input('请输入要查找的学生ID: ')
            elif mode == '2':
                name = input('请输入要查找学生的姓名: ')
            else:
                print('您的输入有误，请重新输入')
                continue

            with open(filename,'r',encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id !='':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            
            show_student(student_query)
            student_query.clear()
            answer = input('是否要继续查询？y/n \n')
            if answer == 'y':
                continue
            else:
                break
                                 
        else:
            print('暂未存储任何学生信息！')
            return

def show_student(lst):
    if len(lst) ==0:
        print('未查到学生信息，无数据显示！！！')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('English'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 float(item.get('English'))+float(item.get('Python'))+float(item.get('Java'))
                                 ))


def delete():
    while True:
        student_id=input('请输入要删除的学生ID： ')
        if student_id!='':
                if os.path.exists(filename):
                    with open (filename,'r',encoding='utf-8')as file:
                        student_old=file.readlines()
                else:
                    student_old=[]
                flag=False
                if student_old:
                    with open(filename,'w',encoding='utf-8') as wfile:
                        d={}
                        for item in student_old:
                            d=dict(eval(item))      #将字符串转成字典
                            #print(type(d))
                            if d['id']!=student_id:
                                wfile.write(str(d)+'\n')
                            else:
                                flag=True
                        if flag:
                            print(f'id为{student_id}的学生信息已被删除')
                        else:
                            print(f'没有找到id为{student_id}的学生信息')
                else:
                    print('无学生信息')
                    break
                show()
                answer=input('是否继续删除？y/n\n')
                if answer =='y':
                    continue
                else:
                    break
                      
               
def modify():
    show()
    if os.path.exists(filename):
        with open (filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id= input('请输入需要修改的学生ID: ')
    with open(filename,'w',encoding='utf-8') as wfile:
        flag=False
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                flag=True
                print('找到学生信息，可以修改信息了')
                while True:
                    try:
                        d['name']=input('请输入姓名: ')
                        d['English']=input('请输入英语成绩: ')
                        d['Python']=input('请输入Python成绩: ')
                        d['Java']=input('请输入Java成绩: ')
                    except:
                        print('您输入的信息有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                #print('修改成功！')

            else:
                wfile.write(str(d)+'\n')
        if flag:
            print(f'学号为{student_id}的学生信息修改成功！')
        else:
            print(f'学号为{student_id}的学生信息不存在！！！')

        wfile.close()                            # 关闭文件，对更新的数据进行保存
        answer=input('是否继续修改？ y/n \n')
        if answer == 'y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            stutdent_lst = rfile.readlines()
        stutdent_new = []
        for item in stutdent_lst:
            stutdent_new.append(eval(item))
    else:
        return
    sort_flag = input('请选择排序方式：\n\t0:升序\n\t1:降序\n\t')
    if sort_flag == '0':
        sort_flag_bool = False
    elif sort_flag == '1':
        sort_flag_bool = True
    else:
        print('你选择的排序方式无效！\n请重新输入！')
        sort()
    mode = input('请选择排序方式：\n\t'
                 '1:按英语成绩排序\n\t'
                 '2:按Python成绩排序\n\t'
                 '3:按Java成绩排序\n\t'
                 '0:按总成绩排序\n\t')
    if mode =='1':
        stutdent_new.sort(key = lambda x : float(x['English']),reverse=sort_flag_bool)
    elif mode =='2':
        stutdent_new.sort(key = lambda x : float(x['Python']),reverse=sort_flag_bool)
    elif mode =='3':
        stutdent_new.sort(key = lambda x : float(x['Java']),reverse=sort_flag_bool)
    elif mode =='0':
        stutdent_new.sort(key = lambda x : float(x['English'])+float(x['Python'])+float(x['Java']),reverse=sort_flag_bool)
    else:
        print('您选的排序方式有误！')
        sort()
    
    show_student(stutdent_new)
        

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
        if students:
            print(f'一共有{len(students)}名学生')
        else:
            print('未录入学生信息！')


    else:
        print('暂未保存数据信息...')
       

def show():
    student_lst = []
    if os.path.exists(filename):
        with open (filename,'r',encoding='utf-8') as rfile:
            student_list = rfile.readlines()
            for item in student_list:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过学生信息！')


if __name__ =='__main__':
    main()