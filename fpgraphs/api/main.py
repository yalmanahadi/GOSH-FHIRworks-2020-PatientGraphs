from fhir_parser import FHIR
import plotly
import plotly.graph_objects as go
from datetime import datetime
import os
from plotly.subplots import make_subplots

fhir = FHIR()
patient = None
#ID = "8f789d0b-3145-4cf2-8504-13159edaa747"
ID = None
observation_types = ["BMI", "Bodyweight", ""]
SBP = [] #systolic
DBP = [] #diastolic
HR = [] #heart rate
BMI = [] #body mass index
W = [] #weight

def get_data(id):
    global ID, patient
    ID = id
    patient = fhir.get_patient(id)
    for observation in fhir.get_patient_observations(ID):
        for component in observation.components:
            if component.code == '8462-4':
                SBP.append((str(component.value), observation.effective_datetime))
            elif component.code == '8480-6':
                DBP.append((str(component.value), observation.effective_datetime))
            elif component.code == '8867-4':
                HR.append((str(component.value), observation.effective_datetime))
            elif component.code == '59576-9':
                BMI.append((str(component.value), observation.effective_datetime))
            elif component.code == '29463-7':
                W.append((str(component.value), observation.effective_datetime))
    sort_data()

def sort_data():
    SBP.sort(key=lambda x: x[1])
    DBP.sort(key=lambda x: x[1])
    HR.sort(key=lambda x: x[1])
    BMI.sort(key=lambda x: x[1])
    W.sort(key=lambda x: x[1])
                

def split_data(tupleList): # split data for graphing
    x = []
    y = []
    for item in tupleList:
        y.append(item[0])
        x.append(item[1])
    return x, y

def generate_graph(observation, tupleList, yaxis, xaxis):
    data = split_data(tupleList)
    fig = go.Figure(data=go.Scatter(x =data[0], y = data[1] ))
    fig.update_layout(
        title = fhir.get_patient(ID).full_name() + " (" + observation + ")",
        xaxis_title = xaxis,
        yaxis_title = yaxis
    )

    #plotly.offline.plot(fig, filename=os.path.join("App/api/webdocs/",  ID + '-' + observation + '.html'), auto_open=False)
    
    #fig.write_html("/api/webdocs/" + ID + '-' + observation + '.html', auto_open = True)

    return fig

def generate_graphs():
    patient_info_title = health_check()
    BMIdata = split_data(BMI)
    HRdata = split_data(HR)
    DBPdata = split_data(DBP)
    SBPdata = split_data(SBP)
    fig = make_subplots(
        rows=2, cols=2, subplot_titles=("Heart Rate", "BMI", "Systolic Blood Pressure", "Diastolic Blood Pressure")
    )

    # Add traces
    fig.add_trace(go.Scatter(x =HRdata[0], y = HRdata[1] ), row=1, col=1)
    fig.add_trace(go.Scatter(x =BMIdata[0], y = BMIdata[1] ), row=1, col=2)
    fig.add_trace(go.Scatter(x =SBPdata[0], y = SBPdata[1] ), row=2, col=1)
    fig.add_trace(go.Scatter(x =DBPdata[0], y = DBPdata[1] ), row=2, col=2)

    # Update xaxis properties
    fig.update_yaxes(title_text="Heart Rate (beats\m)", row=1, col=1)
    fig.update_yaxes(title_text="BMI Percentile Per Age and Gender (%)", row=1, col=2)
    fig.update_yaxes(title_text="Systolic Blood Pressure (mm[Hg])", row=2, col=1)
    fig.update_yaxes(title_text="Diastolic Blood Pressure (mm[Hg])", row=2, col=2)

    # Update yaxis properties
    fig.update_xaxes(title_text="Date of Observation", row=1, col=1)
    fig.update_xaxes(title_text="Date of Observation", row=1, col=2)
    fig.update_xaxes(title_text="Date of Observation", row=2, col=1)
    fig.update_xaxes(title_text="Date of Observation", row=2, col=2)

    # Update title and height
    fig.update_layout(title_text=fhir.get_patient(ID).full_name() + health_check() , height=700)
    return fig

def health_check():
    gender = patient.gender.lower()
    age = patient.age()
    result = ' - Data from latest observation: '
    latest_hr = float(HR[len(HR)-1][0])
    latest_dbp = float(DBP[len(DBP)-1][0])
    latest_sbp = float(DBP[len(DBP)-1][0])
    if latest_sbp in range(80,121):
        result += "SBP = Normal"
    elif latest_sbp > 120:
        result += "SBP = Above Normal"
    else:
        result += "SBP = Below Normal"
    
    if latest_dbp in range(60,81):
        result += ", DBP = Normal"
    elif latest_dbp > 81:
        result += ", DBP = Above Normal"
    else:
        result += ", DBP = Below Normal"
    if (age >= 10):
        if latest_hr in range(60,101):
            result += ", HR = Normal"
        elif latest_hr > 100:
            result += ", HR = Above Normal"
        else:
            result += ", HR = Below Normal"
    return result
    
   
def write_to_html(fig, path, filename):
    plotly.offline.plot(fig, filename=os.path.join(path, filename), auto_open=False)
    return "result.html" 

def create_bmi_graph(id):
    get_data(id)
    return generate_graph("BMI", BMI, yaxis="BMI Percentile Per Age and Gender (%)", xaxis ="Date of Observation")

def create_dbp_graph(id):
    get_data(id)
    return generate_graph("DBP", DBP, yaxis="Diastolic Blood Pressure (mm[Hg])", xaxis ="Date of Observation")

def create_sbp_graph(id):
    get_data(id)
    return generate_graph("SBP", SBP, yaxis="Systolic Blood Pressure (mm[Hg])", xaxis ="Date of Observation")

def create_hr_graph(id):
    get_data(id)
    return generate_graph("HR", HR, yaxis="Heart Rate (beats\m)", xaxis ="Date of Observation")

def create_all_graphs(id):
    get_data(id)
    return generate_graphs()