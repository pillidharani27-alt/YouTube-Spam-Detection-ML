import pandas as pd
from flask import *
import mysql.connector

db=mysql.connector.connect(host='localhost',user="root",password="",port='3306',database='youtube')
cur=db.cursor()


app=Flask(__name__)
app.secret_key = "fghhdfgdfgrthrttgdfsadfsaffgd"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        useremail=request.form['useremail']
        session['useremail']=useremail
        userpassword=request.form['userpassword']
        sql="select count(*) from user where Email='%s' and Password='%s'"%(useremail,userpassword)
        # cur.execute(sql)
        # data=cur.fetchall()
        # db.commit()
        x=pd.read_sql_query(sql,db)
        count=x.values[0][0]

        if count==0:
            msg="user Credentials Are not valid"
            return render_template("login.html",name=msg)
        else:
            s="select * from user where Email='%s' and Password='%s'"%(useremail,userpassword)
            z=pd.read_sql_query(s,db)
            session['email']=useremail
            pno=str(z.values[0][4])
            name=str(z.values[0][1])
            session['pno']=pno
            session['name']=name
            return render_template("userhome.html",myname=name)
    return render_template('login.html')

@app.route('/registration',methods=["POST","GET"])
def registration():
    if request.method=='POST':
        username=request.form['username']
        useremail = request.form['useremail']
        userpassword = request.form['userpassword']
        conpassword = request.form['conpassword']
        Age = request.form['Age']
        
        contact = request.form['contact']
        if userpassword == conpassword:
            sql="select * from user where Email='%s' and Password='%s'"%(useremail,userpassword)
            cur.execute(sql)
            data=cur.fetchall()
            db.commit()
            
            if data==[]:
                sql = "insert into user(Name,Email,Password,Age,Mob)values(%s,%s,%s,%s,%s)"
                val=(username,useremail,userpassword,Age,contact)
                cur.execute(sql,val)
                db.commit()
                msg="Registered successfully","success"
                return render_template("login.html",msg=msg)
            else:
                msg="Details are invalid","warning"
                return render_template("registration.html",msg=msg)
        else:
            msg="Password doesn't match", "warning"
            return render_template("registration.html",msg=msg)
    return render_template('registration.html')


@app.route('/view data',methods = ["POST","GET"])
def view_data():
    df = pd.read_csv(r'dataset\YoutubeSpamMergedData.csv')
    df.head(2)
    return render_template('view data.html',col_name = df.columns,row_val = list(df.values.tolist()))



@app.route('/model',methods = ['GET',"POST"])
def model():
    if request.method == "POST":
        algo = request.form['algo']

        if algo == 'MultinomialNB':
            algorithm = 'Multinomial Naive Bayes'
            accuracy, precision, recall, f1_score = 91.33, 91.86, 91.33, 91.33

        elif algo == 'DecisionTree':
            algorithm = 'Decision Tree Classifier'
            accuracy, precision, recall, f1_score = 94, 94, 94, 93.99

        elif algo == 'AdaBoost':
            algorithm = 'AdaBoost Classifier'
            accuracy, precision, recall, f1_score = 88.66, 89.76, 88.66, 88.51

        elif algo == 'MLPClassifier':
            algorithm = 'MLP Classifier'
            accuracy, precision, recall, f1_score = 92.33, 92.36, 92.33, 92.32

        elif algo == 'SVC':
            algorithm = 'Support Vector Classifier'
            accuracy, precision, recall, f1_score = 95, 95.08, 95, 94.98

        elif algo == 'RandomForest':
            algorithm = 'Random Forest Classifier'
            accuracy, precision, recall, f1_score = 95, 95.03, 95, 94.99

        elif algo == 'ExtraTreesClassifier':
            algorithm = 'Extra Trees Classifier'
            accuracy, precision, recall, f1_score = 95.33, 95.33, 95.33, 95.33

        return render_template('model.html', algorithm = algorithm, accuracy = accuracy, precision = precision, recall = recall, f1_score = f1_score)
    return render_template('model.html')






from sklearn.feature_extraction.text import HashingVectorizer       
hvectorizer = HashingVectorizer(n_features=10000,norm=None,alternate_sign=False,stop_words='english') 

import pickle
with open(r"models\adaboost.sav", "rb") as file:
    model = pickle.load(file)

def prediction_func(input):
    def text_clean(CONTENT): 
        # changing to lower case
        lower = CONTENT.lower()
        
        # Replacing the repeating pattern of &#039;
        pattern_remove = lower.replace("&#039;", "")
        
        # Removing all the special Characters
        special_remove = pattern_remove.replace(r'[^\w\d\s]',' ')
        
        # Removing all the non ASCII characters
        ascii_remove = special_remove.replace(r'[^\x00-\x7F]+',' ')
        
        # Removing the leading and trailing Whitespaces
        whitespace_remove = ascii_remove.replace(r'^\s+|\s+?$','')
        
        # Replacing multiple Spaces with Single Space
        multiw_remove = whitespace_remove.replace(r'\s+',' ')
        
        # Replacing Two or more dots with one
        dataframe = multiw_remove.replace(r'\.{2,}', ' ')
        return dataframe

    cleaned_text = text_clean(input)
    result = model.predict(hvectorizer.transform([cleaned_text]))

    if result == 0:
        return "This is a Not Spam Comment"
    else:
        return "This is a Spam Comment"


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == "POST":
        text = request.form['text']
        result = prediction_func(text)

        return render_template('prediction.html', result = result)
    return render_template('prediction.html')


if __name__=="__main__":
    app.run(debug=True)