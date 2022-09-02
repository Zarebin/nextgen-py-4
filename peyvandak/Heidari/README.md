## Instructions on Running the Program on Linux 
1. Make a `run.yaml` file and copy the following code inside it (or just simply download the run.yaml file):

```
version: '3'

services:
  web:
    image: miladh9999/url-shortener-django:1.0
    container_name: url-shortener-django
    command: "python3 manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```

2. Save the `run.yaml` and enter the following command:

```
docker compose -f <path to run.yaml file> up -d
```

3. Open your browser and type ``` localhost:8000/swagger ```. There you can see detailed documentation of the API.
4. Enjoy playing with the API !
