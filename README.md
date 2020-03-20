# GOSH-FHIRworks-2020-PatientGraphs
A package that allows you to search for a patient from the FHIR records (using thier patient id) and display some data about their observations on graphs (currently Heart Rate, Systolic Blood Pressure, Diastolic Blood Pressure, and BMI)

This visual representation can be used to track the progress of a patient on a medicine prescribed for improvement of blood pressure for example. 

This project has been packaged so it can be installed with:
pip install . 

It can then be imported with:
from fpgraphs.api import main

The functions of main and thier use are listed below:
1. get_data(id) retrieves systolic bp, diastolic bp, heartrate, and bmi observations, all sorted by the effective date of observation
2. generate_(observation, tupleList, yaxis, xaxis) generates a graph from the tuple-list of any observaton type and its value e.g. [(bmiValue1, observationDate1), (bmiValue2, observationDate2)]
3. generate_graphs() generates all the above mentioned graphs in a single figure
4. write_to_html(fig, path, fileName) takes a plotly figure, a path and a file name and writes the figure to the given path with the given file name (must be a .html)

------------------------------------------------------------------------------------

In order to run this project, the requirements must be installed with:
pip install -r requirements.txt

Running the api.py file starts a local host at port 9999

These are the endpoints to get observation data about a patient:

1. localhost:9999/BMI/<patient ID> (graph for the recorded BMI)
2. localhost:9999/HR/<patient ID> (graph for the recorded heart rates)
3. localhost:9999/SBP/<patient ID> (graph for the recorded systolic blood pressure)
4. localhost:9999/DBP/<patient ID> (graph for the recorded diastolic blood pressure)
5. localhost:9999/<patient ID> (All the above graphs on a single page)
