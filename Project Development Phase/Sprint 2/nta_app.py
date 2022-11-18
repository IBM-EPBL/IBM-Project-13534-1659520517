import ibm_db
from flask import Flask,render_template, request,redirect,url_for,session
from glob import escape
app=Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=pkz96094;PWD=LhSkZlezmEjCYhw2;", "", "")

@app.route("/")
def register():
    return render_template("reg.html")

@app.route('/reg.html',methods=['POST'])

def storeUser():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        password = request.form['password']

        res = name + mail + password
        return render_template('reg.html')

        sql = "INSERT INTO customers (FULLNAME,EMAIL,PASSWORD) VALUES(?,?,?);"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt, 1, name)
        ibm_db.bind_param(stmt, 2, mail)
        ibm_db.bind_param(stmt, 3, password)
    return render_template('sign.html')


@app.route("/login")
def log_in():
    return render_template("sign.html")

@app.route('/sign.html',methods = ['POST'])

def getUser():
    if request.method == 'POST':
        user = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM CUSTOMERS where EMAIL = ?"
        stmt = ibm_db.prepare(conn,sql)
        email = user
        
        #Explicitly bind parameters

        ibm_db.bind_param(stmt, 1, user)
        ibm_db.execute(stmt)
        dictionary = ibm_db.fetch_assoc(stmt)
        pwd = dictionary["PASSWORD"]
        if password != pwd:
            return render_template('login.html')
        return render_template('index.html')

@app.route("/index")
def index():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)