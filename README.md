# Multi User Task Tracker

This web application allows users to register and create task lists with deadlines. Once a task is completed, users can mark it as done and also delete it if necessary. Users have the option to update their profiles or delete their profiles from the database.
## Demo

https://drive.google.com/file/d/1MDFBwBi20awV4WCsdnI2DNqk5lWpLNTC/view?usp=sharing

## Screenshots

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/22466417-890d-48de-9c88-398d9fac6225)

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/d6a8c285-6ebd-4601-b7ea-082bb65853e7)

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/40dd83ac-53c6-4650-bb86-9909c0369c16)

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/933dc593-a14d-4787-990e-fb4a3302acfc)

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/29ca2c54-b27f-49e3-bd66-c4f5f74e5f18)

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/953ea8b5-20a3-473b-8909-4f9fa94c4924)

![image](https://github.com/fadingreality1/Multi-user-Task-tracker-webapp-using-django/assets/114291201/bc801ddf-e431-4658-8e24-9b55c9d175f3)


# Run Locally

### Clone the branch master in a folder of your choice

```bash
    git clone -b master --single-branch https://github.com/manas9839/Multi-user-Task-tracker-webapp-using-django
```

### Go to the project directory.
#### Project directory is where your manage.py located.

```bash
  cd project-location
```

### Install dependencies.

#### This command will install package for creating virtual enviroment.
```bash
  pip install pipenv
```

#### In project directory, run,

```bash
  pipenv install 
```

It will install all the dependencies from Pip.lock file.

#### Start the virtual enviroment,

```bash
  pipenv shell
```

#### Making migrations or structure for database.

```bash
  python manage.py makemigrations
```
```bash
  python manage.py makemigrations tasks
```

#### Migrating the database.

```bash
    python manage.py migrate
```
it will create sqlite3 database file in your directory.

#### Now you can either run project directly using command,

```bash
    python manage.py runserver
```
#### Or create super user to manage and access admin panel.

```bash
    python manage.py createsuperuser
```
you'll have to enter name, email and password and then you can access admin panel.

#### now you can create as many accounts you want and create Tasks.
## Features

- Multi user web app with profile management.
- Add, delete and updating the Tasks.
- List of Tasks sorted by Ascending order of deadlines.

## Tech Stack

**Client:** HTML, CSS, JS, JQuery, Bootstrap.

**Server:** Django.

**Database:** SQlite3, we can use any Database with right setup..



## Authors

- [@ManasAwasthi](https://github.com/manas9839)


## Environment Variables

I haven't designed it's frontend to be resposive so it will look good only on PC.
You can make contributions to it if you want about frontend or any other functionality.
