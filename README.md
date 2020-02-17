:satisfied:
# portfolio
#### Application to post projects to be rated by other users, 16 02 2020
#### By ** PETER KURIA**

## Description
 - This is an app that allows users to like post and comment on other people posts.

## Project live site

## Features
* User can log in to application and view other peoples posts.
* A user can rate o a post.
* A user can upload posts and edit their profile.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

## Behavior Driven Development
-| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets redirected to the login page  | User logs in | Directed to the home page where they see posted photos |
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |
|  Home page loads | click to rate  | Rting count appear|
|  Homepage loads | Click `profile` | User's profile appears |
| Homepage loads | Click `upload image` icon | User's redirected to a page where they can upload an image |
| Homepage loads | Click `settings` icon | A modal appears where one can change their password or logout |
| Homepage loads | User inputs in the search form and presses enter | Searched results show |


## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/costamay/Awwards.git

2. Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
- psql
- CREATE DATABASE instacopy;

4. Create .env file and paste paste the following filling where appropriate:

-SECRET_KEY = '<Secret_key>'
-DBNAME = 'instacopy'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True
5. Run initial Migration
-python3.6 manage.py makemigrations instagram
-python3.6 manage.py migrate
6. Run the app
-python3.6 manage.py runserver
-Open terminal on localhost:8000

## Technologies Used
* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRESS

## Prerequisite
* PYTHON 3.6
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRESS

## Support and contact details
contact me @ petermbaik@gmail.com

### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved
  
