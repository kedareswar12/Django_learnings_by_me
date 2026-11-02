# Intro to the Django
  - Django is a hight-level programing web framework 
  - enables us to built the robust(app that does not crash) , scalable(hadles the traffic) , secure web applications 
  - written in python and used in the python based development 

# Importnant things you need to know about the Djano (in building it ) :-
 - Authentication
 - URL Routing 
 - Forms & Validation
 - Database Migrations 
 

## Initially u cant run the django file with out making it , because we are using uv 
  - If you need to use the djnago file then you need to use them with the command - `django-admin startproject <projectname(mysite)>` 
  - since we are usign the uv buit pakage we need to go into the source and then create a folder and then you need to run the command `uv run django-admin startproject config .`


## Significance of th eproject files insed the Djnago Files 
  `Django_udemy` is the root directory which serves the whole project 
 - `mysite` - name of the folder(project)
 - `__init__.py`  -> Makes the entire directory as a python pakage 
 - `asgi.py`      -> used for the websockets , for async programs 
 - `settings.py`  -> destils related the `Installed Apps` , `Middlewares` , `Database`
 - `urls.py`      -> routing urls that need to reach the server 
 - `wsgi.py`      -> web server gateway interface 
 - outside of the django main file you willl have the `manage.py` file
  - This is the command line utility
  - This will let you to perform the admin task for your project like `1. Runing the local Development Server `

## To run the Django Server U need to go to the `django_Learnings` file 
  - Run the command
    - 1. uv run manage.py migrate 
    - 2. uv run manage.py runserver 
  - This will give you a `http://127.0.0.1:8000/` local host server ip 

- You need to know about the apps in Django file , app is nothing but the different sections in your application 
- for starting the file you must do as go to the django_learnings folder and typr thr command  `uv run python manage.py startapp myapp` -> this will give you the real folder or yours

## significance of myapp folder (`uv run python manage.py startapp myapp`)
 - view.py - it is the file which processes the user request , the job of this file is to accept the request and anlyze the request and send back an appropriate response 
  - view in Django is the simple pyhton function 
  -# Create your views here.
      - view needs to accept the incomming request so we need to pass the paramenter 
      - if you are passing the request then you need to know what response need to be returned 
      - when ever you are sending the response you are sedding the http request for this we get an http response 

- you are requested to maintains your own `urls.py` file insed your app and consoliated to mysite this is the conventional way that we use to follow 

- `uv run python manage.py makemigrations ` this command need to be used whaen ever any chages is made in the models.py file 
- `uv run python manage.py migrate . ` - this will migrate the model into the data base 
- if you ever need to create the data_items inside the database then you can use the command  `uv run python manage.py shell` 
  - this will help you to create the objects in the shell 
  - keep remember after creation of the object save the object 
  - to view all the objects in the shell you can use the `Item.objects.all()` -> This will list out all the objects in the daatabse 
  - but to create the data items in the database you need to use the admin panal provided by the Django 
  - and for creating the admin panel you need to register the dummy user initially this can be done by  `uv run python manage.py createsuperuser `
  - `admin.site.register(Item)` for registerring the item data in the admin panael go to the `admin.py` and register the model you have cresated by the above syntax 