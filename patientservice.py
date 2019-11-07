from dboperations import patientDbOperations
from patient import patient
from beautifultable import BeautifulTable
from patient import report
from patient import doctor
from patient import med
from patient import login
from patient import update
from patient import med_p

class PatientService:    

    def __init__(self):
        self.ps = patientDbOperations()
#add patient
    def add_patient(self):
        name = input("Paitent Name : ")
        phone = input("Paitent Phone Number : ")
        problem = input("Nature of Problem :")
        print("1.OPD 2.EMERGENCY ")
        choice = int(input("Enter 1 for OPD or 2 for EMERGENCY :"))
        if choice == 1:
            fee=400
            ward ='OPD'
        else:
            fee=1000
            ward ='EMERGENCY'
        self.show_doc()
        print("Please select Doctors from above table")
        docname = input("Doctor Name :")
        date = input("Enter Date of Admission (YYYY-MM-DD) :")
        print("Estimated fees is {} for doctor {} ".format(fee,docname))
        payment = input("Payment Method (CASH/CARD) : ")
        Patient = patient(0,name, phone, payment, problem,ward,docname,date)
        print("Patient Data added sucessfully  ")
        self.ps.add_patient(Patient)       
        Patients = self.ps.search_number(phone)
        if Patients:
            PatientService.paint_data_list(Patients)
        else:
            print("No data found with Patient ID :{}".format(phone))        

#update patient details
    def update_patient(self):
        print("Enter the Following Details For Updating Patient Details ")
        pid=input("Enter PID to Update :")
        name = input("Paitent Name : ")
        phone = input("Paitent Phone Number : ")
        problem = input("Nature of Problem :")
        print("1.OPD 2.EMERGENCY ")
        choice = int(input("Enter 1 for OPD or 2 for EMERGENCY :"))
        if choice == 1:
            fee=400
            ward='OPD'
        else:
            fee=1000
            ward='EMERGENCY'
        self.show_doc()
        print("Please select Doctors from above table")
        docname = input("Doctor Name :")
        print("Estimated fees is {} for doctor {} ".format(fee,docname))
        payment = input("Payment Method (CASH/CARD) : ")
        Patient = update(name, phone, payment, problem,ward, docname,pid)
        print("Patient Data Updated Sucessfully  ")
        self.ps.update_patient(Patient)
        Patients = self.ps.search_patient(pid)
        if Patients:
            PatientService.paint_data_list(Patients)
        else:
            print("No data found with Patient ID to Update :{}".format(pid))

            
#show all patients details
    def show_all_patients(self):
        print("Following table shows all patient details ")
        Patients = self.ps.get_all_patients()
        PatientService.paint_data_list(Patients)

#search patient details
    def search_patient(self):
        pid = input("Enter Patient ID :")
        Patients = self.ps.search_patient(pid)
        if Patients:
            PatientService.paint_data_list(Patients)
        else:
            print("No data found with Patient ID :{}".format(pid))


#add reports        
    def test_module(self):
        pid=input("Enter PID to add test results :")
        test_u=input("Enter test underwent : ")
        test_r=input("Enter test results : ")
        dod=input("enter date of Test done :")
        Patients = report(test_u,test_r,dod,pid)
        print("Reports updated sucessfully")
        self.ps.test_module(Patients)
        Pid = self.ps.search_reports(pid)
        if Pid:
            PatientService.paint_data_list2(Pid)
        else:
            print("No data found with Patient ID:{}".format(pid))

#show reports        
    def show_test(self):
        print("Following table shows all Test details ")
        reports = self.ps.get_all_reports()
        PatientService.paint_data_list2(reports) 

#doctors module for updating/adding
    def doc_module(self):
        print("Please enter the following for updating Doctor Module")
        name=input("Enter Doctor name : ")
        dept=input("Enter Doctot DEpt : ")
        availabity=input("Wheather Doctot availabe now : ")
        doctors = doctor(name,dept,availabity)
        print("Doctors Details updated sucessfully ")
        self.ps.doc_module(doctors)
        self.show_doc()

#show doctors        
    def show_doc(self):
        print("Following table Shows Doctors Details")
        doctor = self.ps.get_all_docs()
        PatientService.paint_data_list3(doctor)
        


