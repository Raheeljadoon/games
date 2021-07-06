class School:
    school_list = ["punjab","jinnah","american"]
    

    def __init__(self,school_name):
        self.name = school_name
       
        

    def create(self):
        new_value = input("enter name of school  " )
        self.school_list.append(new_value)

    def delete(self,n):
        self.school_list.remove(n)

    def read(self):
        print(self.school_list)

    def update(self):
        self.name = input(str("please enter new name :")) 
        
        #return self.school_list.append(self.name)   
    
    

   
        



class Teacher:

    Teacher_Name = ["kamal","kamran","yousuf","ikram","junaid","sultan","rafaqat","iqbal","sijad"]

    def __init__(self,t_name,t_age):
        self.name = t_name
        self.age = t_age

    def create(self):
        new_value = input("enter name of teacher  " )
        self.Teacher_Name.append(new_value)

    def delete(self,n):
        self.Teacher_Name.remove(n)

    def read(self):
        print(self.Teacher_Name)
    def update(self):
        self.name = input(str("please enter new name :"))
 

   

class Students:

    Student_Name = ["raheel","ahmed","kashif","umair","mohsin","adnan","shanoor","sohrab","ahtisham","usama","usman"]
    

    def __init__(self,s_name,s_age):
        
        

        self.s_name= s_name
        self.s_age = s_age


    def create(self):
        new_value = input("enter name of student  " )
        self.Student_Name.append(new_value)

    def delete(self,n):
        self.Student_Name.remove(n)

    def read(self):
        print(self.Student_Name)

    def update(self):
        self.name = input(str("please enter new name :")) 




print("what information do you want to see")
choice1 = int(input("  1:school name \n  2:teacher name \n  3:students name  "))

if choice1 == 1 :

    school = School("raheel")
   
    print("Names of school are" ,school.school_list)

    choice2 = int(input("what you want to do \n  1:update \n  2:delete \n  3:read \n  4:create   "))

    if choice2 == 1:
        school.update()


    elif choice2 == 2:
        
        n = input(("which name you wanted to delete  "))
        school.delete(n)
        print("new list is ,", school.school_list)


    elif choice2 == 3:
        school.read()

    elif choice2 == 4:

        school.create()

        print("new list is ,", school.school_list)





        




elif choice1 == 2 :
    teacher = Teacher
    print("Names of teacher are ", teacher.Teacher_Name)

    choice3 = int(input("what you want to do \n  1:update \n  2:delete \n  3:read \n  4:create   "))

    if choice3 == 1:
        teacher.update()


    elif choice3 == 2:
        n = input(("which name you wanted to delete  "))
        teacher.delete(n)
        print("new list is ,", teacher.school_list)


    elif choice3 == 3:
        teacher.read()


    elif choice3 == 4 :
        teacher.create()
        print("new list is ", teacher.Teacher_Name)


else:


    student = Students("sd",23)
    
    print("Names of students are " ,student.Student_Name)

    choice4 = int(input("what you want to do \n  1:update \n  2:delete \n  3:read \n  4:create   "))

    if choice4 == 1:
        student.update()


    elif choice4 == 2:
        n = input(("which name you wanted to delete  "))
        student.delete(n)
        print("new list is ,", student.school_list)


    elif choice4 == 3:
        student.read()


    elif choice4 == 4 :
       student.create()
       print("new list is ",student.Student_Name)






