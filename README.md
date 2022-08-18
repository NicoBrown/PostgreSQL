# PostgreSQL

The project is just some practice in PostgreSQL and the temrinal.

It uses the [Chinook database](https://github.com/lerocha/chinook-database)

Ive added some GUI elements to take user inputs as part of the project from [PYtermGUI](https://github.com/bczsalba/pytermgui) and display the reuslts in the terminal.

![image](https://user-images.githubusercontent.com/69271605/185363212-92426cea-59a3-41ef-835d-4b848675f1c2.png)

## accessing the db

To connect to the db you'll need to run these commands before running the python script
`set_pg`
`psql`
`\c chinook`
`\q`

```
gitpod /workspace/PostgreSQL (main) $ set_pg
gitpod /workspace/PostgreSQL (main) $ psql
psql (12.12 (Ubuntu 12.12-1.pgdg20.04+1))
Type "help" for help.

postgres=# \c chinook
You are now connected to database "chinook" as user "gitpod".
chinook=# \q
gitpod /workspace/PostgreSQL (main) $ 
```
then you can simply run the python file as usual
`python3 sql-psycopg2.py`

and then the terminal will appear for the user input.
