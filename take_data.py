import requests
import json
import psycopg2

con = psycopg2.connect(database="Margera_exercise",
                          user="postgres",
                          password="1234",
                          host="localhost",
                          port="5433")
con.autocommit = True
print('Connected')

cursor = con.cursor()
sql = '''drop table if exists forecast;  
          create table forecast(
                id bigint PRIMARY KEY, 
                location varchar(30), 
                air_pressure numeric, 
                applicable_date date, 
                created timestamp, 
                humidity smallint, 
                max_temp real, 
                min_temp real, 
                predictability smallint, 
                the_temp real, 
                visibility double precision, 
                weather_state_abbr varchar(2), 
                weather_state_name varchar(16), 
                wind_direction double precision, 
                wind_direction_compass varchar(5), 
                wind_speed double precision);
        '''
cursor.execute(sql)

# create a dictionary of the selected cities
location = {'London': '44418','Los Angeles': '2442047', 'Paris': '615702'}

for city in location:
    print(city)

    # here it selects seven days from 1st to the 7th of april
    for day in range(1,8):
        response = requests.get("https://www.metaweather.com/api/location/"+str(location[city])+"/2021/4/"+str(day)+"/")
        for data in response.json():
            # adds them to the created table after assigning them to variables
            id = data['id']
            air_pressure = data['air_pressure']
            applicable_date = data['applicable_date'].strip('"')
            created = data['created'].strip('"')
            humidity = data['humidity']
            max_temp = data['max_temp']
            min_temp = data['min_temp']
            predictability = data['predictability']
            the_temp = data['the_temp']
            visibility = data['visibility']
            weather_state_abbr = data['weather_state_abbr'].strip('"')
            weather_state_name = data['weather_state_name'].strip('"')
            wind_direction = data['wind_direction']
            wind_direction_compass = data['wind_direction_compass'].strip('"')
            wind_speed = data['wind_speed']

            # cursor execute to enter values to created table in the database
            cursor.execute("insert into forecast values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, city, air_pressure, applicable_date, created, humidity, max_temp, min_temp, predictability, the_temp, visibility, weather_state_abbr, weather_state_name, wind_direction, wind_direction_compass, wind_speed))
