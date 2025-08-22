# Copilot Instructions for ToDoList Django Project

## Project Overview
- This is a Django 5.2.5 project for a To-Do List application.
- Main project package: `todolist/`
- Main app: `tasks/` (created with `python manage.py startapp tasks`)
- Uses SQLite as the default database (see `settings.py`).

## Key Components
- `manage.py`: Entrypoint for all management commands (runserver, makemigrations, migrate, etc).
- `todolist/settings.py`: Project-wide settings, including installed apps, middleware, and database config.
- `todolist/urls.py`: Root URL configuration. Only the admin route is set up by default.
- `tasks/`: App for task management. Contains models, views, admin, and tests.

## Developer Workflows
- **Run the development server:**
  ```
  python manage.py runserver
  ```
- **Make migrations:**
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Run tests:**
  ```
  python manage.py test
  ```
- **Create new app:**
  ```
  python manage.py startapp <appname>
  ```

## Project Conventions
- All new Django apps should be added to `INSTALLED_APPS` in `settings.py`.
- Models are defined in each app's `models.py` and registered in `admin.py` for admin access.
- Views are defined in each app's `views.py` and routed via the project's or app's `urls.py` (not yet present for `tasks`).
- Tests for each app go in `tests.py`.
- No custom user model or authentication logic is present by default.

## Integration Points
- No external APIs or third-party Django apps are integrated yet.
- Static files are served from the default `static/` path.
- The admin interface is enabled at `/admin/`.

## Patterns & Structure
- Follows standard Django project/app structure.
- No nonstandard conventions or custom management commands as of now.
- Example: To add a new model, define it in `tasks/models.py`, run migrations, and register it in `tasks/admin.py`.

## Next Steps
- Implement task models and views in `tasks/`.
- Add app-level `urls.py` for `tasks` and include it in `todolist/urls.py`.
- Add documentation in a `README.md` if project-specific instructions grow.
