
# Simple Bug Tracker 

A simple implementation of a minimally featured bug tracker utilising *SQLite*, *FastAPI*, and *Streamlit*.

Features include;

* View a list of open bugs :thumbsup:

* View details of individual bugs :thumbsup:

* Create new bugs :thumbsup:

* Update existing bugs :thumbsup:

* Close bugs :thumbsup:

* Assign bugs to users :thumbsup:

* Add new users :thumbsup:

* Update users :thumbsup:

## Usage

The preferred usage method is to utilise docker, though details of how to start the API and web UI manually are described below. All commands should be executed from the root directory of the project.

### Docker

To build the containers:

```
docker compose build --no-cache
```

To start and attach the containers;

```
docker compose up
```


### Manual 

The project should be compatible with most linux distributions; developed on kubuntu 22.10.

Install dependencies;
```
pip install -r requirements.txt
```

Start the API;
```
uvicorn api:app --host 0.0.0.0 --port 8000
```

Start the web app;
```
streamlit run app/Home.py  --server.port 8010 
```

***IMPORTANT*** The web UI will run, but will NOT function correctly outside of the docker setup described in this README.


## Using the API

Once started, the API documentation can be accessed at [localhost:8080/docs](localhost:8080/docs).

## Using the web app

Once started, the web app can be accessed at [localhost:8010](localhost:8010).

The applications initialise with a fresh database and as such do not contain records of any users or bugs. Users are encouraged to add both using either the API endpoints or the web app.

Please note that as a bug must be associated with a user, at least one user must be created before a bug can be created.

## Limitations

The project currently provides a minimum viable product able to fit the brief, whilst realising a short development time. A number of considerations and improvements could be implemented were the project to be taken forward.

* The streamlit framework is particularly suited to fast prototyping, hence it being chosen, but django may provide a more scalable and powerful choice. However, deployment with docker and kubernetes may be sufficient to mitigate this.

* SQLite was chosen as the database due to my familiarity with it. The asynchronous functionality of SQLite is less mature than some other options and a production version could consider utilising POSTGres or MongoDB.

* Due to time constraints asynchronous functionality is not properly implemented.

* User authentication, and additional data fields would typically be included in a fully featured bug tracker, as well as the ability to delete bugs and users. This functionality was not included due to the time limited nature of the project and it not being expressed as a requirement.

* Included tests ensure the core functionality, but would be developed into a more comprehensive suite of tests were the project developed further. In particular, integration tests would be an important consideration.

* Input validation is only focused on type, for example it is possible to create records with blank data fields. With additional time full input validation, including testing for duplicates would be added.

* Logging is implemented for the API but time limitations prevented expansion to the web UI. Further development would expand the logging functionality.

* The database file `api_db.db` (if present) must be removed before running tests. 