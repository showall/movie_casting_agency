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
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup
Ensure Postgres is run in the backend. Create a database to use, which is to be filled into the .env file. When running using Heroku ensure a postgres database is set up.

```bash
$ heroku addons:create heroku-postgresql:hobby-dev --app [my-app-name]
$ heroku config --app [my-app-name] # eg DATABASE_URL:
# postgres://xjlhouchsdbnuw:0e9a708916e496be7136d0eda4c546253f1f5425ec041fd6e3efda3a1f819ba2@ec2-35-175-68-90.compute-1.amazonaws.com:5432/d3mrjpmsi4vvn1
$ heroku run python manage.py db downgrade --app mycastingagency #to drop all tables/relations
$ heroku run python manage.py db upgrade --app mycastingagency #to re-create all tables/relations
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
To test for RBAC, you may run Casting_Agency_Local.postman_collection.json (local) or Casting_Agency_Heroku.postman_collection.json (Heroku) in POSTMAN

## API endpoint test
To run unitest on endpoints:

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

### Authentification

For authentication, include `Authorization` key to the header of the request.
The key is the `Bearer` token generated from Auth0 prepended by the string "Bearer "    
example ; 
```
header =  
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZDS05mSVkzcGQyYVBEV3dLZGtKaCJ9.eyJpc3MiOiJodHRwczovL3JhbmRvbXNpbHZlci51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjJjNDVkYWY2N2ZkZWEzNTZkMjhiYWQ0IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTY1NzYzNzgyMiwiZXhwIjoxNjU3NzI0MjIyLCJhenAiOiJhNkdOWDhpZnBPcldvdnU5TmFrVXA0U3h6MGtxZEp1bCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDpjYXN0aW5nIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZWRpdDphY3RvcnMiLCJlZGl0OmNhc3RpbmciLCJlZGl0Om1vdmllcyIsImdldDphY3RvcnMtZGV0YWlscyIsImdldDpjYXN0aW5nLWRldGFpbHMiLCJnZXQ6bW92aWVzLWRldGFpbHMiXX0.HmglCiFpo7eWRC8xZBrxBrAJk8arDFNss5n6nCAvlJzMKy7XK-M7GRC0adaXhDplR3oW_WqUOVi5b3tnToY6-RVSJf6cLZzNYJj7_nxNh-KGMaTGkQttZZp0hxfgm0TnVacbLGvbse0XfJ5jgjQw0Q8cvoN72RTljVqyXDH2WTCwCgWQEi1zI-EhUzgHn2B2Du1_NaiATfUuScO6SSjgwnQYsJr-TVZl6xW2XWYICl6ePY6mF0Pa2IDwcR2xQwByNkNpWrOoi5V8vT_Qwmm_P18fQLD0JXSV2y9Uvr14M7xPzZ5zcIwZ-wWksMtgwbMpUr3G8JXKhdnzYTIM-gfjIQ"
}
```
For testing, change the BEARER_TOKEN_FULLACESS in the .env file.
### API Documentation

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
Example output:
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
Example output:
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
            "actor_id": 1,
            "movie_id": 1,
            "role": "Stephen Strange"
        }
    ]
}
```

**GET /movies** Fetches all information of all movies.
Example output:
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

**DELETE /movies/id/delete**: Deletes a specific movie using the id of the movie - returns deleted id. 
Example output:
```
{
    "deleted": "5"
}
```

**DELETE /actors/id/delete**: Deletes a specified actor using the id of the actor- returns deleted id. 
Example output:
```
{
    "deleted": "5"
}
```

#### POST Endpoint

**POST /movies**: Sends a post request in order to add a new movie - returns newly created entity. 
Example output:
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

**POST /actors**: Sends a post request in order to add a actor- returns newly created entity. 
Example output:
```
{
    "result": [
        {
            "dateofbirth": "01-01-1980",
            "first_name": "Robert",
            "gender": "male",
            "id": 2,
            "last_name": "Downey"
        }
    ]
}
```

