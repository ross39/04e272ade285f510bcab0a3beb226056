# What I would change if I had more time to work on this project:
1. I would use docker to containerize the application and avoid the need to install dependencies on the host machine. It totally eliminates the problem of "it works on my machine".
2. I would not use global select statements to fetch data from the database. "select * from table" is a bad practice. It assumes that programmer is extremely knowledgeable about the fields in the SQL database and assumption is to be avoided at all costs. So I would use specific fields in the select statement.
3. Not use SQL. SQL is fine for most things but for API's a better approach is a graph database. Allows for much more flexibility. Graph databases are also much better for handling relationships between data. Of course there is no free lunch and graph databases have their downsides too. 
4. I would design the API much better. Its quite crude at the moment. Input validation is not done properly. I would use a library like swagger to design the API.
5. Much more robust testing. The current tests are extremely basic and brittle but can be easily extended out and made more flexible. I basically just tested the happy path and not much else. Does this look like json? great, the test passes. Does the result look correct, great the test passes. 
6. Much more robust error handling. The current error handling is very basic and not very useful. I would use a library like sentry to handle errors. I would also return detailed error messages to the user as well as link to a page with more information on the error. Robust error handling is a must for any production application, especially an API
7. Format the dates correctly, this comes back again to the API design. Currently, the dates are entered in the format of DD-MM-YY. 
7. Fix bugs in the code. Please see the below section of known bugs 


# known bugs:
1. If you re-run main.py then the database will be reinitialized with the values from fake_data.json. This will cause the database to have duplicate entries. This is a bug and should be fixed. A fix would be to wrap the database initialization code in a decorator that ensures the function is only run once and only if the database is not already initialized.
2. The tests invoke the main function which leads to database duplication as described above. The fix is relatively straightforward and is described above.
3. Input validation is not complete, you can enter in weird date formats and the API will accept them with funny results. This is a bug and should be fixed.

# Why I made the design choices I did:
1. Python is as close as you can get to pseudocode in real life. I enjoy it for prototyping 
2. Flask is a nice micro framework for building API's. It is very easy to get started with, and the docs are good 
3. SQLite because it's super easy to use with no setup required. 
4. I used a virtual environment to keep things reproducible. However, I would use docker in a production environment.

Overall I wanted to keep things as simple as possible and get something working quickly, hence the choices above. It's far from a complete solution, but the code is modifiable and the changes I have listed above could be implemented without too much effort. 

# How to run the application:
1. Ensure you have python 3 installed 
2. Activate the virtual environment by running the following command in the root directory of the project: `source env/bin/activate` * assumes you are in root directory
3. Install the requirements.txt file using the following command `pip install -r requirements.txt` * assumes you are in root directory
4. Run the following command to run the application: `python main.py`
5. Run the folliwng command to run the tests `python test.py` 

Once you run main.py then the SQLite database will be initialized with the values from fake_data.json. * If you re-run main.py be sure to delete the database.db file first or else you will get duplicate entries in the database. This is a known bug, and it is listed in the known bugs' section above.

# API documentation:
The API is very simple and only used GET requests. However PUT and DELETE and easily be added if more functionality is required. Please see fake_data.json for a layout of the fake data. This fake data is stored and persisted in an sqlite database




| End Point  | What it does |
| ------------- | ------------- |
| http://127.0.0.1:5000/ | home page! |
| http://127.0.0.1:5000/api | sanity check |
| http://127.0.0.1:5000/api/sensors | returns all information about all sensors |
| http://127.0.0.1:5000/api/sensors/int:sensor_id | returns information about sensor 1 or sensor 2 depending on input, so http://127.0.0.1:5000/api/sensors/1 would return all information about sensor 1 
| http://127.0.0.1:5000/api/sensors/int:sensor_id/temperature | returns the average temperature for sensor id 
| http://127.0.0.1:5000/api/sensors/int:sensor_id/humidity | returns the average humidity for sensor id
| http://127.0.0.1:5000/api/sensors/int:sensor_id/humidity/12-07-2023 | returns the average humidity for a sensor id between todays date and a given date(I just happened to use 12-07-2023 as an example, can be any date. use DD-MM-YY format.
| http://127.0.0.1:5000/api/sensors/int:sensor_id/temperature/12-07-2023 | returns the average temperature for a sensor id between todays date and a given date(I just happened to use 12-07-2023 as an example, can be any date. use DD-MM-YY format.
| http://127.0.0.1:5000/api/sensors/int:sensor_id/data/12-07-2023 | returns all data for a given sensor id between todays date and a given date(I just happened to use 12-07-2023 as an example, can be any date. use DD-MM-YY format.

So an example request could be http://127.0.0.1:5000/api/sensors/2/humidity/12-07-2023 which would return the average humidity for sensor 2 between todays date and the given date of 12-07-2023.
