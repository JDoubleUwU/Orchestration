# HospitalAWSDeployment
Deploying hospital project to AWS and running with Docker Containers

# Requirements
See requirements.txt

# AWS setup
1) Install Amazon CLI, see link https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2) After installing, check if it works by opening a terminal and typing 'aws --version'
3) Log onto your AWS account then type "IAM" in the search bar
4) Select the 'Create Group' option
5) Name the group anything (but you should pick admin) then from "PolicyName", add AdministratorAccess
6) Select 'User' option then select 'Create User'
7) Name your user anything (like developer) and from roles, select the name of your group from step 5
8) Click on the newly created user and select "create access key"
9) In use case, select "Command Line Interface (CLI)"
10) In your desktop terminal, type 'aws configure' then copy and paste your created user's access key and secret key
11) If setup is successful, 'aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com' should say "login successful"

# Uploading docker image to AWS, ECR
1) In AWS, enter ECR and click repositories
2) Under "Private Repository" and click "Create repository"
3) Open a terminal in project directory (where dockerfile, .env, manage.py, docker.yml is)
4) build the docker image
   
   docker compose build web
6) tag docker image with
   
   docker tag <image_name:tag> <aws_account_id>.dkr.ecr.<region>[.amazonaws.com/](https://.amazonaws.com/)<your_repo_name>:latest
8) push docker image with
   
   docker push <aws_account_id>.dkr.ecr.<region>[.amazonaws.com/](https://.amazonaws.com/)<your_repo_name>:latest

# Creating EC2 instance and running docker image
1) In AWS search bar, search for "EC2"
2) Select Instances -> Launch instance

# Running Locally
1) In the .env file, make sure 'DB_HOST' is set to 'localhost'
2) Run the activate.bat file
3) Create a superuser by typing 'python mangae.py createsuperuser'
4) In the terminal type 'python manage.py runserver
5) Enter '127.0.0.1:8000' in address bar

# Running on Docker
1) In the .env file, make sure 'DB_HOST' is set to 'db' (to reference the db created in docker-compose.yml)
2) Run the activate.bat file
3) Create the containers by typing "docker compose build"
4) Create the superuser for the docker container by typing "docker compose run <name of service in docker-compose.yaml, here use 'web'> python manage.py createsuperuser"
5) Run the containers by typing "docker compose up -d"

# Features
1) 127.0.0.1:8000/admin           -Admin panel to manage the database via the web
2) 127.0.0.1:8000/Doctors         -List view of all the doctors
3) 127.0.0.1:8000/Doctors/<pk>    -Detail view of the doctor, allows staff users to edit/delete an existing doctor
4) 127.0.0.1:8000/Doctors/create  -Create view to add a new doctor
5) 127.0.0.1:8000/api             -View available API's 

# Notes
1) If makemigration isn't detecting the models, try typing "python manage.py makemigrations <name of project, here use 'myapp'>
2) It is bad practice to load the .env file into the docker container, but we are not using a secret manager so .dockerignore does not exclude .env
