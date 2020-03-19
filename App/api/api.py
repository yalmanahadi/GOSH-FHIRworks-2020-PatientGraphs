import os
import flask
from flask import request, jsonify, render_template
import sys
import main as m

app = flask.Flask(__name__, template_folder="webdocs")
app.config["DEBUG"] = True

@app.route('/BMI/id=<id>', methods=['GET'])
def getBMI(id):
    m.get_data(id)
    m.generate_graph("BMI", m.BMI, yaxis="BMI Percentile Per Age and Gender (%)", xaxis ="Date of Observation")
    return render_template('result.html')
    #return render_template( id + '-' + "BMI" + '.html')

@app.route('/DBP/id=<id>', methods=['GET'])
def getDBP(id):
    m.get_data(id)
    m.generate_graph("DBP", m.DBP, yaxis="Diastolic Blood Pressure (mm[Hg])", xaxis ="Date of Observation")
    return render_template('result.html')
    #return render_template( id + '-' + "DBP" + '.html')

@app.route('/SBP/id=<id>', methods=['GET'])
def getSBP(id):
    m.get_data(id)
    m.generate_graph("SBP", m.SBP, yaxis="Systolic Blood Pressure (mm[Hg])", xaxis ="Date of Observation")
    return render_template('result.html')
    #return render_template( id + '-' + "SBP" + '.html')

@app.route('/HR/id=<id>', methods=['GET'])
def getHR(id):
    m.get_data(id)
    m.generate_graph("HR", m.HR, yaxis="Heart Rate (beats\m)", xaxis ="Date of Observation")
    return render_template('result.html')
    # return render_template(' id + '-' + "HR" + ''.html')

@app.route('/id=<id>', methods=['GET'])
def getGraphs(id):
    m.get_data(id)
    m.generate_graphs()
    return render_template('result.html')
    #return render_template('result.html')
    # return render_template(' id + '-' + "HR" + ''.html')

app.run(port=9999)