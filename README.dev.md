# Running the application
There are two ways to run this application. 

1) Runs the databases in a docker container, and the application on the local server. This will **support hot reloading**
2) Only requires one command to be run but **doesn't support hot reloading** because Django can't do hot reloading in a Docker container 

[localhost:8002](localhost:8002) will host the application <br>

<details>
<summary>Running the database in Docker, and the app locally</summary>

**To run the app locally:**

    uvicorn backend.config.asgi:app --reload --host localhost --port 8002

  or

    gunicorn backend.config.asgi:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8002

**To run the databases in the Docker container**
- Navigate to the root directory
- Run the following command <br>
`docker compose -f docker-compose-dev-no-front-back.yaml up --build`
</details>

<details>
<summary>Running the application and databases using Docker</summary>

**To run the Docker containers**
- Navigate into `backend/env/dev.env`
  - The variable `DB_HOST` show have the value **db** (the name of the Postgres service in the Docker compose file) 


- Navigate to the root directory
- Run the following command <br>
`docker compose -f docker-compose-dev.yaml up --build`

</details>