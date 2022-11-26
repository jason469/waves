if running it first time ever run this before the application:

    python manage.py collectstatic

run the app:

    uvicorn backend.root.asgi:app --reload --host localhost --port 8005

  or

    gunicorn backend.root.asgi:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8002
