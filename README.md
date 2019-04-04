# mysql-pivot-sensor_data_example

A simple example for pivoting (I undesrtand that's how this is called) a table on MySQL I made for some friends. The code is not elegant at all, it is even probable some people may find my coding offensive... sorry about that.

Anyway, if it may be useful to you, go ahead...

This will generate a set of fake data corresponding to fake sensors at random locations (from the province I live in) to a local MySQL server, creating the DB and tables. Requires some python modules.	

	generate_data.py
	
This one Will print the pivoting query to the console output, should run on any python installation.

	generate_sensor_pivot_query.py

In case you just want to use the DB run this one, instead of the python script.

	example_db.sql

Or just look at the query to make the pivot hapen:

	pivot_sensor_data.sql


Pivoting will turn something like this:

| instrument_id | t                   | sensor | value     |
|---------------|---------------------|--------|-----------|
| 1ADD0E77      | 2019-04-03 21:50:38 | S0     |   12.1231 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S1     |  0.569794 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S3     |   3.20848 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S4     |   2.74889 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S5     |   1.99229 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S6     |    3.0099 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S7     |   2.97097 |
| 1ADD0E77      | 2019-04-03 21:50:38 | S8     |  0.814045 |
| 1E8345D6      | 2019-04-03 21:50:38 | S0     |   12.1238 |
| 1E8345D6      | 2019-04-03 21:50:38 | S1     |   1.99914 |
| 1E8345D6      | 2019-04-03 21:50:38 | S2     |   1.61574 |
| 1F695491      | 2019-04-03 21:50:38 | S0     |   12.2204 |
| 1F695491      | 2019-04-03 21:50:38 | S2     |    2.5713 |
| 1F695491      | 2019-04-03 21:50:38 | S3     |   2.61073 |
| 1F695491      | 2019-04-03 21:50:38 | S4     |  0.430675 |
| 1F695491      | 2019-04-03 21:50:38 | S5     | 0.0701951 |
| 1F695491      | 2019-04-03 21:50:38 | S7     |  0.348648 |
| 2CC54C6E      | 2019-04-03 21:50:38 | S0     |   12.1381 |
| 2CC54C6E      | 2019-04-03 21:50:38 | S1     |   1.48438 |
| 2CC54C6E      | 2019-04-03 21:50:38 | S2     | 0.0358494 |

Into this:

| instrument_id | S0       | S1      | S2      | S3      | S4      | S5      | S6      | S7      | S8      | S9   | S10  |
|---------------|----------|---------|---------|---------|---------|---------|---------|---------|---------|------|------|
| 1ADD0E77      | 12.17722 | 1.59782 | 1.53300 | 1.72511 | 1.62344 | 1.54009 | 1.69964 | 1.56476 | 1.65014 | NULL | NULL |
| 1E8345D6      | 12.10667 | 1.61025 | 1.65695 | 1.59774 |    NULL |    NULL |    NULL |    NULL |    NULL | NULL | NULL |
| 1F695491      | 12.16556 | 1.72114 | 1.73797 | 1.67741 | 1.58760 | 1.56392 | 1.63806 | 1.65236 | 1.60110 | NULL | NULL |
| 2CC54C6E      | 12.10611 | 1.67791 | 1.62117 | 1.71469 | 1.58934 | 1.65959 | 1.69582 |    NULL |    NULL | NULL | NULL |


