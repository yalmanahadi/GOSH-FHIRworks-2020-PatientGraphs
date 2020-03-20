import os
import flask
from flask import request, render_template
import sys
from main import *

app = flask.Flask(__name__, template_folder="webdocs")
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<asdf"

@app.route('/BMI/id=<id>', methods=['GET'])
def getBMI(id):
    graph = create_bmi_graph(id)
    htmlPath = write_to_html(graph, "fpgraphs/api/webdocs" , "result.html")
    return render_template(htmlPath)
    #return render_template( id + '-' + "BMI" + '.html')

@app.route('/DBP/id=<id>', methods=['GET'])
def getDBP(id):
    graph = create_dbp_graph(id)
    htmlPath = write_to_html(graph, "fpgraphs/api/webdocs" , "result.html")
    return render_template(htmlPath)
    #return render_template( id + '-' + "DBP" + '.html')

@app.route('/SBP/id=<id>', methods=['GET'])
def getSBP(id):
    graph = create_sbp_graph(id)
    htmlPath = write_to_html(graph, "fpgraphs/api/webdocs" , "result.html")
    return render_template(htmlPath)
    #return render_template( id + '-' + "SBP" + '.html')

@app.route('/HR/id=<id>', methods=['GET'])
def getHR(id):
    graph = create_hr_graph(id)
    htmlPath = write_to_html(graph, "fpgraphs/api/webdocs" , "result.html")
    return render_template(htmlPath)
    # return render_template(' id + '-' + "HR" + ''.html')

@app.route('/id=<id>', methods=['GET'])
def getGraphs(id):
    graph = create_all_graphs(id)
    htmlPath = write_to_html(graph, "fpgraphs/api/webdocs" , "result.html")
    return render_template(htmlPath)
    #return render_template('result.html')
    # return render_template(' id + '-' + "HR" + ''.html')

app.run(port=9999)