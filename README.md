# Project setup

### Prerequisite
- Python 3.6 should be installed

### Steps for setting up the project environment
- Copy the project into a directory
- Install pipenv
    ```
        $ pip install pipenv
    ```
- change to project directory
    ```
        $ cd <project_path>/find_elapsed_time
    ```
- Install and create virutal environment using pipenv
    ```
        $ pipenv install
    ```
- Activate virtual environment
    ```
        $ pipenv shell
    ```
- Install experiments python package
    ```
        $ python setup.py install
    ```
### Run the code with argument
- Run the code with argument -ed (experiment dates) test date string value 
    ```
        $ experiments_elapsed_time -ed "02/06/1983 - 22/06/1983"
    ```
- Run the code with argument -f (file path) which contains list of test date values
    ```
        $ experiments_elapsed_time -f <project_path>/find_elapsed_time/experiments/exp_date_test_data.txt
    ```
### Run unit test
- Run unit test of the project
    ```
        $ pytest -v
    ```
