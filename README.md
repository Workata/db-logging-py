# db-logging-py

Example of Python logging integrated with Postgres

Copy env file
```sh
cp -n .env.example .env
```

Create new venv
```sh
python3 -m venv ./venv
```

Activate venv
```sh
. ./venv/bin/activate
```

Install needed dependencies
```sh
pip install -r requirements/dev.txt
```

```sh
sudo apt-get install libpq-dev
```

Run postgres / pgadmin
```sh
docker compose up
```

Write dummy log
```sh
python3 ./src/main.py
```

