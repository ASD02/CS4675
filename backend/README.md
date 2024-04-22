# MisinfoVote - Backend

## Setup

Download the model weights from the following link [https://drive.google.com/file/d/1khpMMs_Ui9WuK0CKt_qiYYstnB9aGzj0/view?usp=sharing](https://drive.google.com/file/d/1khpMMs_Ui9WuK0CKt_qiYYstnB9aGzj0/view?usp=sharing) and unzip them in this directory as `bert-model`.

Set the following environment variables for the database connection:

| Environment Variable | Comment |
| - | - |
| DB_USER | Username for database user |
| DB_PASSWORD | Password for database user |
| DB_ENDPOINT | Endpoint for database connection |
| DB_NAME | Name of the database |

### [Optional - Recommended] Using a virtual environment

Install and setup virtual environment

```
pip install virtualenv
virtualenv venv
```

To activate your virtualenv

```
source ./venv/bin/activate
```

To exit the virtual environment

```
deactivate
```

### App setup

Install the required dependencies

```
pip install -r requirements.txt
```


## Running the app

```
flask --app misinfovote run
```
The app will run on `localhost:5000`


## API Documentation

The following endpoints are exposed:

| Endpoint | Method | Request Body (JSON fields) | Comment |
| - | - | - | - |
| /score/<post_id> | GET | None | Get the trust score of a post |
| /vote | POST | post_id, user_id, vote | Vote on a particular post. User ID is for the voter, vote (string) can be either -1 or 1 |
| /posts/<post_id> | PUT | text, user_id | Create a new post |
| /users/<user_id> | PUT | None | Create a new untrusted user |
| /trust/<user_id> | POST | isTrusted (bool) | Trust an untrusted user |

If any of the required request body fields are missing, the response will be an HTTP 400.