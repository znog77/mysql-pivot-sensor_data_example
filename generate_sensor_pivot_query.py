#!/usr/bin/env python	
l = []
for i in range(0,11):
    l.append('\tAVG(CASE WHEN sensor = \'S'+str(i)+'\' THEN ROUND(value,3) END) S'+str(i)) 
sql_select = 'SELECT instrument_id,\n'
sql_from = 'FROM measurements GROUP BY instrument_id;'
print(sql_select+',\n'.join(l)+'\n'+sql_from)
