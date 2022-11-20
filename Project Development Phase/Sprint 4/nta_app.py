import ibm_db
from newsapi import NewsApiClient
from flask import Flask,render_template, request,redirect,url_for,session
from glob import escape
import os
app=Flask(__name__)

try:
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=pkz96094;PWD=hKNkPrVAhopkU1DI;", "", "")
    print("Connection successfull")
except:
    print("Error")

@app.route("/")
def register():
    return render_template("reg.html")

@app.route('/sign.html',methods=['POST'])

def storeUser():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        password = request.form['password']

        res = name + mail + password

        sql = "INSERT INTO CUSTOMERS (FULLNAME,EMAIL,PASSWORD) VALUES(?,?,?);"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt, 1, name)
        ibm_db.bind_param(stmt, 2, mail)
        ibm_db.bind_param(stmt, 3, password)
    return render_template('sign.html')



#@app.route("/news")
#def index():
 #   return render_template("index.html")

@app.route("/news")
def news():
    api_key = 'bc029995b2cd42fbb55c5ef94d088b83'
    
    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines(sources = "the-verge")
    all_articles = newsapi.get_everything(sources = "the-verge")

    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []   
    url_all = []

    for j in range(len(a_articles)): 
        main_all_articles = a_articles[j]   

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
        
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)

    
    return render_template("index.html",all = all)

@app.route("/search",methods = ['POST', 'GET'])
def searchFunct():
    inputText = request.form['nm']
    api_key = 'bc029995b2cd42fbb55c5ef94d088b83'
    
    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
    all_articles = newsapi.get_everything(q=inputText)

    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []   
    url_all = []

    for j in range(len(a_articles)): 
        main_all_articles = a_articles[j]   

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
        
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)

    return render_template('index.html', all = all)

@app.route("/login")
def log_in():
    return render_template("sign.html")

@app.route('/news',methods = ['POST'])

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
        #pwd = dictionary["PASSWORD"]
        #if password != pwd:
         #   return render_template('sign.html')
    return news()




if __name__=='__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(port=port,host='0.0.0.0',debug=True)