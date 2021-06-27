from flask import Flask, render_template,jsonify,request
import random
import json


app = Flask(__name__)


#APIs
@app.route("/api/sendotp",methods=["POST","GET"])
def sendotp():
    print(request.args.get('mobnum'))
    payload = {
        'channel':'sms',
        'source':'918178812482',
        'destination':'918178812482',
        'message':{"type":"text","text":"Hi"}
    }
    url = "https://api.gupshup.io/sm/api/v1/msg"
    
    return "gotit"

@app.route("/profile",methods=['POST','GET'])
def profile():
    return render_template('profile.html',username="Sahil Jena",mobnum="+91 8178812482",userid="9888 7647 7776",qrsrc="Epmty",limit="4")

@app.route("/",methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route("/verify",methods=['POST','GET'])
def verifyotp():
    return render_template('verifyotp.html')

@app.route("/updateprofile",methods=['POST','GET'])
def updtprofile():
    return render_template('updtprofile.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    
