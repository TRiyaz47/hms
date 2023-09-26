import mysql.connector as mc
from datetime import datetime


"""
def function_template():
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='website')
        cursor=conn.cursor()
        conn.start_transaction()
        cursor.execute(query)
        temp = cursor.fetchall()
    except Exception as e:
    conn.rollback()
        
        print("An error occured",e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()
"""
def show_pat():#print patient table
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="hms")
        cursor=conn.cursor()
        conn.start_transaction()

        query="SELECT * FROM patients;"
        cursor.execute(query)
        db_return=cursor.fetchall()
        return db_return
    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")

    finally:
        cursor.close()
        conn.commit()
        conn.close()
#print(show_pat())


 
def show_appt():
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="hms")
        conn.start_transaction()
        cursor=conn.cursor()

        query="SELECT * FROM appointments"
        cursor.execute(query)
        db_return=cursor.fetchall()
        return db_return
    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()
#print(show_appt())

def add_pat(pat_details):#add values in patient table
#0-fname,1-lname,2-gender,3-dob,4-address,5-cntc_number
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='hms')
        cursor=conn.cursor()
        conn.start_transaction()

        query = "INSERT INTO patients (pat_fname, pat_lname, pat_gender, pat_dob, pat_add, pat_cntc_no) VALUES (%s, %s, %s, %s, %s, %s)"
        
        cursor.execute(query,pat_details)
        temp = cursor.fetchall()
        return True
    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return False
    finally:
        cursor.close()
        conn.commit()
        conn.close()
#pat_details=["connor","kenway","Male","2000-10-10","not_given","123456789",]
#add_pat(pat_details)

def add_doc(doc_details):#add values in doctor table
#0-name,1-gender,2-speciality,3-contact_num,4-dob,5-email
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='hms')
        cursor=conn.cursor()
        conn.start_transaction()

        query = "INSERT INTO doctors (doc_name,doc_gender,doc_speciality,doc_cntc_num,doc_dob,doc_email) VALUES (%s,%s,%s,%s,%s,%s);"
        
        cursor.execute(query,doc_details)
        temp = cursor.fetchall()
        return True
    except Exception as e:
        conn.rollback()
        print(f"An error occured as {e}")
        return False
    finally:
        cursor.close()
        conn.commit()
        conn.close()
#doc_details=["Octavious","Male","Biochemistry","123456789","1991-08-01","doc@gmail.com"]
#print(add_doc(doc_details))

def add_appointment(appt_details):
#0-doc_id,1-pat_id,2-appt_dataetime,3-appt_status,4-appt_notes
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="hms")
        conn.start_transaction
        cursor=conn.cursor()

        query="INSERT INTO appointments(doc_id,pat_id,appt_datetime,appt_status,appt_notes) VALUES (%s,%s,%s,%s,%s);"
        cursor.execute(query,appt_details)
        db_return=cursor.fetchall()
        return db_return
    except Exception as e:
        conn.rollback()
        print(f"An error occured as:\n {e}")
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()
    
#appt_datetime = datetime(2023, 10, 15, 14, 30, 0)  # YYYY, MM, DD, HH, MM, SS
#appt_details=[1,1,appt_datetime,"confirm","i have hypertension"]
#add_appointment(appt_details)

def login_db(cntc_num):
    try:
     
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="hms")
        cursor=conn.cursor()
        conn.start_transaction
        if cntc_num=="9321058483":
            user_details=[-1,"admin",0,0,0,0,0,"c"]
            return user_details
    

        #login type:a-patient
        query_a=f"SELECT * FROM patients WHERE pat_cntc_no='{cntc_num}';"
        cursor.execute(query_a)
        db_return_a=cursor.fetchall()
            
        #login type:b->doctor
        query_b=f"SELECT * FROM doctors WHERE doc_cntc_num='{cntc_num}';"
        cursor.execute(query_b)
        db_return_b=cursor.fetchall()

        if db_return_a !=[] and db_return_b==[]:
            user_type="a"
            user_details=list(db_return_a[0])
            user_details.append(user_type)
            return user_details
        elif db_return_b !=[] and db_return_a==[]:
            user_type="b"
            
            user_details=list(db_return_b[0])
            user_details.append(user_type)
            return user_details
        else:
            return False


    except Exception as e:
        conn.rollback()
        print(f"An error occured as:\n{e}")
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()

#print(login_db("123456789"))

def pat_appt_details(pat_id):
    try:
        conn=mc.connect(host="localhost",user="root",password="Tanwar9867@",database="hms")
        cursor=conn.cursor()
        conn.start_transaction()

        query="SELECT * FROM Appointments WHERE pat_id=%s;"
        params=[pat_id]

        cursor.execute(query,params)
        db_return=cursor.fetchall()
        if db_return ==[]:
            return False,"Can't Find any appointments"
        else:
            return db_return
    except Exception as e:
        conn.rollback()
        print(f"An error occurred as:\n{e}")
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()


#0-doc_id,1-pat_id,2-appt_dataetime,3-appt_status,4-appt_notes


#achieve three things""""
"""
1)Select doctors based on speciality
2)select timetable of of the selected doctor
"""

def show_doc(condition):#print doctor table
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="hms")
        conn.start_transaction()
        cursor=conn.cursor()
        if condition==None:
            query="SELECT * FROM doctors"
            cursor.execute(query)
        else:
            query="SELECT * FROM doctors WHERE doc_speciality=%s;"
            cursor.execute(query,[condition])
        db_return=cursor.fetchall()
        return db_return
    except Exception as e:
        conn.rollback()
        print(f"An error occured as:\n{e}")
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()
#print(show_doc(condition))        

def show_timetable(condition):
    try:
        conn=mc.connect(host="localhost",username="root",password="Tanwar9867@",database="hms")
        conn.start_transaction()
        cursor=conn.cursor()

        if condition==None:
            query="SELECT * FROM time_table;"
            cursor.execute(query)

        db_return=cursor.fetchall()
        return db_return
    except Exception as e:
        conn.rollback()
        print(f"An error occured as:\n{e}")
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()

condition=None    
print(show_timetable(condition))


