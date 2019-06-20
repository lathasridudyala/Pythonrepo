from pymongo import MongoClient
import sys
import re
client=MongoClient('localhost',27017)
demodb=client.sample
democollection=demodb.Employee
class Employee_demo1:
    def insert_employee(self,Empid,Empname,Mobileno_List):

        if(emp_obj.find_employee(Empid)=='true'):
            ch=input("Employee exists.Do u want to update Y/n")
            if(ch=='y'):
                action==2
            else:
                sys.exit()
        else:

            Emprecord={'Empid':Empid,'Empname':Empname,'Mobileno1':Mobileno_List[0],'Mobileno2':Mobileno_List[1]}
        return demodb.Employee.insert_one(Emprecord)
    def update_employee(self,Empid,Empname,Mobileno_List):
        if (emp_obj.find_employee(Empid) == 'true'):

            myquery={'Empid':Empid}
            newvalues={"$set":{'Empname':Empname,'Mobileno1':Mobileno_List[0],'Mobileno2':Mobileno_List[1]}}
            return democollection.update_one(myquery,newvalues)
        else:
            print("Employee do not Exist")
    def delete_employee(self,Empid):
        if (emp_obj.find_employee(Empid) == 'true'):

            return democollection.delete_one({'Empid':Empid})
        else:
            print("Employee do not Exist")
    def find_employee(self,Empid):
        if (democollection.count_documents({'Empid': Empid}) >= 1):
            return 'true'
        else:
            return 'false'
    def display(self):
        for i in democollection.find():
            print(i)
    def validate_mobilenum(self,Mobilenum):
        if not re.match("^[0-9]{10}", Mobilenum):
            print("Mobile number should be 10 digits")
            Mobilenum=input("Enter mobile number")
        return Mobilenum

emp_obj=Employee_demo1()
Mobileno_List=[]
while(True):

    print("1.Insertion\t2.update\t3.Delete\t4.display")
    action=int(input("enter a number"))
    if(action==1):
        Empid=input("enter Employeeid")

        Empname=input("enter Employee name")
        Mobileno1=input("enter Mobileno")
        Mobileno = emp_obj.validate_mobilenum(Mobileno1)
        Mobileno2=input("enter alternate mobileno")

        Mobileno_List.append(Mobileno)
        Mobileno_List.append(Mobileno2)
        record_inserted=emp_obj.insert_employee(Empid,Empname,Mobileno_List)
        print("Record inserted with id",record_inserted)
    elif(action==2):
        Empid = input("enter Employeeid")
        Empname = input("enter Employee name")
        Mobileno1 = input("enter Mobileno")
        Mobileno1 = emp_obj.validate_mobilenum(Mobileno1)
        Mobileno2 = input("enter alternate mobileno")
        Mobileno_List.append(Mobileno1)
        Mobileno_List.append(Mobileno2)
        result=emp_obj.update_employee(Empid,Empname,Mobileno_List)
        print("data updated with id",result)
    elif(action==3):
        Empid=input("enter Employeeid")
        record_deleted=emp_obj.delete_employee(Empid)
        print("record deleted with id",record_deleted)
    elif(action==4):
        emp_obj.display()
    else:
        sys.exit()







