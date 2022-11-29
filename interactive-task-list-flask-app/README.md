# Flask Crud App: Task List

## Overview
This app is a basic crud app developed using Flask to simulate managing simple tasks list. In this app, we can create, update, and delete task in a table shown in the interface. The project is mostly developed using Python and HTML, while the data is stored in sqlite.

## Main Requirements
1. Python file for main app definition in Flask
2. Sqlite database
3. HTML file to create interfaces

## Steps

1. Create new virtual environment for this project -> `env` (included in `.gitignore`)
2. Install `requirements.txt`
3. Draft the `app.py`, `base.html`, `index.html`, `update.html` and `main.css` file
4. Create sqlite database in terminal \
    `>>> py` \
    `>>> from app import db` \
    `>>> db.create_all()` \
    `>>> exit()` 
5. Try run `py app.py` and open `http://127.0.0.1:5000/` in a browser or as the command output shown
6. The app should be work to input, update, and remove tasks
