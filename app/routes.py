#import certain functions into the global
#namespace
from app import app
from markdown import markdown
from flask import render_template, render_template_string, request, session
from app.blog_helpers import render_markdown

#safe global import (okay to use)
import flask
import os 


app.secret_key = b'M\xb6NP!YC\x19\x14\xc9\xf09\xab\x1az\x08'

#global import (try to avoid)
#from flask import *

#home page
@app.route("/")
def home():
    return render_markdown('index.md')

@app.route('/all')
def all():
    #TODO: figure out how to find all files 
    #in the app
    
    view_data = {}
    view_data["pages"] = os.listdir(r"C:\Users\njl27\Desktop\bin\Flaskblogv1\flaskblogv2\app\templates")
    return render_template("all.html", data = view_data)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        
        #TODO: process request.values as necessary
        session['user_name'] = request.values['user_name']
    return render_template("login.html")


@app.route("/favicon.ico")
def favicon():
    return ""

@app.route("/click_tracker", methods=['GET', 'POST'])
def click_tracker():
    view_data = {}
    view_data["click_count"] = 0
    if request.method == 'POST':
        view_data["click_count"] = request.values["click_count"]
        view_data["click_count"] = int(view_data["click_count"]) + 1
    return render_template('click_tracker.html', data=view_data)
    
@app.route("/edit/<page_name>", methods=['GET', 'POST'])
def edit_page(page_name):
    view_data = {}
    view_data["page_name"] = page_name
    return render_template("edit.html", data = view_data)

#generic page
@app.route("/<view_name>")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.md')
    view_data = {} #create empty dictionary
    return render_template_string(html, view_data = session)


