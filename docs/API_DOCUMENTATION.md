# API Documentation

**⚠️DISCLAIMER⚠️**: all `POST` and `DELETE` petitions MUST include a header named `X-CSRFToken` with the CRSF token

## Authentication

For creating new users and loggin in and out. Users must have an username, an email and a pasword

### `POST /api/auth/register/`

Creates a new User.

#### Parameters
- `username`: User's username
- `email`: a valid email for the User
- `password`: a password for login

### `POST /api/auth/login/`

Log in to the system creating a new Session.

#### Parameters
- `username`: User's username
- `password`: User's password

### POST /api/auth/logout/

Closing the Session to log out.

#### Parameters
None

## User management

For viewing and editing Users data.

### `GET /api/users/`

Returns a list of the Users instances in the database. Each Users instance has the following fields:
- `id`: a number to identify that User. It is the primary key in the database, which means that each User has a unique `id`
- `username`: User's username
- `email`: User's email

#### Parameters
None

### `GET /api/users/{id}/`

Returns the data of the User whose `id` matches `{id}`. The fields are the same as in `GET /api/users/`

#### Parameters
None

### `POST /api/users/{id}/`

Updates User number `{id}`'s data.

#### Parameters
- `usename`: new username
- `email`: new email

### `GET /api/users/me/`

Returns the data of the logged User. It is the same as using `GET /api/users/{id}/` with the logged User's `id`

#### Parameters
None

## Tag Management

For viewing and editing Tag instances. Each Tag has the following fields:
- `id`: a number that identifies the Tag
- `name`: the display name of the Tag
- `description`: the description of the Tag

### `GET /api/tags/`

Returns a list of the Tags instances in the database

#### Parameters
None

### `POST /api/tags`

Creates a new Tag

#### Parameters
- `name`: Tag's name
- `description`: Tag's description

### `GET /api/tags/{id}`

Returns Tag number `{id}`'s data.

#### Parameters
None

### `POST /api/tags/{id}/`

Updates Tag number `{id}`'s data.

#### Parameters
- `name`: new name
- `description`: new description

### `DELETE /api/tags/{id}/`

Deletes Tag number `{id}`'s instance.

#### Parameters
None

## Task Management

For viewing and editing Task instances. Each Task has the following fields:
- `id`: a number that identifies the Task
- `title`: the display name of the Task
- `description`: the description of the Task
- `status`: Task's status. The options are:
  - `N`: Not started
  - `W`: Work in progress
  - `F`: Finished
- `priority`: Task's priority. The options are:
  - `L`: low
  - `M`: medium
  - `H`: high
- `tags`: a list of the `id`s of the Tags associated with the Task
- `estimated_hours`: the number of hours estimated to finish this Task
- `actual_hours`: the number of hours invested in the Task
- `due_date`: Task's due date. It follows the format `"%Y-%m-%d'T'%H:%M:%S+%UTC`. Example: `"2232-03-31T13:42:00+02:00"`
- `is_archived`: a boolean indicating if the Task is archived or not. `true` or `false`
- `created_by`: the `id` of Task's creator

### `GET /api/tags/`

Returns a list of the Task instances in the database

#### Parameters
None

### `POST /api/tasks`

Creates a new Task

#### Parameters
- `title`: Task's name
- `description`:  Task's description
- `status`: Task's status
- `priority`: Task's priority.
- `tags`: Task's list of Tags' `id`s
- `estimated_hours`: Task's estimated hours
- `actual_hours`: Task's actual hours. NOT mandatory
- `due_date`: Task's due date.
- `is_archived`: Task's 'is_archived' boolean

### `GET /api/tasks/{id}`

Returns Task number `{id}`'s data.

#### Parameters
None

### `POST /api/tasks/{id}/`

Updates Task number `{id}`'s data.

#### Parameters
- `title`: Task's new name
- `description`:  Task's new description
- `status`: Task's new status
- `priority`: Task's new priority.
- `tags`: Task's new list of Tags' `id`s
- `estimated_hours`: Task's new estimated hours
- `actual_hours`: Task's new actual hours. NOT mandatory
- `due_date`: Task's new due date.
- `is_archived`: Task's 'is_archived' boolean

### `DELETE /api/tasks/{id}/`

Deletes Task number `{id}`'s instance.

#### Parameters
None

### `GET /api/tasks/{id}/assign`

Returns `assigned_to`, a list of the Users' `id` that are assigned to Task number `{id}`

#### Parameters
None

### `POST /api/task/{id}/assign`

Update the list of Users assigned to the Task

#### Parameters
- `assigned_to`: Task's new list of Users assigned



