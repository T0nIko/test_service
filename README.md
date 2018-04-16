# Test Service

## Requirements

* Python3 & Python3 dev(e.g. `...-dev`) packages
* pip3
* SQLite3

#### Python dependencies
* Flask
* SQLAlchemy
* Gunicorn

## Installation
It's quite simple:
```bash
cd path_project_root
chmod +x setup.sh
./setup.sh

```

## Usage
There are 2 intended scenarios how to start the app:
1. Run it with flask dev server
2. Run it with gunicorn by executing `run_app.sh`

## API specification

#### Users

##### Request

| Method |     URL    |              Parameters                                                | Response |
|:------:|:----------:|:----------------------------------------------------------------------:|:--------:|
|  POST  |api/v1/users|`int` id, `string` first_name, `string` middle_name, `string` last_name | A list of User object filtered by request params.<br>Example response: <br>[{<br>"first_name": "test1", <br>"id": 2, <br>"last_name": "test1", <br>"middle_name": "test1"<br>}]|

