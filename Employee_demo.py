from pymongo import MongoClient
import sys
client=MongoClient('mongodb://localhost:27017/')
demodb=client.sample
democollection=demodb.Employee
class Employee_demo:
    def insert_employee(self,Empid,Empname,Mobileno):

        if(emp_obj.find_employee(Empid)=='true'):
            ch=input("Employee exists.Do u want to update Y/n")
            if(ch=='y'):
                action==2
            else:
                sys.exit()
        else:
            Emprecord={'Empid':Empid,'Empname':Empname,'Mobileno':Mobileno}
            return demodb.Employee.insert_one(Emprecord)
    def update_employee(self,Empid,Empname,Mobileno):
        if (emp_obj.find_employee(Empid) == 'true'):

            myquery={'Empid':Empid}
            newvalues={"$set":{'Empname':Empname,'Mobileno':Mobileno}}
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


emp_obj=Employee_demo()
while(True):

    print("1.Insertion\t2.update\t3.Delete")
    action=int(input("enter a number"))
    if(action==1):
        Empid=input("enter Employeeid")
                
        Empname=input("enter Employee name")
        Mobileno=input("enter Mobileno")
        record_inserted=emp_obj.insert_employee(Empid,Empname,Mobileno)
        print("Record inserted with id",record_inserted)
    elif(action==2):
        Empid = input("enter Employeeid")
        Empname = input("enter Employee name")
        Mobileno = input("enter Mobileno")
        result=emp_obj.update_employee(Empid,Empname,Mobileno)
        print("data updated with id",result)
    elif(action==3):
        Empid=input("enter Employeeid")
        record_deleted=emp_obj.delete_employee(Empid)
        print("record deleted with id",record_deleted)
    else:
        sys.exit()






