# FSND: Capstone Project
 Heroku Url : **_https://mycastingagency.herokuapp.com/**

<a name="motivation"></a>
## Motivations

1. The challenge or motivation to use all of the concepts and the skills taught in the other previous courses in the fullstack nanodegree in order to build an API from start to finish and host it


2. Concepts and the skills :
    Coding in Python 3
    Relational Database Architecture
    Modeling Data Objects with SQLAlchemy
    Internet Protocols and Communication
    Developing a Flask API
    Authentication and Access
    Authentication with Auth0
    Authentication in Flask
    Role-Based Access Control (RBAC)
    Testing Flask Applications
    Deploying Applications

3. Deployment of application using Heroku
    Heroku is a cloud platform where developers host applications, databases and other services in several languages including Ruby, Java, Node.js, Scala, Clojure, Python, PHP, and Go. Developers use Heroku to deploy, manage, and scale applications

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup
Ensure Postgres is run in the backend. Create a database to use, which is to be filled into the .env file. When running using Heroku ensure a postgres database is set up.

```bash
$ heroku addons:create heroku-postgresql:hobby-dev --app [my-app-name]
$ heroku config --app [my-app-name] # eg DATABASE_URL:
# postgres://xjlhouchsdbnuw:0e9a708916e496be7136d0eda4c546253f1f5425ec041fd6e3efda3a1f819ba2@ec2-35-175-68-90.compute-1.amazonaws.com:5432/d3mrjpmsi4vvn1
```

### Setup Auth0
To set up on your own Auth0, if running locally. 

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. API permissions:
   - get:actors-details
   - get:movies-details
   - get:casting-details
   - edit:actors
   - edit:movies
   - edit:casting
   - add:actors
   - add:movies
   - add:casting
   - delete:movies
   - delete:actors

6. Roles available:
   - Casting Assistant
     - can `get:actors-details`
     - can `get:movies-details`
   - Casting Director
     - can `get:actors-details`
     - can `get:movies-details`
     - can `add:actors`
     - can `delete:actors`
     - can `edit:actors`
     - can `edit:movies`
     - can `get:casting-details`
   - Casting Director
     - can `get:actors-details`
     - can `get:movies-details`
     - can `add:actors`
     - can `delete:actors`
     - can `edit:actors`
     - can `edit:movies`
     - can `get:casting-details`
     - can `add:casting`
     - can `add:movies`
     - can `delete:movies`
     - can `edit:casting`
     - can `edit:movies`
     - can `get:casting-details`


## Configuration
Ensure the configuration .env file is filled up by changing `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `AUTH0_DOMAIN`, `ALGORITHMS`, `API_AUDIENCE`, `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `YOUR_CALLBACK_URI`, `APP_SECRET_KEY` and `APP_SECRET_KEY`.

 if running on Heroku, fill in DB_`NAME_HEROKU` with the online Heroku addon postgres URL.

## RBAC testing
To test for RBAC, you may run Casting_Agency.postman_collection.json in POSTMAN

## API endpoint test
To run test:

```bash
$ python test_app.py

```

## To start API locally
```bash
$ export FLASK_APP=app.py
$ flask run
```
Run create_sample.py to create sample data.

```bash
$ python create_sample.py  
$ flask run

```
### Base URL

**_https://mycastingagency.herokuapp.com/**







Running this project locally means that it can´t access `Herokus` env variables.
To fix this, you need to edit a few informations in `config.py`, so it can
correctly connect to a local database

