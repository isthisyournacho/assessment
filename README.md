# Assessment

This is a python script which acts as a restful API to a sqllite database.  There are some assumptions the application accessing the data would handle.

### Files

 - oasis.db - sqlite db
 - server.py - assessment server that runs the api on port 5002
 - Assessment.postman_collection.json - A postman import to test the script, when running

### Endpoints

  - /questions - GET all the questions
  - /users - POST user
  - /tests - POST test/session

### Installation

Assessment requires Flask to run.

Install the flask via pip (On Mac)

```sh
$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
```
More instructions at: http://flask.pocoo.org/docs/1.0/installation/

Run the server:

```sh
$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
```

### Endpoint Details

#### Questions
/questions - GET all the questions

Example Request (Get):
http://127.0.0.1:5002/questions

Example Response:
{"questions": [{"id": 1, "question": "What is up?", "correctAnswer": "Not Down.", "incorrectAnswer1": "Down", "incorrectAnswer2": "Blue"}, {"id": 2, "question": "What is east?", "correctAnswer": "Not West.", "incorrectAnswer1": "West", "incorrectAnswer2": "Zelda"}, {"id": 3, "question": "What's the meaning of life?", "correctAnswer": "42", "incorrectAnswer1": "No one knows", "incorrectAnswer2": "Zoidberg"}]}

#### Users
/users - POST user

Example Request (Post):
http://127.0.0.1:5002/users

JSON Body:

```json
{
	"last_name":"Losey",
	"first_name":"Doug",
	"email":"douglosey@gmail.com"
}
```

Example Response:
```json
{
    "status": "success",
    "sessionId": "c8650a8d-8c0d-4acf-a546-3ec9aa731aee"
}
```

#### Tests

/tests - POST test

Example Request (Post):
http://127.0.0.1:5002/tests

JSON Body:
```json
{
	"sessionId": "test-data",
	"userId": "test-user",
	"answer1": "test-answer1",
	"answer2": "test-answer2",
	"answer3": "test-answer-3"
}
````
Example Response:
```json
{
    "status": "Success - Final Assessment Questions have been Submitted!"
}
```
