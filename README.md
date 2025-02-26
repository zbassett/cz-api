# CurlingZone API

A comprehensive RESTful API for accessing curling data including events, tournaments, teams, players, and games.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Overview

The CurlingZone API provides programmatic access to curling data, allowing developers to build applications that track curling events, teams, players, and game statistics. The API follows RESTful principles and returns data in JSON format.

### Key Features

- **Events & Tournaments**: Access data about curling events and tournaments worldwide
- **Teams & Players**: Get information about teams and individual players
- **Games & Scores**: Retrieve game data, including scores and results
- **Live Data**: Find out what games and events are happening right now
- **Statistics**: Access player and team statistics

### API Documentation

Interactive API documentation is available at these endpoints after starting the server:

- **Swagger UI**: `/api/docs/` - Interactive documentation with "Try it out" capability
- **ReDoc**: `/api/redoc/` - Clean, organized API documentation
- **OpenAPI Schema**: `/api/schema/` - Raw OpenAPI specification in JSON format

## API Endpoints

### Core Resources

- `/api/events/` - Curling events
- `/api/tournaments/` - Tournament information
- `/api/teams/` - Curling teams
- `/api/players/` - Player information
- `/api/scoregames/` - Game data and scores
- `/api/tournamentgames/` - Games associated with tournaments

### Convenience Endpoints

- `/api/current-events/` - Events happening now
- `/api/upcoming-events/` - Events starting in the next 30 days
- `/api/live-games/` - Games currently in progress
- `/api/recent-results/` - Recently completed games
- `/api/event-schedule/?event_id={id}` - Schedule for a specific event
- `/api/player-stats/?player_id={id}` - Statistics for a specific player
- `/api/team-stats/?team_id={id}` - Statistics for a specific team
- `/api/standings/?event_id={id}` - Standings for a specific event

## Settings

Detailed settings documentation moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy cz_api

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Local Docker Setup

To run the API locally using Docker:

1. Clone this repository:
   ```
   git clone https://github.com/your-username/cz-api.git
   cd cz-api
   ```

2. Start the Docker containers:
   ```
   docker-compose up -d
   ```

   This will spin up two containers:
   - MySQL - Database containing curling data
   - Django - API server

3. The API should now be available at:
   - API Root: http://localhost:8000/api/
   - API Documentation: http://localhost:8000/api/docs/

### Data Access Notes

- The database has been pre-populated with curling data from CurlingZone
- All API endpoints are **read-only** to ensure data integrity
- The API is designed for integration with front-end applications and other services

### Example API Usage

#### Using cURL:

```bash
# Get list of current events
curl -X GET "http://localhost:8000/api/current-events/" -H "accept: application/json"

# Get player details
curl -X GET "http://localhost:8000/api/players/12345/" -H "accept: application/json"
```

#### Using JavaScript:

```javascript
// Fetch current events
fetch('http://localhost:8000/api/current-events/')
  .then(response => response.json())
  .then(data => console.log(data));

// Get team stats
fetch('http://localhost:8000/api/team-stats/?team_id=123')
  .then(response => response.json())
  .then(data => console.log(data));
```
