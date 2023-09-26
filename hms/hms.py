from flask import Flask, render_template, request, redirect, url_for, session
from db import login_db,pat_appt_details

app = Flask(__name__)
app.secret_key="This_secret_key"

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/login")
def login_web():
    if "user_id" in session:
        if session["user_type"]=="a":
            return redirect(url_for("pat_dashboard"))
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return redirect(url_for("admin_dashboard"))
    else:
        return render_template("login.html")

@app.route("/login_validation",methods=['GET','POST'])
def login_validation():
    if "user_id" in session:
        if session["user_type"]=="a":
            return redirect(url_for("pat_dashboard"))
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return redirect(url_for("admin_dashboard"))
    else:
        if request.method=="POST":
            cntc_number=request.form.get("cntc_num")
            feedback=login_db(str(cntc_number))

            if feedback is not False:
                session["cntc_number"]=cntc_number
                #return redirect(url_for("otp_validation_web"))
                return render_template("otp_validation.html")
            else:
                return render_template('login.html')
        
@app.route("/otp_validation_web")
def otp_validation_template():
    if "user_id" in session:
        if session["user_type"]=="a":
            return redirect(url_for("pat_dashboard"))
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return redirect(url_for("admin_dashboard"))
    else:
        return render_template("otp_validation.html")

@app.route("/otp_validation",methods=['GET','POST'])
def otp_validation():
    if "user_id" in session:
        if session["user_type"]=="a":
            return redirect(url_for("pat_dashboard"))
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return redirect(url_for("admin_dashboard"))
    else:
        cntc_number=session['cntc_number']
        #otp=generate_otp(cntc_number)
        otp1="123456"
        otp2=request.form.get("otp")
        if otp1==otp2:
            user_details=login_db(cntc_number)
            session['user_id']=user_details[0]
            session['user_name']=user_details[1]
            session['user_type']=user_details[7]
            user_type=user_details[7]
            #return f"{user_details}"

            if user_type=="a":
                return redirect(url_for("pat_dashboard"))
                #return "Correct"
            elif user_type=="b":
                return redirect(url_for("doc_dashboard"))
            elif user_type=="c":
                return redirect(url_for("admin_dashboard"))

        else:
            #return redirect(url_for("otp_validation_web"))
            return render_template("otp_validation.html")
    
@app.route("/pat_dashboard")
def pat_dashboard():
    if "user_id" in session:
        if session["user_type"]=="a":
            return render_template("patient.html")
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return redirect(url_for("admin_dashboard"))
    else:
        return redirect(url_for("login_web"))

@app.route("/doc_dashboard")
def doc_dashboard():
    if "user_id" in session:
        if session["user_type"]=="a":
            return render_template("doctor.html")
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return redirect(url_for("admin_dashboard"))
    else:
        return redirect(url_for("login_web"))

@app.route("/admin_dashboard")
def admin_dashboard():
    if "user_id" in session:
        if session["user_type"]=="a":
            return redirect(url_for("pat_dashboard"))
        elif session["user_type"]=="b":
            return redirect(url_for("doc_dashboard"))
        elif session["user_type"]=="c":
            return render_template("hospital.html")
    else:
        return redirect(url_for("login_web"))

@app.route("/logout")
def logout():
    if 'user_id' in session:
        session.pop("user_id")
    return redirect(url_for("login_web"))
    #return render_template("login.html")


@app.route('/render_pat_appts')
def render_pat_appts():
    if "user_id" in session and session['user_type']=='a':
        return redirect(url_for("pat_appts"))
    else:
        return "Unauthorized Access"


@app.route('/pat_appts',methods=['GET','POST'])
def pat_appts():
    if "user_id" in session and session['user_type']=='a':
        if request.method=="GET" or "POST":
            user_id=session['user_id']
            appt_details=pat_appt_details(user_id)
            return render_template("pat_appt.html",appt_details=appt_details)
    else:
        return "Unauthorized Access"
    
@app.route('/pat_book_appt')
def pat_book_appt():
    if "user_id" in session and session["user_type"]=="a":
        if request.method=="POST":
            #0-doc_id,1-pat_id,2-appt_dataetime,3-appt_status,4-appt_notes
            doc_id=request.form.get("doc_id")
            pat_id=request.form.get("pat_id")
            appt_datetime=request.form.get("appt_datetime")
            appt_status=request.form.get("appt_status")
            appt_notes=request.form.get("appt_notes")
            appt_details=[doc_id,pat_id,appt_datetime,appt_status,appt_notes]
            return "appointment successful"
        else:
            return render_template("pat_book_appt.html")
    else:
        return "Unauthorized Access"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
