# Hello World
TYPE DESCRIPTION HERE

## How to run

### Pre-Requirements

```bash
git clone git@github.com:dhacks/team-h.git
cd team-h
pip3 install -r requirements.txt
```

### Initialize Database

```bash
python3 run.py db init
python3 run.py db migrate
python3 run.py db upgrade
```

### Run Server in Debug Mode

```bash
python3 run.py runserver -d
```
