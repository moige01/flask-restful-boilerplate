# Flask RESTful API Boilerplate 

This is a boilerplate for a RESTful API implemented in Flask. This boilerplate use SQLAlchemy for ORM handler, and Marshmallow for SQLAlchemy object serializing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

For developer server, just run `flask run` inside of the project folder. Modify `.flaskenv` to change respective environment vars.

### Installing

All that you need for developing and deployment are in `requirements.txt` file.

```
python -m venv VENV_NAME
cd VENV_NAME
source bin/activate
mkdir src
cd src
git clone https://github.com/sugud0r/flask-restful-boilerplate.git
cd flask-restful-boilerplate 
pip install -r requirements.txt
```

## Running the tests

:construction: Comming soon. :construction:

## Deployment

For deployment, this project use Gunicorn :bangbang:**REMEMBER TO CHANGE ENVIRONMENTS VARS WHEN DEPLOY A FLASK APP**:bangbang::

```
gunicorn -w WORKERS -b IP_ADDR:PORT TOP_FOLDER.app:app
```

**NOTE:** You *need* to change the dir to the *outside* of the `TOP_FOLDER` that contain the instance of the Flask object for correct execution of the Gunicorn command. This is due that the project is organized like a package and not like a module, so you need treat it like importing a module and not executing them directly or you will get import errors.

## Built With

* [Flask](https://flask.pocoo.org) - The web framework used
* [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org) - ORM handler
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io) - Used to serealize SQLAlchemy objects
* [Gunicorn](https://gunicorn.org) - Python WSGI HTTP Server for UNIX for deployment

## Contributing

PR's are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
