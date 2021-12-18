from db import db


class Forecast:

    def __init__(self, row):
        # creates class and parameters so an obj can be created and formatted correctly when needed
        self.id = row[0]
        self.location = row[1]
        self.air_pressure = row[2]
        self.applicable_date = row[3]
        self.created = row[4]
        self.humidity = row[5]
        self.max_temp = row[6]
        self.min_temp = row[7]
        self.predictability = row[8]
        self.the_temp = row[9]
        self.visibility = row[10]
        self.weather_state_abbr = row[11]
        self.weather_state_name = row[12]
        self.wind_direction = row[13]
        self.wind_direction_compass = row[14]
        self.wind_speed = row[15]

    def toJson(self):
        # creates a toJson function so the data are properly uploaded in the api in json formatting
        return {
            "id": self.id,
            "location": self.location,
            "air_pressure": self.air_pressure,
            "applicable_date": self.applicable_date.strftime("%d/%m/%Y"),
            "created": self.created.strftime("%d/%m/%Y, %H:%M:%S"),
            "humidity": self.humidity,
            "max_temp": self.max_temp,
            "min_temp": self.min_temp,
            "predictability": self.predictability,
            "the_temp": self.the_temp,
            "visibility": self.visibility,
            "weather_state_abbr": self.weather_state_abbr,
            "weather_state_name": self.weather_state_name,
            "wind_direction": self.wind_direction,
            "wind_direction_compass": self.wind_direction_compass,
            "wind_speed": self.wind_speed
        }

    @staticmethod
    def selectAll():
        # creates a query that prints all the values of the table
        return [Forecast(row) for row in db.query("select * from forecast")]

    @staticmethod
    def selectAllTemp():
        # creates a query that Lists the latest forecast for each location for every day
        results = []
        for city in ['London', 'Los Angeles', 'Paris']:
            for day in range(1, 8):
                query = '''
                           select * 
                           from forecast 
                           where location = %s and applicable_date = '2021-04-%s'
                           order by 4 desc limit 1 '''
                results.extend([Forecast(row) for row in db.query(query, (city, day))])
        return results

    @staticmethod
    def selectThe_Temp():
        # Lists the average the_temp of the last 3 forecasts for each location for every day
        result = []
        for city in ['London', 'Los Angeles', 'Paris']:
            for day in range(1, 8):
                query = '''
                        select tmp.location, tmp.applicable_date , avg(tmp.the_temp) 
                        from(select * 
                            from forecast 
                            where location = %s and applicable_date = '2021-04-%s' 
                            order by 4 desc limit 3) as tmp 
                        Group by tmp.location, tmp.applicable_date
                        '''
                for location, applicable_date, avg in db.query(query, (city, day)):
                    result.append({
                        "location": location,
                        "applicable_date": applicable_date.strftime("%d/%m/%Y"),
                        "avg": avg
                    })
        return result

    @staticmethod
    def selectTopMetric(n):
        # Get the top n locations based on each available metric where n is a parameter given to the API call
        result = []
        for metric in ["air_pressure", "humidity", "max_temp", "min_temp", "predictability", "the_temp", "visibility",
                       "weather_state_abbr", "weather_state_name", "wind_direction", "wind_direction_compass",
                       "wind_speed"]:
            query = """
                        select a.location 
                        from (select location, """ + str(metric) + """   
	                    from forecast 
	                    order by 2 desc
                        limit """ + str(n) + """) as a
                        """
            for location in db.query(query):
                result.append({
                    metric: location[0]
                })
        return result
