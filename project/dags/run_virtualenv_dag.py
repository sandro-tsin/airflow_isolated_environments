"""
The example of using the @task.virtualenv decorator that creates a new 
virtual environment each time the task runs using Python version 
as Airflow environment 
"""

from airflow.decorators import dag, task
from datetime import datetime

@dag(schedule=None, start_date=datetime(2024, 1, 1), catchup=False)

def run_virtualenv_dag():

    @task.virtualenv(
    requirements=["numpy==1.24.4"]
    )
    def virtualenv_task():
        import numpy
        print('numpy version:', numpy.__version__)
        return numpy.random.randint(100)

    virtualenv_task()

run_virtualenv_dag()