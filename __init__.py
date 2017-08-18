#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:12:49 2017

@author: mayur
"""

from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(debug=True)