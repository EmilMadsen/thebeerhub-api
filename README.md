#thebeerhub-api

Simple Python Flask web API for storing data in Postgres

#### TODOs:  
- dockerize
- tests
- deployment, github action?

#### local development:
*activate venv*  
``"$ . venv/bin/activate"
 or "venv\Scripts\activate"``

*install dependencies*  
``pip install -r requirements.txt``

*windows psycopg2 postgres database adapter fix (yikes - install prebuilt binaries for windows)*  
``pip install pipwin ``  
``pipwin install psycopg2``  
``pip uninstall pipwin`` (optional)

*setup postgres+adminer:*  
```docker-compose up```

*apply db migrations:*  
`` python manage.py db init``  
`` python manage.py db migrate -m "initial database migration"``  
`` python manage.py db upgrade`` 

*run*  
``python manage.py run``

#### build?:

#### deployment?: