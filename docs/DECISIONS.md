# Decisions

## Features completed

- Docker infraestructure: the application is containerized using Docker Compose and configured in a `docker-compose.yml` file. This allows configuration of enviromental variables via a `.env` file, automatic migrations on startup, generating Docker volumes for database's persistance, dependecies and health checks (for more information about the architecture, see [this doc](ARCHITECTURE.md))
- RES API: a REST-ful API developed in DRF to see, create and manipulate the database. It can serve HTML pages as well as JSON depeding on the 'Accept' header. More on the API at [this doc](API_DOCUMENTATION.md)
- Frontend: basic frontend using Django's templates for loggin and out and checking API endpoints
- Session authentication: for authenticating users I chose to work with DRF's the Session authentication, as the project has a heavy sever-side rendering mindset
- Celery tasks: there are 4 Celery task implemented:
  - `send_task_notification`, to send Users assigned to a Task notifications via email (for example, send a notification when a user is assigned to a Task)
  - `generate_daily_summary`, to generate a daily summary to each user about their assined task
  - `check_overdue_tasks`, to alert users a Task is overdue. Thanks to Celery Beats, it is called every hour
  - `cleanup_archived_tasks`, to delete archived tasks
- Database desing: implemented models for Tasks, Users, Tags and Comments using Django ORM following a Entity-Relation Diagram for best practices (see below). **NOTE:** although Comments' Model is implemented, there are no API endpoints for managing them. 
<img width="1232" height="700" alt="imagen" src="https://github.com/user-attachments/assets/ddc468b7-f7d8-4745-90ce-e5d3e6911d63" />

## Features skipped
Most of the features I skipped were due to not having time to implement them. These days I had already private matters I could not elude, so I could not dedicate to this project all the time I wanted to.

Some small features I really decided to implement were:
- `POST /api/auth/refresh/` endpoint: as I explained above, I used Session Authentication, so I did not see this endpoint worth of implementing. If I had used Token Authentication I would have this endpoint operative
- Using task specific templates: if there is a reason why I love Django is the mindset of keeping things DRY. So, instead of having task-specific templates and user-specific templates, I worked around to find away of using the same template to render the diferent lists and elements of the project (`list.html` & `unit.html`). The only user-specific template I have is `profile.html`. It is not so diferent from the `unit.html` template, but I designed it at the first place for giving Users information on their profile than on the user list

## Time allocation breakdown

### Day 1
I setted the basic Docker infrastructure for Django and postgreSQL, checking their connection and implementing a few models: User, Task, Tag and Comment

### Day 2
I spent the second day reading documentaion focused on Celery and its integration with Django, as well as using Django templates with DRF as I am used to working with a JavaScript frontend.

### Day 3
I have implemented all the API endpoints related to user management and authetification, as well as a simple frontend with Django templates to give clients an intuitive way to interact with the API. I also wanted to implement the rest of the API, although I had problem with the authentification system which cosumed a great part of today's worktime (more about it on the 'Technical challenges faced' section).

### Day 4
I started programming a universal template for rendering all the lists and detail views. Furthermore, I implemented all the endpoints for the tasks and tags API and I tested they worked well. There are still some minors bugs that need fixing.

### Day 5
I have implemented all Celery tasks and the beat schedule and I have tested them. I also created an endpoint for deleting models and a separate endpoint for task assignation to alert users only when task assignation has changed.

### Day 6
I spent the day finishing the documentation and elaborating some diagrams

## Technical challenges faced
I had a big problem implementing the authentification system because I forgot to use the 'set_password()' function to set the password of the users so that it is hashed on the database, which meant that the 'login()' function from the Django authetification system did not recognized any password as good.

I also encountered some challenges at first when working with Celery because it is a tool I had never used before, but I consider I did a pretty good job with it.

Lastly, I committed a grave mistake during the setting of the email notification system as I uploaded to the repo Gmail's App Codes, although I quickly discover this error and I changed the App Codes.

## Trade-offs made

- PUT API routes: as I wanted to serve both HTML pages and JSONs, I encountered a problem: HTML forms only used GET and POST methods, so I decided to substitute PUT routes with POST

## What you would add with more time

- DRY-ness: now, revising all the code, I have discover that there are some parts of the code that can be DRY-er (for example, the Tags and Tasks Viewsets), but I have no time to change it and test it
- A nicer frontend: I would like a more beautiful frontend as well as give it more features, although it would probably require to use JavaScript based frontend
- Cybersecurity: there are some security concerns with the apps such as no email confirmation or no HTTPS protocol, and some secury features like 2-Factor Authentication, JSON web tokens, password confirmation...would be nice

## Justification for Django templates

The main reasons for using Django templates are:
- Easy and fast deployment: as it is Django itself who renders the templates, backend's information display is becomes easier and more upfront than when using a client-side render aproach like when using JavaScript. Thanks to tags like `render_form` and `url`, Django automatically creates HTML forms with the needed fields. Furthermore, when the information changes (for example, we decided to include new field in the serializers), Django automatically updates this forms for us.
- DRY: thanks to Django templates I managed to created a single template to render any queryset of models, as well as concrete instances, instead of developing separated HTML pages for each model
