from setuptools import setup

setup(name='FHIRPatientGraphs',
      version='0.1',
      install_requires=['plotly', 'fhir_parser==0.1.5', 'datetime'],
      description='Graphing some data about patients using thier ID',
      url='https://github.com/yalmanahadi/GOSH-FHIRworks-2020-PatientGraphs',
      author='Yalman Ahadi',
      author_email='zcabyah@ucl.ac.uk',
      license='MIT',
      packages=['fpgraphs'],
      zip_safe=False)
