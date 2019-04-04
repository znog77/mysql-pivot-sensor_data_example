# mysql-pivot-sensor_data_example

A simple example for pivoting (I undesrtand that's how this is called) a table on MySQL I made for some friends. The code is not elegant at all, it is even probable some people may find my coding offensive... sorry about that.

Anyway, if it may be useful to you, go ahead...

generate_data.py
	Will generate a set of fake data corresponding to fake sensors at random locations (from the province I live in) to a local MySQL server, creating the DB and tables. Requires some python modules.
generate_sensor_pivot_query.py
	Will print the pivoting query to the console output, should run on any python installation.
example_db.sql
	In case you just want to use the DB run this one, instead of the python script.

Pivoting will turn something like this:
+---------------+---------------------+--------+-----------+
| instrument_id | t                   | sensor | value     |
+---------------+---------------------+--------+-----------+
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
+---------------+---------------------+--------+-----------+

Into this:
+---------------+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------+------+
| instrument_id | S0         | S1        | S2        | S3        | S4        | S5        | S6        | S7        | S8        | S9   | S10  |
+---------------+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------+------+
| 1ADD0E77      | 12.1627722 | 1.5978222 | 1.5330076 | 1.7251119 | 1.6234457 | 1.5400913 | 1.6996420 | 1.5647653 | 1.6501444 | NULL | NULL |
| 1E8345D6      | 12.1620667 | 1.6102583 | 1.6569551 | 1.5977422 |      NULL |      NULL |      NULL |      NULL |      NULL | NULL | NULL |
| 1F695491      | 12.1616556 | 1.7211417 | 1.7379767 | 1.6774170 | 1.5876058 | 1.5639228 | 1.6380611 | 1.6523613 | 1.6011081 | NULL | NULL |
| 2CC54C6E      | 12.1610611 | 1.6779151 | 1.6211792 | 1.7146970 | 1.5893410 | 1.6595904 | 1.6958248 |      NULL |      NULL | NULL | NULL |
+---------------+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+------+------+

