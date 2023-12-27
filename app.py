from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import json
import os
import glob

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# Topページ
# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quiz_reception')
def quiz_reception():
    return render_template("quiz_reception.html")



if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)