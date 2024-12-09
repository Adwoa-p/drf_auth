# API Documentation
This API allows users to sign in, sign up and test tokens generated.

**Endpoints**
1. POST Sign up
  Endpoint: /signup/
  Method: POST
  Description: Allows user to sign up with username, password and email.
*Example Request*
GET   http://127.0.0.1:8000/signup
Body:
    [
        {
            "username": "John",
            "password": "1234pass",
            "email": "john@gmail.com"
        }
       ]
*Example Response*
Status: 200 OK
Body:
[
    {
        "token": "fbf32dc0321d15f8509eaa99c33afe26abb00e17",
        "user": {
            "id": 3,
            "username": "John",
            "password": "1234pass",
            "email": "john@gmail.com"
            }
    }
       ]
   
2. POST Log in
  Endpoint: /login/
  Method: POST
  Description: Allows an existing user to log in.
*Example Request*
POST   http://127.0.0.1:8000/login
Body:
    [
        { 
            "username": "John",
            "password": "1234pass"
        }
       ]
*Example Response*
Status: 200 OK
Body:
    [
        {
    "token": "fbf32dc0321d15f8509eaa99c33afe26abb00e17",
    "user": {
        "id": 3,
        "username": "John",
        "password": "pbkdf2_sha256$870000$w3BT7b5bAnFosnZEv6xmLP$Ct6uuUhOOejFXatFzhr0vKuj9/YHkey9qPImt3yDuRs=",
        "email": "john@gmail.com"
    }
}
       ]

3. GET  Token
  Endpoint: /test_token/
  Method: POST
  Description: Tests token to validate user and sends user email as response.
*Example Request*
GET   http://127.0.0.1:8000/test_token/
Body:
     {
            "book_title": "The Annointing",
            "book_author": "Benny Hinn"
        }
*Example Response*
Status: 201 CREATED
Body:
    [
        {
            "book_id": 3,
            "book_title": "The Annointing",
            "book_author": "Benny Hinn"
        }
       ]