#paitent management system

if __name__ == '__main__':
        from patientservice import PatientService
        ps=PatientService()
    
        while True:
            
            print("*"*150)
            print("WELCOME TO PAITENT INFORMATION SYSYTEM")
            print("*"*150)
            print(" 1.Paitent Management Module\n 2.Add Test Reports\n 3.Show Test Reports\n 4.Add Doctor Details\n 5.Show Doctors \n 6.Add Medicines\n 7.Show Medicines\n 8.Login Module\n 9.User Management Module\n 10.SEARCH\n 11.Show all patients details\n 12.Update Patient Details\n 13.EXIT ")
            print("*"*80)
            choice = input("Enter your choice (1~13):")
            if choice == '1':
                ps.add_patient()
            elif choice == '2':
                ps.test_module()
            elif choice == '3':
                ps.show_test()
            elif choice == '4':
                ps.doc_module()
            elif choice == '5':
                ps.show_doc()
            elif choice == '6':
                ps.med_module()    
            elif choice == '7':
                ps.show_med()
            elif choice=='8':
                un=input("Enter user name :")
                pwd=input("Enter password :")
                if un == 'pms' and pwd == 'pms' :
                        ps.show_login()
                else:
                        print("invalid Login")
            elif choice == '9':
                un=input("Enter user name :")
                pwd=input("Enter password :")
                if un == 'pms' and pwd == 'pms' :
                        ps.user_module()
                else:
                        print("invalid Login")
            elif choice == '11':
                    ps.show_all_patients()
            elif choice == '10':
                    ps.search()
            elif choice == '12':
                    ps.update_patient()
            elif choice == '13':
                    print("Exiting Application............................")
                    exit();
            else:
                print("Enter only 1 to 13 ......")
        
    
     
