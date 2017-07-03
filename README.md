# Timetable-app
This is a web app that allows Covenant University students generate their timetables.
It eliminates the need for printing, and any updates to the timetable from the school
is reflected instantly.

## Getting Started


### Prerequisites

Fork this repo into a folder on your machine. 

```
git clone https://github.com/nnamdiib/timetable-app folder-name
```

You need to have virtualenv installed on your machine.
```
pip install virtualenv
```

### Installing

Activate your virtual env and run this command to install all dependencies
```
pip install -r requirements.txt
```

Then run all database migrations to make the db
```
python manage.py migrate
```

Start the server
```
python manage.py runserver
```

Go to the ip address on your browser.
```
127.0.0.1/index
```

## Running the tests

Explain how to run the automated tests for this system
```
python manage.py test
```

## Authors

* **Adeyemo Daniel** - [github](https://github.com/letroot)
* **Ibeanusi Nnamdi** - [github](https://github.com/nnamdiib)

## License

This project is licensed under the MIT License
