from flask import Flask, jsonify, render_template, request
import numpy as np
import pandas as pd
import sklearn as sk
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import train_test_split
import sqlite3
from textblob import TextBlob
import module as md

'''customer = ''
arrR = {}
id ='''''
M = md.data()
app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def root():
    return render_template('base.html')


@app.route('/disp', methods=['GET','POST'])
def disp():
    return render_template('base.html')


@app.route('/customer', methods=['GET','POST'])
def customer():
    return render_template('customer_base.html')


@app.route('/cust_login', methods=['GET','POST'])
def cust_login():
    return render_template('login.html')


@app.route('/cust_signup', methods=['GET','POST'])
def cust_signup():
    return render_template('signup.html')


@app.route('/admin', methods=['GET','POST'])
def admin():
    return render_template('admin_login.html')


@app.route('/admin_login', methods=['GET','POST'])
def admin_login():
    username = request.form.get('id')
    password = request.form.get('pass')
    if username == 'admin' and password == 'admin':
        return render_template('admin_menu.html')
    return render_template('admin_login.html', prediction_text=0)


@app.route('/login', methods=['GET','POST'])
def login():
    W = md.credentials()
    username = request.form.get('id')
    #customer = username
    M.set_customer(username)
    password = request.form.get('pass')
    if W.login(username, password):
        return render_template('cust_menu.html')
    return render_template('login.html', prediction_text=0)


@app.route('/menu_disp', methods=['GET','POST'])
def menu_disp():
    return render_template('cust_menu.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    W = md.credentials()
    username = request.form.get('id')
    password = request.form.get('pass')
    email = request.form.get('email')
    if W.signup(username, password, email):
        return render_template('login.html', prediction_text=1)
    return render_template('signup.html', prediction_text=0)


# --- Customer Conrols ---
@app.route('/review_product', methods=['GET','POST'])
def review_product():
    W = md.products()
    data = W.get_products()
    arrD = data.to_dict('list')
    #arrR = arrD
    M.set_dict(arrD)
    return render_template('review_product.html', len = len(arrD['name']), prod = arrD)


@app.route('/review', methods=['GET','POST'])
def review():
    return render_template('index.html')


@app.route('/cust_menu', methods=['GET','POST'])
def cust_menu():
    return render_template('cust_menu.html')


@app.route('/cust_review_delete', methods=['GET','POST'])
def cust_review_delete():
    W = md.reviews()
    data = W.get_review_name(M.customer)
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('customer_reviews.html', len=len(arrD['name']), prod=arrD, pre=1)


@app.route('/cust_review', methods=['GET','POST'])
def cust_review():
    W = md.reviews()
    data = W.get_review_name(M.customer)
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('customer_reviews.html', len=len(arrD['name']), prod=arrD)


@app.route('/delete_review_cust', methods=['GET','POST'])
def delete_review_cust():
    W = md.reviews()
    data = W.get_review_name(M.customer)
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('customer_reviews.html', len=len(arrD['name']), prod=arrD, pre=1)


@app.route('/delete_review_index/<string:id>', methods=['GET','POST'])
def delete_review_index(id):
    RS = md.reviews()
    RS.delete_review(id)

    W = md.reviews()
    data = W.get_review_name(M.customer)
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('customer_reviews.html', len=len(arrD['name']), prod=arrD, pre=1, pro=1)


@app.route('/review_index/<string:id>', methods=['GET','POST'])
def review_index(id):
    '''id = request.form.get('id')
    print(id)'''
    M.set_id(str(id))
    return render_template('index.html')


# --- Admin Conrols ---
@app.route('/add_product', methods=['GET','POST'])
def add_product():
    return render_template('add_product.html')


@app.route('/admin_menu', methods=['GET','POST'])
def admin_menu():
    return render_template('admin_menu.html')


@app.route('/add_product_dao', methods=['GET','POST'])
def add_product_dao():
    W = md.products()
    name = request.form.get('name')
    price = request.form.get('price')
    description = request.form.get('product_info')
    if W.add_product(name, price, description):
        return render_template('add_product.html', prediction_text=1)
    return render_template('add_product.html', prediction_text=0)


@app.route('/delete_product', methods=['GET','POST'])
def delete_product():
    W = md.products()
    data = W.get_products()
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('product_moniter.html', len=len(arrD['name']), prod=arrD)


@app.route('/delete_product_item/<string:id>', methods=['GET','POST'])
def delete_product_item(id):
    RS = md.products()
    RS.delete_item(id)

    W = md.products()
    data = W.get_products()
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('product_moniter.html', len=len(arrD['name']), prod=arrD, pro=1)


@app.route('/delete_fake', methods=['GET','POST'])
def delete_fake():
    RS = md.reviews()
    RS.delete_fake()

    W = md.reviews()
    data = W.get_review()
    arrD = data.to_dict('list')
    M.set_dict(arrD)
    return render_template('review_moniter.html', len=len(arrD['name']), prod=arrD, pro=1)


@app.route('/moniter_review', methods=['GET','POST'])
def moniter_review():
    W = md.reviews()
    data = W.get_review()
    arrD = data.to_dict('list')
    #arrR = arrD
    M.set_dict(arrD)
    return render_template('review_moniter.html', len=len(arrD['name']), prod=arrD)


@app.route('/predict', methods=['GET','POST'])
def predict():
    df = pd.read_csv('deceptive-opinion.csv')
    df1 = df[['deceptive', 'text']]
    df1.loc[df1['deceptive'] == 'deceptive', 'deceptive'] = 0
    df1.loc[df1['deceptive'] == 'truthful', 'deceptive'] = 1
    X = df1['text']
    Y = np.asarray(df1['deceptive'], dtype = int)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,random_state=109)
    cv = CountVectorizer()
    x = cv.fit_transform(X_train)
    y = cv.transform(X_test)
    message = request.form.get('enteredinfo')
    data = [message]
    vect = cv.transform(data).toarray()
    pred = model.predict(vect)

    W = md.reviews()
    check = 'Fake' if pred == 0 else 'Genuine'
    R = TextBlob(message)
    a = R.sentiment.polarity
    rate = round(abs(a), 2)*10
    W.save_review(M.customer, M.id, check, rate, message)
    return render_template('index.html', insert=1)

    
if __name__ == '__main__':
    app.run(debug=True)