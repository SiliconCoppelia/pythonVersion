from flask import Flask, render_template, send_from_directory, request, jsonify

import json

app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route('/')
def home():
    return render_template('new_qa_ui.html')

app.run(debug=True, host="0.0.0.0",port=8080)