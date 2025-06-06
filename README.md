# timetracker

App to allow a team to track their time as quickly as possible (few clicks, efficient UI)

## Features

- User registration and authentication
- Project and time entry management
- Per-user and per-project time tracking
- Weekly and project-based reports
- Admin interface

## Requirements

- Python 3.12+
- Django 5.x
- PostgreSQL
- Docker (optional, for containerized deployment)

## Setup (Local)

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd timetracker
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure the database** in `myproject/settings.py` if needed.

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Docker Setup

1. **Build and start the containers:**
   ```sh
   docker-compose up
   ```

2. The app will be available at [http://localhost:8000](http://localhost:8000).

## Usage

- Register a new user or log in.
- Create projects and add time entries.
- View and manage your time entries and projects.

## Running Tests

```sh
docker exec -it timetracker-app-1 bash
python manage.py test
```

**Note:**  
- Default database credentials are set in `docker-compose.yml` and `settings.py`.
- For production, update your environment variables and security settings.
- Included .env for testing submition purposes. For actual, it should be ignored.