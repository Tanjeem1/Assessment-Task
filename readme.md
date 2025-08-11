# User Authentication API (DRF & jwt)


## Overview
This is a Django Rest APi based user authentication api. It allowes to registration, login, change password with jwt authentication.


## Features
- user can complete their Registration
- user can Login
- Retrive user's information (id, name, email) from database with authentication token
- change password with JWT authentication


## Tech Stack
- **Backend**: python, DRF, JWT


## Prerequisites
For test api endpoint use postman


## Build and start locally:vs code (terminal: powershell)

-run mysql ans apache server background inside xampp app (NB: In the userapi/settings.py file use the Mysql port which was running in your current xampp app server. Mine was 3307, your may could be different)

-clone the repository and open it with vs code
-create a virtual env
-cd userapi (run this command)
-pip install r- requiements.txt (run this command)
-python manage.py makemigrations (run this command)
-python manage.py migrate (run this command)
 

## Test Api Endpoints  

postman documnetation link- https://documenter.getpostman.com/view/39770088/2sB3BEnAQg 
follow the link given, all the description has been written that how to test those endpoints.


This README provides a basic overview, installation steps, and structure based on the visible files.
