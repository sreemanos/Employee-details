import re 
import datetime

def findage(birthDate):
     today = datetime.date.today()
     age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
     return age

def Repeated(employeeName): 
    flag=0 
    for i in range (0,len(employeeName)-2):  
            if employeeName[i]==employeeName[i+1]==employeeName[i+2]:  
                flag=1 
                break 
    if flag==1: 
        return False 
    return True 

 
def validateName(): 
    employeeName=input("Enter Employee Name:") 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if employeeName.isalpha() and len(employeeName)>2 and Repeated(employeeName): 
        print("Employee Name:"+employeeName) 
    elif(regex.search(employeeName) != None):
        print("String is not accepted as it has special characters, so enter a valid name")
        validateName()
    elif employeeName.isnumeric():
        print("It has numbers, so enter a valid name")
        validateName()
    #elif employeeName.isalnum():
    #    print("It has both name and numbers, so enter a valid name name")
     #   validateName()
    elif employeeName.isspace():
        print("It has space, so enter a valid name")
        validateName()          
    else: 
        print("Invalid name , Please enter the first name or no repeating characters and length must be greater than 2") 
        validateName() 
 
validateName() 

 
def validateId(): 
    employeeId=input("Enter Employee Id:") 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if employeeId.isnumeric() and (len(employeeId))==4: 
       # validatedId=employeeId.zfill(4) 
        print("Employee ID:ACE"+employeeId)
    elif(regex.search(employeeId) != None):
        print("It has special characters, so enter a valid id")
        validateId()
    elif len(employeeId)>4 or len(employeeId)==1 or len(employeeId)==2 or len(employeeId)==3:
        print("Employee Id must contain only 4 numbers, so enter a valid employee id")   
        validateId()  
    elif employeeId.isalpha(): 
        print("Employee Id must not contain alphabets")
        validateId()  
    elif employeeId.isalnum():
        print("It has both name and numbers, so enter only proper id")   
        validateId()      
    else: 
        print("The range must be 4 digit number. So, enter a valid Employee Id") 
        validateId() 
 
validateId() 

 
def validateEmail(): 
    regex ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}' 
    employeeEmail=input("Enter Email id:") 
    if(re.fullmatch(regex,employeeEmail)): 
        print("Email Id:"+employeeEmail) 
    else: 
        print("Invalid Email, Please enter a valid email id") 
        validateEmail() 
 
validateEmail() 


def validatedob():
    try:
       dob1=input('Enter your DOB in the given valid format YYYY-MM-DD:')
       dob= datetime.datetime.strptime(dob1, '%Y-%m-%d')
       age=findage(dob)
       if age<0:
          print("you have entered a future date, enter valid DOB")
          validatedob()
       elif age<18:
          print('You age should be greater then 18 and below 60, enter valid DOB')
          validatedob()
       elif age>60:
          print("Invalid one, try again")
          validatedob()
       else:
          print("The age is",age)
    except ValueError:
          print("Invalid format, so enter again")
          validatedob()

validatedob()    


def validatedoj():
    try:
      doj1=input('Enter your DOJ in the format YYYY-MM-DD:')
      doj= datetime.datetime.strptime(doj1, '%Y-%m-%d')
      exp=findage(doj)
      if exp<0:
         print("you have entered a future date")
         validatedoj() 
      else:
         print("Your experience is",str(exp))
    except  ValueError:
         print("Invalid DOJ, Kindly check the format and enter again")   
         validatedoj()  
     
validatedoj()  


def validateSalary(): 
    try: 
        salary=int(input("Enter your salary:")) 
        if salary<=0: 
            print("Salary should not be zero and negative numbers") 
            validateSalary() 
        if salary>5000000 and salary<300000:
            print("Salary limit exceeded ot its invalid") 
            validateSalary() 
        else: 
            print("The salary is",salary) 
    except ValueError: 
        print("Salary should consist only digits") 
        validateSalary() 
 
validateSalary() 


def validateMobilenum(): 
    employeeMobile=input("Enter Mobile number:") 
    regex=re.compile("(0|91)?[7-9][0-9]{9}")
    regex1 = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if employeeMobile.isdigit() and len(employeeMobile)==10 and re.fullmatch(regex,employeeMobile): 
        print("Mobile Number:"+employeeMobile)
    elif(regex1.search(employeeMobile) != None):
        print("It has special characters, so enter a valid id")
        validateMobilenum()    
    elif len(employeeMobile)>10 or len(employeeMobile)<10:
       print("The lenght must be 10 digits, so enter valid mobile number") 
       validateMobilenum()      
    else: 
        print("The mobile number must start with 7 or 8 or 9 and it must not contain alphabets and special characters, so enter a valid mobile number") 
        validateMobilenum() 
 
validateMobilenum() 

 
print("1.B.E\n2.B.Tech\n3.M.E\n4.Bsc\n5.Others") 
def validateQualification(): 
    qualification={1:"B.E", 2:"B.Tech", 3:"M.E", 4:"Bsc", 5:"Others"} 
    key=int(input("Choose your qualification:")) 
    print(qualification.get(key,"Invalid Choice")) 
    if key==5: 
        qual=input("Enter from above options")
        print("The qualification is"+qual) 
        
    if key>5 or key==0: 
        print("Please select from above") 
        validateQualification()     
 
validateQualification()
