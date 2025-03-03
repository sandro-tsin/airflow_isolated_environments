"""
The example of using the @task.external_python decorator which 
runs a Python function in an existing virtual Python environment, 
isolated from your Airflow environment.
"""

from airflow.decorators import dag, task
from datetime import datetime

VENV_PYTHON_PATH = "/home/airflow/.pyenv/versions/3.12.0/envs/great_expectation_env/bin/python"

@dag(schedule=None, start_date=datetime(2024, 1, 1), catchup=False)

def run_external_python_dag():

    @task.external_python(python=VENV_PYTHON_PATH)
    def external_python_task():
        import great_expectations as gx
        
        print('gx version:', gx.__version__)
        gx_context = gx.get_context(mode="file")
        return(str(gx_context))

    @task() 
    def print_xcom(run_great_expectations_res):
        print(run_great_expectations_res)

    print_xcom(external_python_task()) 

run_external_python_dag()