# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
