# Misinfovote

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
