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
1. If you re-run main.py then the database will be reinitialized with the values from fake_data.json. This will cause the database to have duplicate entries. This is a bug and should be fixed.
2. Input validation is not complete, you can enter in weird date formats and the API will accept them with funny results. This is a bug and should be fixed.

# Why I made the design choices I did:
1. Python is as close as you can get to pseudocode in real life. I enjoy it for prototyping 
2. Flask is a nice micro framework for building API's. It is very easy to get started with, and the docs are good 
3. SQLite because it's super easy to use with no setup required. 
4. I used a virtual environment to keep things reproducible. However, I would use docker in a production environment.

Overall I wanted to keep things as simple as possible and get something working quickly, hence the choices above. It's far from a complete solution, but the code is modifiable and the changes I have listed above could be implemented without too much effort. 

# How to run the application:
1. Install python 3.10
2. Activate the virtual environment by running the following command in the root directory of the project: `source env/bin/activate`
3. Run the following command to run the application: `python main.py`

Once you run main.py then the SQLite database will be initialized with the values from fake_data.json. * If you re-run main.py be sure to delete the database.db file first or else you will get duplicate entries in the database. This is a known bug, and it is listed in the known bugs' section above.
