# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:16:20 2021

@author: naved
"""
from flask import Flask, request, jsonify
import conceptnett
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = conceptnett.returndic()
#     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)
 
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()