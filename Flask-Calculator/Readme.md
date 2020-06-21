# Calculator App

The application is built in flask and written in python.

The application will take 2 number (int or float) and can add, subtract, multiply and divide.
The history of all the operations made are also stored and can be fetched using api endpoints 

## To  run the application

You must have Python and pip installed in your system.
Click [here](https://www.python.org/downloads/) to install.

1. Install flask 
```python
pip install Flask
```

2. Run the application

Navigate to directory with `app.py` 

**For Mac**
```python
$ export FLASK_APP=app.py
$ python -m flask run
```

**For Windows**
```python
set FLASK_APP=app.py
python -m flask run
```

On successfull execution of above commands you see this

```
 * Environment: development 
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The server will run on <http://127.0.0.1:5000/>. Below are the REST API endpoints  

`GET /calculator`   - Home page  
`POST /calculator`  - The API will evaluate your inputs  
`GET /history`      - Shows all the operations in tabular format  
`GET /api/history`  - Returns JSON object of all the operations   

