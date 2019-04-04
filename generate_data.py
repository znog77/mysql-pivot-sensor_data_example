#!/usr/bin/env python3

import mysql.connector
import random
import datetime

locations = ['Agrelo (Argentina)','Agua Escondida','Alto del Olvido',\
    'Alto Salvador','Alto Verde (Mendoza)','Andrade (Mendoza)',\
    'Bardas Blancas','Barrancas (Maipú)','Barrio ADINA',\
    'Barrio Belgrano Norte','Barrio Chivilcoy',\
    'Barrio Cooperativa Los Campamentos','Barrio Echeverría',\
    'Barrio El Nevado','Barrio Empleados de Comercio','Barrio Intendencia',\
    'Barrio Jesús de Nazaret','Barrio Jocolí II','Barrio La Esperanza',\
    'Barrio Las Rosas','Barrio Los Jarilleros','Barrio María Auxiliadora',\
    'Barrio Perdriel IV','Barrio Primavera','Barrio Rivadavia (Mendoza)',\
    'Barrio San Cayetano (Mendoza)','Barrio Tres Olivos',\
    'Blanco Encalada (Mendoza)','Bowen','Cacheuta','Campo de los Andes',\
    'Capdevilla','Capitán Montoya','Carmensa','Chacras de Coria',\
    'Chapanay','Chilecito (Mendoza)','Chivilcoy (Mendoza)',\
    'Colonia Las Rosas','Colonia Segovia','Cordón del Plata (Tupungato)',\
    'Costa de Araujo','Costa El Toledano','Costa Flores',\
    'Cruz de Piedra (Mendoza)','Cuadro Benegas','Cuadro Nacional',\
    'Cuadro Ortega','Desaguadero (Mendoza-San Luis)',\
    'Doce de Octubre (Mendoza)','El Carmelo (Argentina)',\
    'El Carrizal (Argentina)','El Central','El Cepillo','El Challao',\
    'El Manzano Histórico','El Marcado','El Mirador (Argentina)',\
    'El Nihuil','El Paramillo','El Pedregal (Argentina)',\
    'El Peral (Argentina)','El Plumerillo','El Retamo','El Salto (Mendoza)',\
    'El Sosneado','El Tropezón','El Vergel','Estación Polvaredas (Mendoza)',\
    'Eugenio Bustos','General Alvear (Mendoza)','Goudge','Ingeniero Giagnoni',\
    'Ingeniero Gustavo André','Jaime Prats','Jocolí','Jocolí Viejo',\
    'Junín (Mendoza)','La Arboleda (Argentina)','La Central (Mendoza)',\
    'La Colonia (Mendoza)','La Consulta','La Dormida',\
    'La Esperanza (Mendoza)','La Florida (Mendoza)','La Libertad (Argentina)',\
    'La Llave (Argentina)','La Palmera (Argentina)','La Paz (Mendoza)',\
    'La Pega','La Reducción (Mendoza)','Lagunas de Bartoluzzi',\
    'Las Carditas','Las Catitas','Las Compuertas','Las Cuevas','Las Leñas',\
    'Las Malvinas (Mendoza)','Las Paredes (Mendoza)','Las Vegas (Mendoza)',\
    'Las Violetas (Mendoza)','Los Árboles','Los Barriales','Los Campamentos',\
    'Los Charabones','Los Compartos','Los Corralitos','Los Penitentes',\
    'Los Reyunos (localidad)','Los Sauces (Mendoza)','Malargüe',\
    'Manantiales (Mendoza)','Medrano (Argentina)','Monte Comán (Mendoza)',\
    'Montecaseros','Mundo Nuevo','Nueva California (Argentina)',\
    'Palmira (Argentina)','Papagayos (Mendoza)','Pareditas',\
    'Perdriel (Mendoza)','Phillips','Piedras Blancas (Mendoza)',\
    'Pobre Diablo (Argentina)','Polvaredas (Mendoza)',\
    'Potrerillos (Mendoza)','Puente de Hierro (Argentina)',\
    'Puente del Inca (localidad)','Punta de Vacas',\
    'Punta del Agua (Mendoza)','Rama Caída','Real del Padre',\
    'Rivadavia (Mendoza)','Rodeo del Medio','Rodríguez Peña (Mendoza)',\
    'Russell (Argentina)','Salto de las Rosas','San Isidro (Mendoza)',\
    'San José (Tupungato)','San Martín (Mendoza)','San Roque (Mendoza)',\
    'Santa María de Oro','Santa Rosa (Mendoza)','Tres de Mayo',\
    'Tres Esquinas (Luján de Cuyo)','Tres Esquinas (Mendoza)',\
    'Tres Porteñas','Tunuyán','Ciudad de Tupungato',\
    'Ugarteche (Mendoza)','Uspallata','Valle del Sol (Argentina)',\
    'Vallecitos','Villa Antigua','Villa Atuel','Villa Atuel Norte',\
    'Villa Bastías','Villa El Refugio','Villa San Carlos (Mendoza)',\
    'Villa Teresa (Argentina)','Villa Tulumaya','Villa Veinticinco de Mayo',\
    'Vista Flores','Vistalba']

MAX_SENSORS = 10
N_INSTRUMENTS = 25

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS sensor_pivot_experiment")

mycursor.execute("USE sensor_pivot_experiment")

mycursor.execute("DROP TABLE IF EXISTS instruments")

mycursor.execute("CREATE TABLE instruments (\
    id varchar(8) NOT NULL,\
    location varchar(45),\
    n_sensors int,\
    PRIMARY KEY (id)\
    );")

mycursor.execute("DROP TABLE IF EXISTS measurements")

mycursor.execute("CREATE TABLE measurements (\
    instrument_id varchar(8),\
    t timestamp,\
    sensor varchar(4),\
    value float\
    );")

mycursor.execute('DELETE FROM instruments')

for i in range(N_INSTRUMENTS):
    mycursor.execute('INSERT INTO instruments (id,location,n_sensors) VALUES (%s,%s,%s)',(
        "%08X" % int(2**32*random.random()),\
        locations[int(len(locations)*random.random())],\
        int(MAX_SENSORS*random.random()))\
        )
    mydb.commit()

mycursor.execute("SELECT * FROM instruments")
instruments = mycursor.fetchall()

#Start one hour ago
t_now = datetime.datetime.now()
t_0 = t_now+datetime.timedelta(hours=-1)
t = t_0
#Move to now in steps of:
dt = datetime.timedelta(seconds=10)

while t < t_now:
    for instrument in instruments:
        #e.g.: mandatory battery meassurement on S0
        sensor = 'S0'
        value = 12.1+random.random()/8.0
        mycursor.execute('INSERT INTO measurements (instrument_id,t,sensor,value) VALUES (%s,%s,%s,%s)',\
            (instrument[0], t, sensor, value))
        #Random meassurements, 0 to 3.3V
        for sensor in range(1,instrument[2]):
            if random.random() > 0.25:
                sensor = 'S'+str(sensor)
                value = str(0+3.3*random.random())
                mycursor.execute('INSERT INTO measurements (instrument_id,t,sensor,value) VALUES (%s,%s,%s,%s)',\
                        (instrument[0], t, sensor, value))
    t += dt
    mydb.commit()
