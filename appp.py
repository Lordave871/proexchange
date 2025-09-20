
from flask import Flask,render_template, request,session,flash
from config import Config
import pymysql
import os
from flask_session import Session
import datetime
v=datetime.datetime.now()
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']
app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = \
#        'mysql://avnadmin:AVNS_DI3Sbd-yQoViLOuMUL@mysql-649e331-uchechukwudavid2024-8278.j.aivencloud.com/default.db'
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#
#connection = pymysql.connect(
    ##host=app.config['DATABASE_HOST'],
    #user=app.config['DATABASE_USER'],
    #password=app.config['DATABASE_PASSWORD'],
    #db=app.config['DATABASE_NAME'],
    #port=app.config['DATABASE_PORT'],
    #charset='utf8mb4',
    #cursorclass=pymysql.cursors.DictCursor
    
#) 
#cursor= connection.cursor()
#print("Done")

@app.route("/")
def home():    
    return render_template("index.html".)
                
@app.route("/transfer",methods=['GET','POST'])
def transfer():
    if request.method == "POST":
        
        benefeciary = request.form.get("accountno")
        session["name"]=benefeciary
        global amount
        amount = request.form.get("amount")
        return render_template("proceed.html")
    return render_template("transfer.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        first_name = request.form.get("accountno")
        print(first_name) 
        emal=request.form.get("email")
        pi=request.form.get("password") 
        print(pi)
        cursor.execute('SELECT * FROM Bankerd WHERE accountno = %s'%(first_name,))
        x=cursor.fetchone()
        for i in x:
            typet= x['AccountType']
            name =x["Name"]
            count=x['Country']
            ema=x['Email']
            ge=x['Gender']
            pin=x['Password']
            acc=x['accountno']
            global bala
            bala=x['Balance'] 
        if str(pin)==pi:
            session["country"]=count
            session["email"]= ema
            session["gender"]=ge
            session["password"]= pin
            session["accountno"]= acc
            session["balance"]= bala
            session["accounttype"]= typet
            session["name"]= name
            return render_template("dashboard.html")
        elif str(pin)!=pi:
            flash('Your pin is incorrect')
    return render_template("login.html")
    
@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":
        global first_name
        first_name = request.form.get("name")
        print(first_name)
        if first_name is not None and first_name == 'dave':
            flash('Looks like you have changed your name!')
        global gen
        gen = request.form.get("gender")
        global county
        county = request.form.get("country")
        return render_template("signin.html")
    return render_template("signup.html")

@app.route("/hidden",methods=['GET','POST'])
def hidden():
    if request.method == "POST":
        global first_name
        global gen
        global county
        emal=request.form.get("email")
        accountype = request.form.get("accountip")
        accountno = request.form.get("phone")
        passcode = request.form.get("password")
        sql="INSERT INTO Bankerd (id, Name,accountno,Country,Password,AccountType,Email,Gender) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(id, first_name,accountno,county,passcode,accountype,emal,gen)
        print("installed")
        return render_template("index.html") 
    return render_template("signin.html")  

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dash")
def dash():
     global bal
     return render_template("dashboard.html",bal=session["balance"])

@app.route("/proceed",methods=['GET','POST'])
def trans():
    global amount
    print(amount)
    if request.method == "POST":
        bal=session["balance"]
        pin = request.form.get("password")
        date="\nDATE :" +  v.strftime("%B") +' '+  v.strftime("%d") + "\t" + v.strftime("%A")
        cursor.execute('SELECT * FROM Bankerd WHERE accountno = %s'%(beneficiary,))
        x=cursor.fetchone()
        name="LORDAVE"
        for i in x:
            typet= x['AccountType']
            print(typet)
            count=x['Country']
            ema=x['Email']
            ge=x['Gender']
            nam=x['Name']
            pin=x['Password']
            acc=x['accountno']
            global bala
            bala=x['Balance'] 
        if pin==pas:
            bal-=amoot
            bala+=amoot
            insert_ques= '''UPDATE Bankerd SET Balance= %s WHERE Account_no =%s '''%(bala , beneficiary)
            cursor.execute(insert_ques)
            connection.commit()
            ma="\nDATE :" +  v.strftime("%B") +' '+  v.strftime("%d") + "\t" + v.strftime("%A") + "\nYou received " + str(amoot) + "from "+ str(self.name) 
            insert_ques= '''UPDATE Bankerd SET Balance= %s WHERE Account_no =%s '''%(bal , self.no)
            cursor.execute(insert_ques)
            connection.commit()
            ma="\nDATE :" +  v.strftime("%B") +' '+  v.strftime("%d") + "\t" + v.strftime("%A") + "\nYou Sent " + str(amoot) + "to "+ str(namm)
            sql="INSERT INTO Mail (account, Mail,date) VALUES(%s,%s,%s)"
            val=(beneficiary,ma,date)
            cursor.execute(sql, val)
            connectin.commit()
            sql="INSERT INTO Mail (account, Mail,date) VALUES(%s,%s,%s)"
            val=(aza,mal,date)
            cursor.execute(sql, val)
            connection.commit()
            print("installed")
            return "Transfer sucessful"
            flash('Transaction successful')
            return render_template("dashboard.html") 
        else:
            return "Wrong pin"
            return render_template("dashboard.html")
    benefeciary=session.get('name')
    return render_template("proceed.html",name=benefeciary,amoun=amount) 

@app.route("/mail")
def mail():
    date="\nDATE :" +  v.strftime("%B") +' '+  v.strftime("%d") + "\t" + v.strftime("%A")
    data='You ,transferred, 2000 ,to ,dave'
    datee=v.strftime("%B") +' '+  v.strftime("%d") +","+  "\t" + v.strftime("%A") + ' : You transferred 2000 to NDavid' 
    return render_template("mail.html",details=datee,date=date)

@app.route("/profile")
def profile():
    cursor.execute('SELECT * FROM Bankerd WHERE accountno = %s'%(first_name,))
    x=cursor.fetchone()
    for i in x:
        typet= x['AccountType']
        print(typet)
        count=x['Country']
        ema=x['Email']
        ge=x['Gender']
        nam=x['Name']
        pin=x['Password']
        acc=x['accountno']
        global bala
        bala=x['Balance'] 
        return render_template("profile.html")

@app.route("/Deposit")
def Deposit():
    first_name = request.form.get("Amount")
    print(first_name) 
    amount=request.form.get("password") 
    print(amount)
    return render_template("deposit.html")

@app.route("/grexle")
def gaa():
    global hand
    return hand

@app.route("/swap")
def swap():
    return render_template("swap.html")

 
if __name__ == '__main__':
    app.run(debug=True,port=8000)


                

                        
                        

        

                

