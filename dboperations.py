import config
from util import DbUtil
import pymysql
from patient import patient
from patient import report
from patient import doctor
from patient import med
from patient import login
from patient import test
from patient import med_p

class patientDbOperations:

    def add_patient(self, new_patient):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into pms(pid,name,phone,payment,prob,ward,doc,doa) values(%s,%s,%s,%s,%s,%s,%s,%s)",(new_patient.pid,new_patient.name,new_patient.phone,new_patient.payment,new_patient.problem,new_patient.ward,new_patient.docname,new_patient.date))
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def search_number(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name,phone,payment,prob,ward,doc,doa from pms where phone like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                numb = self.get_list_data(rows)
                return numb
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def update_patient(self, contact):
        try:
            conn = DbUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("update pms set name=%s,phone=%s,payment=%s,prob=%s,ward=%s,doc=%s  where pid = %s", contact)
            conn.commit()
        except pymysql.DatabaseError as error:
            print("While updating ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(conn)
            DbUtil.close_cursor(cursor)

    def get_all_patients(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name,phone,payment,prob,ward,doc,doa from pms")
                rows = cursor.fetchall()
                Patients = self.get_list_data(rows)
                return Patients
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

    def search_patient(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name,phone,payment,prob,ward,doc,doa from pms where pid like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                Patients = self.get_list_data(rows)
                return Patients
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)
            
#reports module*************************************************************************************************************************************
#starts here for updating               
    def test_module(self, contact):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("update pms set tests = %s ,test_result = %s, test_date = %s where pid = %s", contact)
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

#to get all reports        
    def get_all_reports(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name,prob,doc,tests,test_result,test_date from pms")
                rows = cursor.fetchall()
                test = self.get_list_data2(rows)
                return test
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)                              

    def search_reports(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name,prob,doc,tests,test_result,test_date from pms where pid like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                Reports = self.get_list_data2(rows)
                return Reports
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)    
#reports module ends here******************************************************************************************************************************* 

#doctor module
#starts here for Add doctors

    def doc_module(self, new_doc):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into doc(name,dept,availabity) values(%s,%s,%s)", (new_doc.name, new_doc.dept, new_doc.availabity))
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

#to get all doctors
    def get_all_docs(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,dept,availabity from doc")
                rows = cursor.fetchall()
                doctor = self.get_list_data3(rows)
                return doctor
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

    def search_doc(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,dept,availabity from doc where name like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                doctor = self.get_list_data3(rows)
                return doctor
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)
#Ends here ******************************************************************************************************************************************************
#medicine module
                
    def med_module(self, med):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("update pms set med = %s ,quant = %s where pid = %s", med)
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def get_all_meds(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select pid,name,doc,med,quant from pms")
                rows = cursor.fetchall()
                med_p = self.get_list_data4(rows)
                return med_p
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)


    def search_med(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select  pid,name,doc,med,quant from pms where pid like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                med_p = self.get_list_data4(rows)
                return med_p
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)
#ends here ********************************************************************************************************************************************************
#login module
    def login_module(self, new_log):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into login(id,name,username,password) values(%s,%s,%s,%s)", (new_log.i_d, new_log.name, new_log.un,new_log.pwd))
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)
            
    def get_all_logins(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id,name,username,password from login")
                rows = cursor.fetchall()
                login = self.get_list_data5(rows)
                return login
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)        

#ends here**************************************************************************************************************************************************
#user module
                
    @staticmethod
    def user_delete(user):
        try:
            connection = DbUtil.get_connection()
            cursor = connection.cursor()
            print("User is going to delete with id ",user.i_d)
            cursor.execute("delete from login where id = %s ",str(user.i_d))
            connection.commit()

        except pymysql.DatabaseError as error:
            print("While deleting data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    @staticmethod                                 #for patient 
    def get_list_data(rows):
        return [patient(*row) for row in rows]


    @staticmethod                                 #for reports
    def get_list_data2(rows):
        return [test(*row) for row in rows]

    @staticmethod                                 #for doctor
    def get_list_data3(rows):
        return [doctor(*row) for row in rows]


    @staticmethod                                 #for medicine
    def get_list_data4(rows):
        return [med_p(*row) for row in rows]



    @staticmethod                                 #for login
    def get_list_data5(rows):
        return [login(*row) for row in rows]
    
