from app import app
from flask import Flask, render_template, url_for

@app.route('/class8cbse_Social_and_Political_Life')
def class8cbse_Social_and_Political_Life():
    return render_template('cbse/8th/Social_and_Political_Life.html')

@app.route('/class8cbse_science')
def class8cbse_science():
    return render_template('cbse/8th/science.html')

@app.route('/class8cbse_resource_and_development')
def class8cbse_resource_and_development():
    return render_template('cbse/8th/resource_and_development.html')

@app.route('/class8cbse_maths')
def class8cbse_maths():
    return render_template('cbse/8th/maths.html')

@app.route('/class8cbse_history')
def class8cbse_history():
    return render_template('cbse/8th/history.html')

@app.route('/class8cbse_english-it-so-happened')
def class8cbse_english-it-so-happened():
    return render_template('cbse/8th/english-it-so-happened.html')

@app.route('/class8cbse_english-honey-dew')
def class8cbse_english-honey-dew():
    return render_template('cbse/8th/english-honey-dew.html')
