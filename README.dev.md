# Running the application
As this is a full-stack application, you'll need to run 2 separate ports to access the application. <br>
[localhost:8005](localhost:8005) will host the backend server <br>
[localhost:4200](localhost:4200) will host the frontend application

Both applications should support hot reloading (meaning you don't need to restart the application or server for changes to be applied)

<details>
<summary>Running each port individually</summary>
**To run the backend server:**

    uvicorn backend.config.asgi:app --reload --host localhost --port 8005

  or

    gunicorn backend.config.asgi:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8002

**To run the frontend application:**
</details>

<details>
<summary>Running both ports using Docker containers</summary>
To run both ports with one command, you can spin up several docker containers, each housing one part of the application

I've written the Docker file to have 1 container for the backend, 1 for the frontend, 1 for the database and 1 for caching (Redis)

**To run the Docker containers**
- Navigate to the root directory
- Run the following command <br>
`docker compose -f docker-compose-dev.yaml up --build`

</details>