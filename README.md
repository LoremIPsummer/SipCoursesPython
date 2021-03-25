# SipCoursesPython

## Introduction

A small CRUD implementation based on **SQLAlchemy** and the **Bottle** webframework with Python.

## Database Configuration

Update your connection details inside the `oracleconn.py` file.

## Usage

1. `cd SipCoursesPython`
1. Create a virtual environment inside this folder. (On Windows, that will be `python3 -m venv .`).
1. Activate it via the `\env\Scripts\activate.bat` script.
1. Run `pip install -r requirements.txt`
1. Create a folder called `oracleclient` inside the project folder. Download the [Oracle x64 Thin Client](https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html) package, and unzip it's content to the `oracleclient` folder.
1. Run `python app.py`.

Your server should be listening on port 13224.

## Endpoints

| METHOD | ENDPOINT                          | DESCRIPTION                                                                                                                          |
| ------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| GET    | localhost:13224/courses           | Returns all of the courses in a json array.                                                                                          |
| GET    | localhost:13224/courses/:crs_code | Returns a single course, or in case of an error, a json object with a single "error" property describing the problem.                |
| POST   | localhost:13224/courses           | Creates a single course and returns it, or in case of an error, a json object with a single "error" property describing the problem. |
| UPDATE | localhost:13224/courses/:crs_code | Updates a single course and returns it, or in case of an error, a json object with a single "error" property describing the problem. |
| DELETE | localhost:13224/courses/:crs_code | Deletes a single course and returns it, or in case of an error, a json object with a single "error" property describing the problem. |
