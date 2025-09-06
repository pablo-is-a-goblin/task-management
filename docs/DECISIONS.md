# Decisions:
Set decimal places to 2 and max digits to 5

## Features completed

## Features skipped

## Time allocation breakdown

### Day 1
I setted the basic Docker infrastructure for Django and postgreSQL, checking their connection and implementing a few models: User, Task, Tag and Comment

### Day 2
I spent the second day reading documentaion focused on Celery and its integration with Django, as well as using Django templates with DRF as I am used to working with a JavaScript frontend

### Day 3
I have implemented all the API endpoints related to user management and authetification, as well as a simple frontend with Django templates to give clients an intuitive way to interact with the API. I also wanted to implement the rest of the API, although I had problem with the authentification system which cosumed a great part of today's worktime (more about it on the 'Technical challenges faced' section)

## Technical challenges faced
I had a big problem implementing the authentification system because I forgot to use the 'set_password()' function to set the password of the users so that it is hashed on the database, which meant that the 'login()' function from the Django authetification system did not recognized any password as good.

## Trade-offs made

## What you would add with more time

## Justification for Django templates