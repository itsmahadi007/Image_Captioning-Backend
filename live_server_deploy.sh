docker-compose down
# docker system prune -a --volumes
docker-compose build
docker-compose run app_v2 python manage.py makemigrations
docker-compose run app_v2 python manage.py migrate
docker-compose up
