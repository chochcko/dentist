
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "ad1ecb70-7906-4a0c-91c2-3de0c69062e1c882bcd8-410a-4cac-933e-1e95ee795c2b8f1b88c2-232d-4b4f-9490-abb6f880c4d4"
NEVERCACHE_KEY = "0f0d9d9d-651b-427b-b6f6-25bf44fb3710912ed660-2b7f-4088-aba2-7a7626847bfab21a3d83-6b81-48ba-8830-5ddeb14acd06"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
