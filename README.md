# thebeerhub-api

Simple Python Flask web API for storing data in Postgres

### TODOs:
- deployment, github action?

### local development:
*activate venv*  
``"$ . venv/bin/activate"
 or "venv\Scripts\activate"``

*install dependencies*  
``pip install -r requirements.txt``

*setup postgres+adminer:*  
```docker-compose up```

*run*  
``python manage.py run``


#### extra steps

*set ENV db url*  
``DATABASE_URL=postgresql://devuser:devpassword@localhost:5432/brews``


*windows psycopg2 postgres database adapter fix (yikes - install prebuilt binaries for windows)*  
``pip install pipwin ``  
``pipwin install psycopg2``  
``pip uninstall pipwin`` (optional)

### db migrations
`` python manage.py db init``  
`` python manage.py db migrate -m "initial database migration"``  
`` python manage.py db upgrade`` 

### docker build:
``docker build -t emilmadsen/thebeerhub-api:0.0.1 .``  
``docker push emilmadsen/thebeerhub-api:0.0.1``  

(arm for rpi)  
``docker build -t emilmadsen/thebeerhub-api:rpi -f DockerfileRPI .`` 

### docker run:
(run standalone - uses sqlite)  
``docker run -p 5000:5000 emilmadsen/thebeerhub-api:0.0.1``

(connects to postgres from docker-compose network)  
``docker run -p 5000:5000 --net thebeerhub-api_brew-net -e DATABASE_URL=postgresql://devuser:devpassword@db/brews emilmadsen/thebeerhub-api:0.0.1``


