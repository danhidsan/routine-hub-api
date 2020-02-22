FLASK_ENV=development
FLASK_APP=RoutineHub.app:create_app
SECRET_KEY=changeme
DATABASE_URI=postgresql://postgres:routinehub@localhost/routinehub
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=amqp://guest:guest@localhost/
