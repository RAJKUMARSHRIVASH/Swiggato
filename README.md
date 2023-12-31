# Swiggato KhanaMangao.com
This is a food ordering and delivery app where any user can use this app to order or deliver the food that customers want.

## Folder Structure
```
swiggato/
├── my_env/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── assets/
│   ├── templates/
│   │   ├── base.html
│   │   ├── add_dish.html
│   │   ├── edit_dish.html
│   │   ├── menu.html
│   │   ├── new_order.html
│   │   ├── order.html
│   │   ├── review_orders.html
│   │   ├── order_status.html
│   │   └── ...
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── migrations/
├── config.py
├── requirements.txt
├── app.py
└── README.md


```
Let's go through each component briefly:

1. `app/`: This directory will contain all the application-specific code.
  - `static/`: This directory will store static files like CSS stylesheets, JavaScript files, and images.
  - `templates/`: This directory will contain HTML templates for different pages of the web application.
  - `__init__.py`: This file initializes the Flask application and sets up the database connection.
  - `models.py`: This file defines the database models and schema using an Object-Relational Mapping (ORM) library like `SQLAlchemy`.
  - `routes.py`: This file defines the Flask routes that handle different HTTP requests and render appropriate templates.
  - `utils.py`: This file can contain utility functions and helper methods used throughout the application.
2. `migrations/`: This directory will store database migration files generated by a migration tool like Flask-Migrate.
3. `config.py`: This file holds the configuration variables for the application, such as database connection details, secret keys, etc.
4. `requirements.txt`: This file lists all the dependencies required for the project. You can install them using `pip install -r requirements.txt`.
5. `app.py`: This file is used to run the Flask development server.
6. `README.md` This is a readme file.
7. `my_env`: This is `virtualenv` file, The procedure to create this has been given later below.


## Features

- Cross-platform
- Responsive

## Tech Stack

**Frontend:** HTML, CSS, JavaScript

**Backend:** Python, Flask

## Run Locally

Clone the project

```bash
  git clone https://github.com/RAJKUMARSHRIVASH/Swiggato.git
```

Go to the project directory

```bash
  cd Swiggato
```

Install dependencies

```bash
  pip freeze > requirements.txt
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
## **How to Set Up a Virtual Environment in Python**

Here are the steps to create a virtual environment in Python:
1. Install the `virtualenv` package:
```
pip install virtualenv
```
2. Navigate to your project directory and create a virtual environment. Here,`my_env` is the name of the virtual environment.
```
cd my_project/ virtualenv my_env
```
3. Now, you have to activate the virtual environment. On `macOS` and `Linux`, you can do this:
```
source my_env/bin/activate
```
On `Windows`:
```
my_env\Scripts\activate
```
4. After the activation, your terminal prompt will change to show the name of the activated environment.

Now, you can install packages into this isolated environment. For example:
```
pip install flask
```
This will install Flask in the **`my_env`** environment, not in your global Python environment. All Python commands like **`python`**, **`pip`**, etc., used in this environment will apply to **`my_env`** only.

1. When you're done with your work, you can deactivate the environment to return to your global Python environment:
```
deactivate
```

Start the server

```bash
  python app.py
```

Open the app on a browser locally
```
http://localhost:5000/
```

## API Reference

#### Welcome 

```http
  GET /
```

#### POST

```http
  POST /
```

## Demo
```
https://swiggato.onrender.com/
```
## Screenshots

![App Screenshot](https://i.imgur.com/WRediW3.jpeg)

## Author

- [@Raj Kumar Sen](https://github.com/RAJKUMARSHRIVASH)

