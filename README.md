
# Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

# Model
- Movies with attributes title and release date
- Actors with attributes name, age and gender

# Roles:
- Casting Assistant
  - Can view actors and movies
- Casting Director
  - All permissions a Casting Assistant has and…
  - Add or delete an actor from the database
  - Modify actors or movies
- Executive Producer
  - All permissions a Casting Director has and…
  - Add or delete a movie from the database

# API Endpoint
The Flask have 8 endpoint, all of them requires a valid jwt token:
- `GET '/'`: Hello world! 👋
- `GET '/actors'`: Get list actors.
- `GET '/movies'`: Get list movies.
- `DELETE '/actors/<int:id>'`: Delete an actor.
- `DELETE '/movies/<int:id>'`: Delete an actor.
- `POST '/actors'`: This takes a actor information as json arguments to create new actor. Example: ```{
    "name": "test",
    "age": 22,
    "gender": "women"
}```
- `POST '/movies'`: This takes a movie information as json arguments to create new movie. Example: ```{
    "title": "test",
    "release_date": "02/02/2024"
}```
- `PATCH '/actors/<int:id>'`: This takes a actor information as json arguments to update actor. Example: ```{
    "name": "test",
    "age": 22,
    "gender": "women"
}```
- `PATCH '/movies/<int:id>'`: This takes a movie information as json arguments to update movie. Example: ```{
    "title": "test",
    "release_date": "02/02/2024"
}```

## Authentication & Authorization
To login or set up an account, go to the following url: 

```
url
```

After login you will see an access_token in the url path.

```
url
```

There are three roles within the API. ***Casting Assistant***, ***Casting Director*** and ***Executive Producer***. The logins for the three roles has been provided in the separate notes 

The url for the API:
```
url
```