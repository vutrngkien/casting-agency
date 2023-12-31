
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

# Example token to test role:
```
ASSISTANT_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTE3Mjk3MDY2NDIzMDE1NTg1MCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk1NTY0MTM4LCJleHAiOjE2OTU1NzEzMzgsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.vuZ8xAySwbhc-3zcCv6UIpvqSKXtUOrYCcaz_P1hQBDl6oW4M51o3FMrS9F6-A4irH-IHE5CtzmNxMpH8iTFaYeQpoMoTz7a7VI9lcQOjiqZDapvMTYB-YX0_t1loVsB15clnw-GZEmTZ_t4O8-9YM-vwhI42sl2hL9tOVMxUzKW0ZZRFjisxzNnTGRJS0FCOhBR9YZ7eWcfaVleveJvZExeawnmjRKULfapSKXhAKw0qb9n0BexxrB0VYjT-lquk-X0eWpX-AaP1mCBFYiOtjxXwUSyt7GAaTvAnM6B87RMz4qfvMRqT_rDBwGbPNhueHEoEncSGQLPYF-hbmIgmw
```

```
DIRECTOR_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDU5MjA2MjUwMTIzMDgyMzk4OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk1NTY0Mzk1LCJleHAiOjE2OTU1NzE1OTUsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.Lo20mKmVeQ2uadKj76orc7Dg2c3iMSObDgbcxFG9ArxHWuSDCfGtVAfIovkzgx3YkUQLWpXtfHpSrKJu5-tkhNtLDNcrE7d4zkfwdDqqEQwuMRjkEPlnySAIsiFp3Pc1jd6KoAYvM-A8cim4s7kzMDIS9n6EaK5RSogcxHeYkAizdRstPrzql7SVE9dVKI7v1AWehtm12lQcYlk2bupZzWM5AqU3zcXriXuJsDiyi8CIZdbqRAmt0KFDNXLe6cOinT5KvEyD5tG4skbQsPOjeVBmtv1tHPC96_rr28S4GfVyEGRe1J4EA5EaMjQZjVac88JcnZWXxYCcT0nfZyUCZQ
```

```
PRODUCER_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzY5NjA3MjY3MTkzMTI4MjI5MSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk1NTY0MzA1LCJleHAiOjE2OTU1NzE1MDUsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ikDmENRi77t6hZMPSPZtZHYm26qCkfzYjoustHjEHXueta9Zlohg_QcOXi3P0zLfJhtTWkUAKCoH0xB_452bIZw2qO-wuzIMm7R2a72b-MHKGJSe2hIzDStCX6npOVukF1tlHVZOw8nWqEnZwcqkHLbtIAQ275Rw9_XatSAToKQ0xCc_gijuSGFpSV-6-VTXFTlYvi1Quf-5cK_eggWV6XX5AjVDTWdvkMVw6b-OaAfYKVPr8b2Oc39C0e0W0DY8THJnveu12BA0o9HHyW654YLDHZT_2bt3gOPx3WJ109q-j7lmiKXz1yeKUMHAwu7cUhBpvBiweh5bHjA4IUv_FQ
```

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
To login or sign up: 

```
https://udacity-fullstackweb.us.auth0.com/authorize?audience=casting-agency&response_type=token&client_id=FZ1z6RbcZ61yZa4V2t5bWdrFRMmPNPYh&redirect_uri=https://casting-agency-c0x3.onrender.com
```

After login you will see an access_token in the url path.

```
https://casting-agency-c0x3.onrender.com/#access_token=<TOKEN>&expires_in=7200&token_type=Bearer
```

The url for the API Endpoint:
```
https://casting-agency-c0x3.onrender.com
```