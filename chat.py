from extract_info import *
import prompts, random
from flask import Flask, render_template, jsonify, request, session

app = Flask("__name__")

app.config['SECRET_KEY'] = 'the random string'    


@app.route("/", methods=['get','post'])
def home():    
    return render_template("index.html")

@app.route("/bot", methods=['get','post'])
def chat():    
    prompt = request.args.get("msg")
    response = get_bot_response(prompt)
    return response

def get_bot_response(prompt):    

    name, age, location, insurance_product = extract_info(prompt)
    if insurance_product != None:   
            session["insurance_product"] = insurance_product
    if age != None:
            session["age"] = age 
    if name != None:
            session["name"] = name
    if location != None:
            session["location"] = location

    if insurance_product == None and session.get("insurance_product") == None:
        return random.choice(prompts.get_product)
    else:
        if insurance_product != None:   
            session["insurance_product"] = insurance_product
    if age == None and session.get("age") == None:
        return random.choice(prompts.get_age)
    else:
        if age != None:
            session["age"] = age 
    if name == None and session.get("name") == None:
        return random.choice(prompts.get_name)
    else:
        if name != None:
            session["name"] = name

    if location == None and session.get("location") == None:
        return random.choice(prompts.get_location)
    else:
        if location != None:
            session["location"] = location
    response = "we have noted following information. Name " + session.get("name")
    response = response + ',age ' + str(session.get("age"))
    response = response + ',product ' + session.get("insurance_product")
    response = response + ',location ' + session.get("location")
    session.clear()
    return response 

if __name__ == '__main__':
   app.run()