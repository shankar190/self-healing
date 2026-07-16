from flask import Flask,request
import subprocess

app=Flask(__name__)

@app.route("/",methods=["POST"])

def alert():

    subprocess.call("./alert.sh")

    return "Recovered"

app.run(host="0.0.0.0",port=5001)
