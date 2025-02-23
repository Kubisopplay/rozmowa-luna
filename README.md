## Installation

```bash
docker-compose up
```

Then use docker exec to create a superuser, and apply migrations.

```
docker exec -it <container_id> python manage.py createsuperuser
docker exec -it <container_id> python manage.py migrate
```


Swagger documentation is available at http://localhost:8000/swagger/

Admin panel is available at http://localhost:8000/admin/

Use admin panel to add management permissions for users.



### If you docker is not working too

Uncomment the sqlite database in settings.py, comment the postgres and run the following commands:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
