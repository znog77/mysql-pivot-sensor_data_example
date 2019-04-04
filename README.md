# mysql-pivot-sensor_data_example

A simple example for pivoting (I undesrtand that's how this is called) a table on MySQL I made for some friends. If it may be useful to you, go ahead...

generate_data.py
	Will generate a set of fake data corresponding to fake sensors to a local MySQL server, creating the DB and tables. Requires some python modules.
generate_sensor_pivot_query.py
	Will print the pivoting query to the console output, should run on any python installation.
example_db.sql
	In case you just want to use the DB run this one, instead of the python script.