**POST /casting**: Sends a post request in order to add a casting - returns newly created entity. 
Example output:
```
{
    "result": [
        {
            "actor_id": 1,
            "movie_id": 3,
            "role": null
        }
    ]
}
```

#### PATCH Endpoint

**PATCH /movies/id**: Edit the details a specific movie using the id of the movie- returns just edited entity. 
Example output:
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

**PATCH /actors/id**: Edit the details of a specified actor using the id of the actor - returns just edited entity. 
Example output:
```
{
    "result": [
        {
            "dateofbirth": "01-01-1980",
            "first_name": "Benedict",
            "gender": "male",
            "id": 1,
            "last_name": "Cumberbatch"
        }
    ]
}
```

**PATCH /casting/id**: Edit the details of a specified actor using the id of the casting - returns just edited entity. 
Example output:
```
{
    "result": [
        {
            "actor_id": 1,
            "movie_id": 1,
            "role": "Stephen Strange"
        }
    ]
}
```

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
  - DELETE /movies (delete:movies): Can remove existing Movies from database

  ## To deploy on Heroku

1. Procfile

You should have a Procfile, a text file in the root directory of your application, to explicitly declare what command should be executed to start your app. We'll be deploying our applications using the Gunicorn webserver. Therefore, in our case, the Procfile text file will contain the command to start the app using the Gunicorn
```
    web: gunicorn app:APP
```
2. runtime.txt

A runtime.txtspecifiies which exact Python version will be used. Whereas, a requirements.txt is used by Python’s dependency manager, Pip

3. Database migration

A manage.py file is included in the repository. Ensure you have run the following before migration. 

'''
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

'''
4. Before deploying ensure that you have installed Heroku on the command line and have an account created. 
```
# Install, if Heroku as Standalone
curl https://cli-assets.heroku.com/install.sh | sh

```
To verify 
```
heroku --version
which heroku

```
Once you have the Heroku CLI you can start to run Heroku command. Next, log into heroku with the following command
```
heroku login -i
```
Heroku asks for your account email address and password, which you type into the terminal and press enter.

5. To deploy, navigate back to the project directory and run. 

```
heroku create [my-app-name] --buildpack heroku/python

```
where, [my-app-name] is a unique name that nobody else on Heroku has already used. You have to define the build environment using the option --buildpack heroku/python The heroku create command will create a Git "remote" repository on Heroku cloud and a web address for accessing your web app. You can check that a remote repository was added to your git repository with the following terminal command

```
git remote -v

```

6. To Add PostgresSQL addon for the database

Heroku has an addon for apps for a postgresql database instance. Run this code in order to create your database and connect it to your application
```
heroku addons:create heroku-postgresql:hobby-dev --app [my-app-name]
```

In the command above,
heroku-postgresql is the name of the addon that will create an empty Postgres database.
hobby-dev on the other hand specifies the tier of the addon, in this case the free version which has a limit on the amount of data it will store, albeit fairly high.

7. Configure the App

After the database has been created, you would want to set up the Environment variables in the Heroku Cloud, specific to youor application. Run the following command to fix your DATABASE_URL configuration variable in Heroku.

```
heroku config --app [my-app-name]
```
Copy the DATABASE_URL generated from the step above, and update your local DATABASE_URL environment variable files.

You may set the environment variables in the Heroku portal after you "create" your application. To save the environment variables in the Heroku, you can go to the Heroku dashboard >> Particular App >> Settings >> Reveal Config Vars section and save the variables and their values.

8. You are now ready to push the latest changes: 
```
git add -A
git status
git commit -m "your message"
git push heroku master
```
Whenever you make any changes to your application folder contents, you will have to commit your changes and push again. 

9. Lastly, do not forget to migrate the latest version capture by flask-migrate to the database by running:

heroku run python manage.py db upgrade --app [my-app-name]

You online app is now ready to go. 
