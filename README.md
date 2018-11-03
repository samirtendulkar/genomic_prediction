# Genomic Prediction Project

#### Project Description

API Backend with SQL database and job queue.
Goal:
­ Create Django REST Framework project that allows to:
Manage list of patients and their embryos. Send patient’s report via email. OPTIONAL:
detect embryo’s sex. OPTIONAL: detect Down syndrome.
­ Set up NGINX to serve the project over port 8000 on localhost
­ Set up PostgreSQL database
­ Deploy with Docker

#### Specs:

```
­ Python 3.
­ Django 2.1.*
­ PostgreSQL
­ PythonRQ
­ Web Server NGINX (gunicorn)
­ Docker
```
#### Requirements :

```
­ Token based authentication. There always must be a superuser (username: “admin”,
password: “password”). Tokens are to be stored in the database.There must be an
endpoint to obtain a token for a registered user.
­ Models: patient, embryo
“patient” required fields:
­ first_name,
­ last_name,
­ phone,
­ email
“embryo” required fields:
­ code_name,
­ karyotype
Both “patient” and “embryo” must have “created_at” and “updated_at” fields.
Patient belongs to a user (superuser in this case).
```

Patient can have multiple embryos.
Embryo belongs to only one patient.
­ Email report contains patient’s data and a list (it can be an html list or a table) of patient’s
embryos. Every item on the list must have embryo’s “code_name”, “karyotype”, and
optionally: determined sex and whether or not Down syndrome is present. Use
PythonRQ tasks to create and send the email report. Any email backend can be used.
­ OPTIONAL: Determine embryo’s sex and Down syndrome from karyotype and include it
in the report sent via email.
Karyotype is the representation of the chromosomes of a cell:
46,XX,­4,+
46 ­ total number of chromosomes
XX ­ sex chromosomes
­4 ­ loss of a chromosome
+10 ­ gain of a chromosome
For example: “46,XX” is a normal female, and “46,XY” is a normal male. Male with Down
syndrome: “47,XY,+21” (47 because there’s one extra chromosome 21).
More info on karyotype
­ Endpoints:

1. Authenticate and get token for superuser.
    ­­ use token based auth for all the endpoints bellow ­­
2. Create patient.
3. Read patient.
4. Update patient.
5. Delete patient (if patient doesn’t have embryos).
6. Create embryo.
7. Read embryo.
8. Update embryo.
9. Delete embryo.
10.Get list of all the patients that belong to a valid user (superuser in this case).
11.Get list of all the embryos of a specified patient.
12.Send patient’s report to a specified email address.


#### Main Parts:

```
API Backend Authenticate users.
Provide endpoints for managing
data and executing tasks.
Django REST Framework,
default view: json
Job Queue Service Execution of the long running
tasks: sending email
PythonRQ
Database Persist user data PostgreSQL
Deployment Run code. Give access to the API
at  http://localhost:
Docker
```
#### Deployment :

Deploy your project with Docker. Project’s code base should live in “/code/”. Use Docker
Compose (docker­compose.yml). When you run the docker image, make sure:
­ The database is populated. Every time you build Docker image, postgreSQL database
gets wiped out. Populate database with all the necessary data on build (superuser data
in this case).
­ The NGINX is running and serving your Django REST Framework project (not “python
manage.py runserver”).
­ The correct virtual environment for python is set and contains all the packages used in
the project.
­ Port 8000 is exposed, so we can access the root endpoint at  http://localhost:8000 .
­ The project structure is free of Django’s boilerplate code. Remember: this is an API
backend only.
­ Test are optional.

#### When you are ready :

```
­ Test all the endpoints. They should work as expected and return proper responses in
case of invalid request.
­ Push to GIT and send us the repo link. Make sure that you have properly configured
Dockerfile and docker­compose.yml. By running “docker­compose up” we should be
able to have it running and be able to access the API at  http://localhost:8000 .
­ You can send us the Docker image repo as well, but it’s not required.
­ Send us the list of all the endpoints that you’ve set up.
­ Explain, how you structured your code and why is it the best way to go in your opinion
(OPTIONAL).
```

NOTE: if you’re unfamiliar with Docker, you can send us just the code base that we can run
using Django’s “manage.py runserver”. It’s totally AOK.


