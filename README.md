# Runing Airflow tasks in isolated environment example

Repository contains example of running DAGs with @task.external_python and @task.virtualenv decorators 
that allow you to run a tasks with different dependencies than your Airflow environment.

To run @task.external_python, separate Python environment needs to be craeted using '[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)'. Check Dockerfile to find out how this can be done. 

## Build and run

Run the following command to test project: `docker-compose up -d --build`.

## DAGs

### run_external_python_dag

This DAG is using the @task.external_python decorator to runs a Python function in an existing virtual Python environment 
named 'isolated_vertial_env' with path: "/home/airflow/.pyenv/versions/3.12.0/envs/great_expectation_env/bin/python". Task 'print_xcom' shows that result of such functions can be used further. 

### run_virtualenv_dag

This DAG is using @task.virtualenv decorator, it creates new virtual enviroment each time and installs packages provided in 'requirements' argument, so no need of preinstalled environment. 