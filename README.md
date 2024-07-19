# Choose Your Own Adventure Backend

This is a backend implementation for a choose-your-own-adventure style app. The backend includes a web application server exposing an API, a PostgreSQL database for persistence, and an environment for running the project with Docker Compose.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

## Important commands

1. `make build` - build containers
1. `make run` - run containers
1. `make setup` - run setup script
1. `make makemigraitons` - run `python manage.py makemigrations` in bash shell
1. `make migrate` - run `python manage.py migrate` in bash shell

## API Notes

- Stories API is protected via DRF's `Token Authentication` authentication class
- Story primary key is an auto-generated UUID
- Frames can be access via a nested model viewset
  - Use `index` value to view Frame detail API
- `opensesame` token can be used after running `make setup` command

### Example API Calls:

- cURL for Story API

```curl
curl -H "Authorization: Token opensesame" http://localhost:8000/api/stories/
```

- cURL for nested Frame API

```curl
curl -H "Authorization: Token opensesame" http://localhost:8000/api/stories/e1b9224e-8973-4394-97d4-a999e916540b/frames/
```

- cURL for nested Frame Detail API via `index`

```curl
curl -H "Authorization: Token opensesame" http://localhost:8000/api/stories/e1b9224e-8973-4394-97d4-a999e916540b/frames/4/
```

---

- How to navigate nested API's:

```
GET /api/stories/e1b9224e-8973-4394-97d4-a999e916540b/frames/4/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 5,
    "buttons": [
        {
            "id": 7,
            "created": "2024-07-19T21:09:55.828853Z",
            "modified": "2024-07-19T21:21:11.889344Z",
            "text": "Start Over",
            "link_index": 0,
            "frame": 5
        }
    ],
    "created": "2024-07-19T21:09:55.827763Z",
    "modified": "2024-07-19T21:21:11.888156Z",
    "index": 4,
    "title": "No Return",
    "body": "<p>You close your eyes, and drift into sleep. When you awaken, you are in your own bed. The previous events were a dream, which has already begun to fade.</p><p>You spend the rest of your life trying to return to the winding path in the dark forest.</p><p><b>You never will.</b></p>",
    "img": "http://example.com/img/10.png",
    "colors": {
        "bg": "#E0072F",
        "text": "#680013"
    },
    "story": "e1b9224e-8973-4394-97d4-a999e916540b"
}
```

## TODO

1. add test coverage via `pytest` / `pytest-django`
1. add type annotations to all methods, classes, functions, etc.
1. add docstrings to all methods, classes, functions, etc.
1. add UI
