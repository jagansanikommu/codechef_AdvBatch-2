from flask import Flask, render_template, request, redirect, url_for,send_from_directory
import os
from models import create_post,get_posts,clear_data,get_data,update_data

app=Flask(__name__)

user={"jagan":"123456"}

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/notepad',methods={"GET","POST"})
def notepad():
    if request.method == 'GET':
            pass
    if request.form.get("btn")=="Submit":
        if request.method == 'POST':
            if request.form.get('name')=="725":
                post = request.form.get('post')
                create_post(post)
    if request.form.get("btn")=="Clear":
        if request.method == 'POST':
            print("hi")
            if request.form.get('name')=="725":
                clear_data()
    posts = get_posts()
    return render_template('notepad.html',posts=posts)


@app.route('/codechef',methods={"GET","POST"})
def codechef():
    error = None
    data= []
    passcode = "7jagan25"
    if request.form.get("btn")=="Show":
        if request.method == 'POST':
            if request.form.get('batch')!="1":
                batch = request.form.get("batch")
                data = get_data(batch)

    if request.form.get("btn")=="Update":
        if request.method == 'POST':
            if request.form.get("passcode")  != passcode:
                error="Invalid Credentials"
            else:
                if request.form.get('batch')!="1":
                    batch = request.form.get("batch")
                    query="Updation takes 1.4 minutes⏳"
                    query=update_data(batch)
                    return render_template("Success.html",query=query)
                else:
                    error="Select Batch to Update!"
                    return render_template('codechef.html', error=error,data=data)            
    return render_template('codechef.html', error=error,data=data)


@app.route('/codechef_data',methods={"GET","POST"})
def codechef_data():
    error=None
    data= []
    if request.form.get("btn")=="Show":
        if request.method == 'POST':
            if request.form.get('batch')!="1":
                batch = request.form.get("batch")
                data = get_data(batch)
            else:
                error="Select Batch to Show Data!"     
    return render_template('codechef_data.html', error=error,data=data)



@app.route('/login',methods={"GET","POST"})
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in user or request.form['password'] != user[request.form['username']]:
            error="Invalid Credentials"
        else:
            details="Hello! "+request.form['username']
            return render_template("Success.html",details=details)
    return render_template('login.html', error=error)




if __name__=="__main__":
    app.run(debug=True)