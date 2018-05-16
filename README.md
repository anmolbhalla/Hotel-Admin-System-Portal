# Hotel-Admin-System-Portal

A simple django framework based project to -

* Update hotel room prices and room availability till a year for any hotel admin user persisitng to the database.
* Bulk update for multiple days as well as update for single days.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python pip package
If using python version 2 :
```
sudo apt-get install python-pip
```

If using python version 3 :
```
sudo apt-get install python3-pip
```

You will need Django framework to run this project smoothly. Go to your terminal and execute the following command or visit [Django](https://www.djangoproject.com/) website.


For python 2 :
```
pip install django
```

For python 3 :
```
pip3 install django
```

### Deployment

A step by step series of examples that tells what you have to do to get this project running -

* Enter the project directory.
* Make migrations for the project -

```
python/python3 manage.py makemigrations
```

* Migrate the changes -

```
python/python3 manage.py migrate
```

* Create SuperUser-

```
python/python3 manage.py createsuperuser

Provide username, email and password and remember it.

```

* Run the server -

```
python/python3 manage.py runserver
```

* Access http://127.0.0.1:8000/home on your browser to use the application.

### Usage

* Firstly Access http://127.0.0.1:800/home/db to establish the database.
* The calender on home shows the values from the databse. SOme default is being set.

![Screenshot](/Screenshots/Screenshot%20from%202018-05-16%2020-09-34.png)

* To update values in the database for multiple days select the fields and hit update.

![Screenshot](/Screenshots/Screenshot%20from%202018-05-16%2020-13-17.png)

* To update value in the database for a single day click on the data to be updated in the calender and edit it and click anywhere outside it.

![Screenshot](/Screenshots/Screenshot%20from%202018-05-16%2020-16-17.png)

![Screenshot](/Screenshots/Screenshot%20from%202018-05-16%2020-16-23.png)

* To check the entry in the database access :
	
	 http://127.0.0.1:800/admin
	Authenticate yourself with the username and password created in the above steps.
	Go to Hotel and see the object you want to see.
	![Screenshot](/Screenshots/Screenshot%20from%202018-05-16%2020-20-36.png)

## Built With

* [Django](https://www.djangoproject.com/) - Python web framework used.
* [Python](https://www.python.org/) - Python programming language.




