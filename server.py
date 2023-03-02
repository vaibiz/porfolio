from flask import Flask, render_template, url_for, request, redirect

import csv

app = Flask(__name__)

@app.route("/")
def my_home1():
    return render_template('index.html')

 # @app.route('/<string:page_name>')
 # def html_page(page_name):
 #    return render_template(page_name)

@app.route("/strategic.html")
def strategic1():
   return render_template('strategic.html')

@app.route("/python.html")
def python1():
   return render_template('python.html')

@app.route("/about.html")
def about1():
   return render_template('about.html')

@app.route("/contact.html")
def contact1():
   return render_template('contact.html')

@app.route("/index.html")
def my_home2():
    return render_template('index.html')

@app.route("/work.html")
def works2():
   return render_template('work.html')

@app.route("/soon.html")
def soon1():
   return render_template('soon.html')


@app.route("/thanks.html")
def thanks1():
   return render_template('thanks.html')


def write_to_csv (data):
    with open ('database.csv', mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        messsage=data["messsage"]
        csv_writer=csv.writer(database2, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,messsage])


@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect ('/thanks.html')
    else:
        return "something wrong"

