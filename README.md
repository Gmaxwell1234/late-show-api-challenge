# Late Show API Challenge

A RESTful API for managing guests, episodes, and appearances on a late-night show. Built with Flask, SQLAlchemy, JWT authentication, and PostgreSQL.

## Features
- User registration and login with JWT authentication
- CRUD operations for Guests, Episodes, and Appearances
- Protected endpoints for creating/deleting resources
- Database migrations with Flask-Migrate

## Tech Stack
- Python 3.8
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-Bcrypt
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <git@github.com:Gmaxwell1234/late-show-api-challenge.git>
cd late-show-api-challenge
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
pip install pipenv
pipenv install
pipenv shell
```

### 3. Configure the Database
Update the database URI in `server/config.py` if needed:
```
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```
Create the database in PostgreSQL:
```bash
createdb late_show_db
```

### 4. Run Migrations
```bash
flask db upgrade
```

### 5. Seed the Database (Optional)
```bash
python server/seed.py
```

### 6. Start the Server
```bash
flask run
```
The API will be available at `http://localhost:5000/`.

## API Endpoints

### Auth
- `POST /auth/register` — Register a new user
- `POST /auth/login` — Login and receive a JWT token

### Guests
- `GET /guests` — List all guests
- `DELETE /guests/<id>` — Delete a guest (JWT required)

### Episodes
- `GET /episodes` — List all episodes
- `GET /episodes/<id>` — Get episode details
- `DELETE /episodes/<id>` — Delete an episode (JWT required)

### Appearances
- `POST /appearances` — Create an appearance (JWT required)

## Authentication
Some endpoints require a JWT token. Register or login to receive a token, then include it in the `Authorization` header:
```
Authorization: Bearer <your_token>
```

## Database Migrations
This project uses Flask-Migrate (Alembic) for database migrations. To create a new migration after changing models:
```bash
flask db migrate -m "Your message"
flask db upgrade
```

## Development Notes
- All code is in the `server/` directory.
- Models: `server/models/`
- Controllers: `server/controllers/`
- Config: `server/config.py`
- Seed script: `server/seed.py`

## License
MIT
