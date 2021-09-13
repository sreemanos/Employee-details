#Employee Management System in Python
#Author - Sreeman Nithik
#Created on - 16-Aug-2021

import sys
import re

class Employees:
    def __init__(self,Employee_count):
        self.Employee_count=Employee_count
        self.Employee_name=None
        self.ACE_number=None
        self.Employee_email=None
        self.Quualification=None
        self.Mobile_number=None
        self.salary=None
    
    def Allocate_ID(self):
        self.ACE_number=f'ACE000{self.Employee_count}'
        #print('Welcome')
        print(f'Your employee Id is {self.ACE_number} ')
        ACE_number=int(input("Enter Employee Id:")) 
        print("Employee ID:ACE{0}".format(ACE_number)) 

    
    def Check_name(self):
        name=input("Enter a valid name:")
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                return False
            if any(char.isdigit() for char in name) :
                return False
        #Check for repeated char
            char_count=0
            for i in range(len(name)):
                char_count = 1
                for j in range(i + 1, len(name)):
                    if (name[i] != name[j]):
                        break
                    char_count += 1
                if char_count >2:
                    return False
            self.Employee_name=name
            return True

    def Validate_name(self):
        while(self.Check_name()==False):
            pass
        print("Name:" +self.Employee_name)

    def Validate_email(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email=input("Enter Email:")
        while(re.search(regex,email)==None):
            email=input("Enter valid Email:")
        else:
            self.Employee_email=email
    
    def Choose_qualification(self):
        switch={1:'BTech Information Technology',2:'BE Computer Science',3:'BE Automobile'}
        print("Select your Qualification")
        for i in range(1,4):
            print(f'Option {i} : {switch[i]}')
        self.Qualification=switch[int(input())]
        print(self.Qualification)
    
    def Validate_mobile(self):
        regex='(0|91)?[7-9][0-9]{9}'
        mobile=input("Enter mobile number:")
        while(re.search(regex,mobile)==None):
            mobile=input("Enter valid mobile number:")
        else:
            self.Mobile_number=mobile
    
    def Validate_salary(self):
        salary=input("Enter salary:")
        regex='^[0-9]{6,7}$'
        while (re.search(regex,salary)==None):
            salary=input("Enter valid salary:")
        self.salary=salary

    def Print_details(self):
        print("Details are")
        print(f'Name:          {self.Employee_name}')
        print(f'ACE ID.:       {self.ACE_number}')
        print(f'Email:         {self.Employee_email}')
        print(f'Qualification: {self.Qualification}')
        print(f'Number:        {self.Mobile_number}')
        print(f'Salary:        {self.salary}')

   
if __name__=="__main__":
    objects=[]
    operation={1 :"Enter Another Employee", 2 : "Quit"}
    while True:
        Employee=Employees(len(objects)+1)
        objects.append(Employee)
        Employee.Allocate_ID()
        Employee.Validate_name()
        Employee.Validate_email()
        Employee.Choose_qualification()
        Employee.Validate_mobile()
        Employee.Validate_salary()
        Employee.Print_details()
        print("Users wish")
        for i in range(1,3):
            print(f' {i} : {operation[i]}')
        choice=input()   
        if(int(choice)==2):
            print("Employee details")
            for i in objects:
                i.Print_details()
            break
        
    


    
    
    