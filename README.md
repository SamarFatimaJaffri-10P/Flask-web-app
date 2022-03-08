# Flask-web-app
A flask web application to store books information in the PostgreSQL database

## Run app
For running the application do the following
- Open the terminal
- Run the command `flask run`
- The app should start

## Create database
For creating a **PostgreSQL** database do the following
- Goto PostgreSQL shell by running the command `psql` in the shell
- In the shell create database by running `CREATE DATABASE database_name;` i.e.,
  ```
  CREATE DATABASE books_store;
  ```
- If the database already exist, run the command `DROP DATABASE database_name;` i.e.,
  ```
  DROP DATABASE books_store;
  ```

## Create Environment variables
Save the confidential information such as APP_SETTING and DATABASE_URL in Environment variables.
- Export APP_SETTING variable by `export APP_SETTINGS="config.DevelopmentConfig"`
- And DATABASE_URL variable by `export DATABASE_URL="postgresql://username:password@localhost:5432/books_store"`
- Or simply create a file as `.env` and save the information in it i.e.,
 ```
 export APP_SETTINGS="config.DevelopmentConfig"
 export DATABASE_URL=export DATABASE_URL="postgresql://username:password@localhost:5432/books_store"
 ```

## Make Migrations
- Run the command `flask db init` to create a folder name migration in the project folder to migrate using these files
- Make the migrations by `flask db migrate`
- Run `flask db upgrade` to apply the migrations
If migration fails try running `DROP TABLE alembic_version;`

## View Tables
- View the table name by starting the shell by running `psql` in the terminal
- Run `\c books_store` to connect with books_store database.
- Run `\dt` to see all the relations
- Run `\d books` to view the books table structure

## Different pages
- Home page is at `http://127.0.0.1:5000/`
- Add page let use add book by `http://127.0.0.1:5000/add?name=book_name&author=author_name&published=publishing_year`
- Get page let user get any book record by id i.e., `http://127.0.0.1:5000/get/1` will return the book data with id 1
- Get all page let user get all the records by `http://127.0.0.1:5000/getall`
- Add form let the user add the book data into database through HTML template. It can be accessed through `http://127.0.0.1:5000/add/form`
