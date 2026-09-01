# Django Project Setup Guide

This guide contains all the essential commands from creating a brand new Django project to running it on your local server.

## 1. Virtual Environment Setup

First, it is always recommended to create a virtual environment to manage dependencies for your project.

**Create a virtual environment:**
```powershell
python -m venv myenv
```

**Activate the virtual environment (Windows):**
```powershell
.\myenv\Scripts\activate
```
*(When activated, you will see `(myenv)` at the beginning of your terminal prompt.)*

## 2. Install Django

Once the virtual environment is active, install Django using pip:
```powershell
pip install django
```

## 3. Create Django Project and App

**Create a new Django project:**
```powershell
django-admin startproject myproject .
```
*(The dot `.` at the end ensures the project is created in the current directory instead of nesting it in another folder.)*

**Create a new app inside the project:**
```powershell
python manage.py startapp homepage
```
*(Don't forget to add your new app `'homepage'` to the `INSTALLED_APPS` list in `myproject/settings.py`!)*

## 4. Run the Development Server

Whenever you want to start the project, make sure your virtual environment is active, then run:
```powershell
python manage.py runserver
```
Your site will be live at `http://127.0.0.1:8000/`. To stop the server, press `Ctrl + C` in the terminal.

## 5. Database Migrations

When you create new database tables or setup the project for the first time, you need to apply migrations:
```powershell
python manage.py makemigrations
python manage.py migrate
```

## 6. Git and GitHub Commands

To save your code to GitHub, use these commands:
```powershell
# Check changed files
git status

# Add all changes
git add .

# Commit changes
git commit -m "Update code"

# Push to Github 
git push origin main
```
*(We already created a `.gitignore` file in your project so that the `myenv` folder and `db.sqlite3` are not uploaded to GitHub.)*
