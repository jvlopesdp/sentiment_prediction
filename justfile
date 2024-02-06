set shell := ["cmd.exe", "/c"]

up:
  docker-compose up --build
# Builds the image and start the container application

down:
  docker-compose down
# Stops containers and removes containers, networks, volumes, and images created by up.


