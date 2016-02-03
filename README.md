# README #

This README would normally document whatever steps are necessary to get your application up and running. For the app "Concesionario WWW" 

### Software Requirements ###

* Python 2.7.10
* Django 1.6.11
* django-mongodb-engine 0.6.0
* djangotoolbox 1.8.0
* pymongo 3.1.1
* MongoDB
* Pip
* Bootstrap 3.3.5
* font-awesome 4.5.0

### Installation Requirements Development Environment ###

* Install Python

 
```
#!console

sudo apt-get install python
```

* Install Pip

```
#!console

sudo apt-get install python-pip
```

* Install DJANGO-NONREL

```
#!console

sudo pip install git+https://github.com/django-nonrel/django
```

* Install mongodb-engine (drive to MongoDB in Python)
```
#!console
sudo pip install pymongo
sudo pip install git+https://github.com/django-nonrel/mongodb-engine
```

* Install djangotoolbox (utility to avoid some querys not supported in MongoDB)
```
#!console
sudo pip install pymongo
sudo pip install git+https://github.com/django-nonrel/djangotoolbox
```

### Testing Server Development Environment ###

Use this only in Development Enviroment. This comand run server in [http://127.0.0.1:8000/](http://127.0.0.1:8000/). 

```
#!console
python manage.py createsuperuser
python manage.py runserver
```

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

### Contributors ###

* Sebastian Salazar
* Alexander Muñoz

### Data Base to Use ###

* MongoDB, references to install mongo: [MongoPython](https://docs.mongodb.org/getting-started/python/)