#medice module for adding/updating medicine
    def med_module(self):
        print("Enter the following to add Medicine in Medicine Module")
        pid=input("Enter PID to add Medicines:")
        med_name=input("Enter Medicine name : ")
        quant=input("Enter the Quantity of Medicines : ")
        meds = med(med_name,quant,pid)
        print("Medicines Details updated sucessfully ")
        self.ps.med_module(meds)
        Meds = self.ps.search_med(pid)
        if Meds:
            PatientService.paint_data_list4(Meds)
        else:
            print("No Medicine data found with Patient ID :{}".format(pid))
#show medicines
    def show_med(self):
        print("Following table Shows Medicine Details")
        med = self.ps.get_all_meds()
        PatientService.paint_data_list4(med)    


#login module
    def login_module(self):
        i_d = input("Enter ID : ")
        name = input("Enter Name : ")
        un = input("Enter UserName : ")
        pwd = input("Enter Password : ")
        Login = login(i_d,name,un,pwd)
        self.ps.login_module(Login)
        self.show_login()
#show logins
    def show_login(self):
        login=self.ps.get_all_logins()
        PatientService.paint_data_list5(login)
        

#user module
    def user_module(self):
        
        choice = input("1.Add user 2.Delete User :")
        
        if choice == '1':
            name = input("Enter Name : ")
            un = input("Enter UserName : ")
            pwd = input("Enter Password : ")
            Login = login(0,name,un,pwd)
            self.ps.login_module(Login)
            print("User added sucessfully :")
            self.show_login()
        elif choice == '2':
            i_d = int(input("Enter userid : "))
            Del = login(i_d,0,0,0)
            self.ps.user_delete(Del)
            print("Deleted sucessfully")
            self.show_login()
        else:
            print("Invald Choice ")

#search module
    def search(self):
        print("1.Search Patient Details 2.Search Doctors 3.Search Reports :")
        choice = input("Enter your choice (1~3) :")
        if choice == '1':
            pid = input("Enter Patient ID :")
            Patients = self.ps.search_patient(pid)
            if Patients:
                PatientService.paint_data_list(Patients)
            else:
                print("No data found with Patient ID :{}".format(pid))

        elif choice == '2':
            name = input("Enter Doctor name :")
            Docs = self.ps.search_doc(name)
            if Docs:
                PatientService.paint_data_list3(Docs)
            else:
                print("No data found with doctor name :{}".format(name))
        elif choice == '3' :
            pid = input("Enter Patient ID to see Reports :")
            Pid = self.ps.search_reports(pid)
            if Pid:
                PatientService.paint_data_list2(Pid)
            else:
                print("No data found with Patient ID:{}".format(pid))
        else:
            print("Invalid choice")
                
#Patient module
    @staticmethod
    def paint_data_list(data):
        table = BeautifulTable()
        table.column_headers = ["PATIENT ID","PATIENT NAME", "PHONENUMBER", "PAYMENT", "PROBLEM", "WARD","DOCTOR_NAME","DOA"]
        for li in data:
            table.append_row([li.pid,li.name, li.phone, li.payment, li.problem,li.ward, li.docname,li.date])
        print(table)
        
    
#reports module
    @staticmethod
    def paint_data_list2(data):
        table = BeautifulTable()
        table.column_headers = ["PATIENT ID","PATIENT NAME","PROBLEM","DOCTOR NAME","TEST DONE","TEST RESULT", "TEST DATE"]
        for li in data:
            table.append_row([li.pid, li.name,li.problem,li.doc, li.test_u, li.test_r,li.dod])
        print(table)


#doctor module
    @staticmethod
    def paint_data_list3(data):
        table = BeautifulTable()
        table.column_headers = ["NAME", "DEPT", "AVAILABITY"]
        for li in data:
            table.append_row([li.name, li.dept, li.availabity])
        print(table)

#medicinemodule
    @staticmethod
    def paint_data_list4(data):
        table = BeautifulTable()
        table.column_headers = ["PATIENT ID","NAME","DOCTOR NAME","MEDICINE","QUANTITY"]
        for li in data:
            table.append_row([li.pid, li.name,li.docname, li.med,li.quant])
        print(table)    

#login module
    @staticmethod
    def paint_data_list5(data):
        table = BeautifulTable()
        table.column_headers = ["USER ID", "NAME", "USERNAME","PASSWORD"]
        for li in data:
            table.append_row([li.i_d, li.name, li.un,li.pwd])
        print(table)
