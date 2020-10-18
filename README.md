# About api Redes
Requirement before install project:
--
  1. Install python 3^
  2. Install virtualenv

## Environment preparation
The next commands should by executing in terminal inside directory 
```api-salud```
steps:
- create file ```.env``` and copy content of the ```base.env```
  and past inside ```.env```, set up the variable with their credentials.
  - table variable ```base.env```.
  
  | Name             | Description                    | example value   |
  |------------------|--------------------------------|:---------------:|
  | DATABASE_NAME    | The name of database           | example         |
  | DATABSE_PASSWORD | The password of database       | root            |
  | DATABASE_USER    | The username of the database   | root            |
  | DATABASE_SERVER  | The address of database server | localhost       |

- ```pip install virtualenv```
- ```virtualenv .```
- active virtual environment with commands:
  - windows ```/Scripts/activate.bat```
  - mac and linux ```source env/bin/activate```
-  ```pip install```
- execute ```python run.py``` and open youre explorer in ```localhost:5000```