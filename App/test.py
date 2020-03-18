##from fhir_parser import FHIR
##
####import plotly.graph_objects as go
####fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
####fig.write_html('first_figure.html', auto_open=True)
##
##fhir = FHIR()
##
##pid = "8f789d0b-3145-4cf2-8504-13159edaa747"
##patient = fhir.get_patient(pid)
##
##observation = fhir.get_observation("4a064229-2a40-45f4-a259-f4eedcfd525a")
##
##print(patient.full_name())
##
##print(patient.marital_status)
##
##for i in observation.components:
##    print(i)
##
##for i in patient.telecoms:
##    print(i)
##
##for i in patient.addresses:
##    print(i)
##

##import matplotlib.pyplot as plt
##from fhir_parser import FHIR
##
##fhir = FHIR()
##patients = fhir.get_all_patients()
##observations = []
##
##for patient in patients:
##    try:
##        for observation in fhir.get_patient_observations(patient.uuid):
##            for component in observation.components:
##                print(component)
##                if component.code == '8462-4' or component.code == '8480-6':
##                    observations.append(str(component))
##    except:
##        continue
##    break
##        

from fhir_parser import FHIR

fhir = FHIR()
patient = fhir.get_all_patients()
#"8f789d0b-3145-4cf2-8504-13159edaa747"
print(patient[0].uuid)
observations = []

for observation in fhir.get_patient_observations(patient[0].uuid):
    for component in observation.components:
        print(component)
        if component.code == '8462-4' or component.code == '8480-6':
            observations.append(str(component))

print(observations)
    