3. Change database config so it can connect to your local postgres database
- Open `config.py` with your editor of choice. 
- Here you can see this dict:
 ```python
database_setup = {
    "database_name_production" : "agency",
    "user_name" : "postgres", # default postgres user name
    "password" : "testpassword123", # if applicable. If no password, just type in None
    "port" : "localhost:5432" # default postgres port
}
```
`

4. Setup Auth0
If you only want to test the API (i.e. Project Reviewer), you can
simply take the existing bearer tokens in `config.py`.

If you already know your way around `Auth0`, just insert your data 
into `config.py` => auth0_config.

FYI: Here are the steps I followed to enable [authentification](#authentification).

## API Documentation
<a name="api"></a>


### Authentification



### Available Endpoints


#### GET Endpoints


**GET /actors/<id>** Fetches all information of the actor of specific id.

Example output:
```
{
    "result": [
        {
            "dateofbirth": "20-02-1970",
            "first_name": "Chris",
            "gender": "male",
            "id": 3,
            "last_name": "Hemsworth"
        }
}
```
**GET /movies/<id>** Fetches all information of the movie of specific id.

```

{
    "result": [
        {
            "duration_mins": 99,
            "genre": "mystery",
            "id": 1,
            "released_year": 2010,
            "title": "Dr Strange"
        }
}
```

**GET /casting/<id>** Fetches all information of the casting of specific id.

```

{
    "result": [
        {
            "duration_mins": 99,
            "genre": "mystery",
            "id": 1,
            "released_year": 2010,
            "title": "Dr Strange"
        }
}
```

**GET /actors** Fetches all information of the actors.
Example output:
```
{
    "result": [
        {
            "dateofbirth": "20-02-1970",
            "first_name": "Chris",
            "gender": "male",
            "id": 3,
            "last_name": "Hemsworth"
        }
}
```

**GET /casting** Fetches all information of the casting.
Example output:
```
{
    "result": [
        {
            "dateofbirth": "20-02-1970",
            "first_name": "Chris",
            "gender": "male",
            "id": 3,
            "last_name": "Hemsworth"
        }
}
```

**GET /movies** Fetches all information of all movies.

```
{
    "result": [
        {
            "duration_mins": 99,
            "genre": "mystery",
            "id": 1,
            "released_year": 2010,
            "title": "Dr Strange"
        }
}
```

#### DELETE Endpoint

**DELETE /movies/id/delete**: Deletes a specific movie using the id of the movie.

```
{
    "result": [
        {
            "duration_mins": 99,
            "genre": "mystery",
            "id": 1,
            "released_year": 2010,
            "title": "Dr Strange"
        }
}
```


**DELETE /actors/id/delete**: Deletes a specified actor using the id of the actor.




#### POST Endpoint

**POST /movies**: Sends a post request in order to add a new movie

**POST /actors**: Sends a post request in order to add a actor

**POST /casting**: Sends a post request in order to add a casting



#### PATCH Endpoint

**PATCH /movies/id**: Edit the details a specific movie using the id of the movie.

```
{
    "result": [
        {
            "duration_mins": 99,
            "genre": "mystery",
            "id": 1,
            "released_year": 2010,
            "title": "Dr Strange"
        }
}
```


**PATCH /actors/id**: Edit the details of a specified actor using the id of the actor.

**PATCH /actors/id**: Edit the details of a specified actor using the id of the casting.













# <a name="authentification-bearer"></a>
### Auth0 to use existing API
If you want to access the real, temporary API, bearer tokens for all 3 roles are included in the `config.py` file.

## Existing Roles

They are 3 Roles with distinct permission sets:

1. Casting Assistant:
  - GET /actors (view:actors): Can see all actors
  - GET /movies (view:movies): Can see all movies
2. Casting Director (everything from Casting Assistant plus)
  - POST /actors (create:actors): Can create new Actors
  - PATCH /actors (edit:actors): Can edit existing Actors
  - DELETE /actors (delete:actors): Can remove existing Actors from database
  - PATCH /movies (edit:movies): Can edit existing Movies
3. Exectutive Dircector (everything from Casting Director plus)
  - POST /movies (create:movies): Can create new Movies
  - DELETE /movies (delete:movies): Can remove existing Motives from database

In your API Calls, add them as Header, with `Authorization` as key and the `Bearer token` as value. Don´t forget to also
prepend `Bearer` to the token (seperated by space).

For example: (Bearer token for `Executive Director`)
```js
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmYzc2N2YxYmEwZWJiNDIwMTYzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NjI0NjksImV4cCI6MTU4MTg2OTY2OSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.iScamWOFNx9pjiVZhsvPzDoRi6EraZaxWg-WMj80HNW_-dchkOymnKA7OOhPQ8svLc9-wViLlCT-ySnupZ-209cIBVHSA_slncSP-lzEM6NKbBmDEETTQ1oxv2jTH-JL72eLhyAWUsmSIZDmEab1hln1yWEN7mUnn0nZJfxCRCs89h5EGJzXS2v8PbAjq9Mu7wFsrioEMx_PGWzSM0r5WIrKBvpXRy0Jm-vssZl4M1akDHIL5Shcfp_Bfnarc2OLOMvdQVHVDEWhrbFSnfCENLDxkcmB18VnOedJAuY_C88YRUfY2wQAOPux8RVuqIb5KxTg4YP7kiDcBUKXEnhL9A"
}
```