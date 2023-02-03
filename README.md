
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

## Installation

Preferred usage is with docker. 

### Manual 
The project should be compatible with most linux distributions, tested on kubuntu 22.10.

From the project root; 

*Install dependencies*
```
$ pip install -r requirements.txt
```

### Docker

The API;
```
$ docker build --no-cache -t bugtrackerapi -f api/Dockerfile .
```

The web app;
```
$ docker build --no-cache -t bugtrackerapp -f app/Dockerfile .
```

Create a network bridge to allow communication between the containers;
```
docker network create bugtracker-bridge
```

## Starting the API

### Manual

From the root folder of the project:
```
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Docker

```
$ docker run -it --rm --net bugtracker-bridge -p 8000:8000 -e SERVER_HOST=0.0.0.0 -e SERVER_PORT=8000 --name bugtrackerapi bugtrackerapi:latest
```

## Starting the web app

### Manual

From the root folder of the project:
```
streamlit run app/Home.py  --server.port 8010 
```

### Docker

```
$ docker run -it --rm --net bugtracker-bridge -p 8010:8010 -e SERVER_HOST=0.0.0.0 -e SERVER_PORT=8010 --name bugtrackerapp bugtrackerapp:latest
```

## Using the API

Once started, the API documentation can be accessed at [localhost:8080/docs](localhost:8080/docs).

## Using the web app

Once started, the web app can be accessed at [localhost:8010](localhost:8010).

## Limitations

The project currently provides a minimum viable product able to fit the brief, whilst realising a short development time. A number of considerations and improvements could be implemented were the project to be taken forward.

* The streamlit framework is particularly suited to fast prototyping, hence it being chosen, but django may provide a more scalable and powerful choice. However, deployment with docker and kubernetes may be sufficient to mitigate this.

* SQLite was chosen as the database due to my familiarity with it. The asynchronous functionality of SQLite is less mature than some other options and a production version could consider utilising POSTGres or MongoDB.

* Due to time constraints asynchronous functionality is not properly implemented.

* User authentication, and additional data fields would typically be included in a fully featured bug tracker, as well as the ability to delete bugs and users. This functionality was not included due to the time limited nature of the project and it not being expressed as a requirement.

* Included tests ensure the core functionality, but would be developed into a more comprehensive suite of tests were the project developed further. In particular, integration tests would be an important consideration.