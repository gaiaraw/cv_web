from flask import render_template
from app import app

@app.route('/')
@app.route('/gaia')
def home():
    return render_template("gaia.html", name="gaïa")

@app.route('/formations')
def formations():
    return render_template('formations.html')

@app.route('/competences')
def competences():
    return render_template('competences.html')

@app.route('/experiences')
def experiences():
    return render_template('experiences.html')

@app.route('/job-etudiants')
def job_etudiants():
    return render_template('job_etudiants.html')
