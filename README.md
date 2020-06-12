# Project Name

Inspire

## Description

Inspire is an application that provides users with a platform whereby they can showcase their websites and  receive reviews from other users. 

## Core Features

<ul>
<li>A user can view posted projects and their details</li>
<li>Post a project to be rated</li>
<li>Rate Projects</li>
<li>Search for projects</li>
<li>View a projects overall score</li>
<li>A user can view their profile page</li>
</ul>

## Prerequisites

<ul>
<li>Python3</li>
<li>Virtual Environment</li>
<li>Django </li>
</ul>

## Technologies and Tools Used

<ul>
<li>Html and Css </li>
<li>Git Version Control</li>
<li>Javascript </li>
<li>Django</li>
</ul>

## Installation and Setup

Clone the repository below

  `https://github.com/Brenda-M/inspire.git`

Create and activate a virtual environment. 

  ```
  virtualenv venv --python=python3.6
  source venv/bin/activate

  ```

Install required Dependencies.

  ```
  pip install -r requirements.txt
  Ensure that the virtual  environment is active before making any instalations
  ```

Setup a local database.

  ```
  CREATE DATABASE <your-database-name>

  ```

Create a .env file and add the following.

  ```
  SECRET_KEY='<random_string'
  DEBUG=True
  DB_NAME='<your_database_name'
  DB_USER='<your_database_user>'
  DB_PASSWORD='<your_database_password>'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.127.0.0.1'
  
  ```

Make a migrations file and migrate.

  ```
  python manage.py makemigrations
  python manage.py migrate

  ```

Run the application

  `python manage.py server`

## Endpoints
  <ul>
  <li>api/v1/projects/</li>
  <li>api/v1/users/</li>

  </ul>



## Live Link

View the website <a href="https://inspire-an-awwward-clone.herokuapp.com/">here</a>

## License

 MIT
