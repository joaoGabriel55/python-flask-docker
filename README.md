# SETUP

`python3 -m venv venv`
`. venv/bin/activate`
`pip install Flask`

`pip install psycopg2-binary`
`pip install flask-sqlalchemy`

#
### If are using docker
`docker container exec -it postgresqldb bash`
#

`su postgres`
`\password <user>`
`psql -U <user>`
`CREATE DATABASE app_flask;`

### Init DB

```py
from src.database import init_db
from src.database import db_session
from src.models import UserModel

init_db()

user = UserModel('john', 25)

db_session.add(user)
db_session.commit()

UserModel.query.all()
```

`python3 app.py`

`http://127.0.0.1:5000/`
