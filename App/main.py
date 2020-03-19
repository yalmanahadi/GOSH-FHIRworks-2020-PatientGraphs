from fhir_parser import FHIR
import plotly.graph_objects as go
from datetime import datetime


fhir = FHIR()
patient = fhir.get_all_patients()
ID = "8f789d0b-3145-4cf2-8504-13159edaa747"
systolic_observations = []
diastolic_observations = []
heartrate_observations = []
BMI = []
weight_observations = []


def get_data(ID):
    global systolic_observations, diastolic_observations
    for observation in fhir.get_patient_observations(ID):
        for component in observation.components:
            if component.code == '8462-4':
                systolic_observations.append((str(component.value), observation.effective_datetime))
            elif component.code == '8480-6':
                diastolic_observations.append((str(component.value), observation.effective_datetime))
            elif component.code == '8867-4':
                heartrate_observations.append((str(component.value), observation.effective_datetime))
            elif component.code == '59576-9':
                BMI.append((str(component.value), observation.effective_datetime))
            elif component.code == '29463-7':
                weight_observations.append((str(component.value), observation.effective_datetime))
    BMI.sort(key=lambda x: x[1])
    systolic_observations.sort(key=lambda x: x[1])
    diastolic_observations.sort(key=lambda x: x[1])
    heartrate_observations.sort(key=lambda x: x[1])
    print(BMI)
                  

get_data(ID)

def split_data(tupleList):
    x = []
    y = []
    for item in tupleList:
        y.append(item[0])
        x.append(item[1])
    return x, y

def generate_graph(observation, tupleList):
    data = split_data(tupleList)
    fig = go.Figure(data=go.Line(x =data[0], y = data[1] ))
    fig.update_layout(title = fhir.get_patient(ID).full_name() + " (" + observation + ")")
    fig.write_html(ID + '-' + observation + '.html', auto_open = True)

generate_graph("BMI", BMI)