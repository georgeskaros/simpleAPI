# API project

The compressed file consists of 4 python files. 
____________________________________________________
# take_data.py

This program fetches the selected data from the metaweather API. The parameters of the data are set for the specific data I chose to collect. You can change them in the for loop (the date) and in the dictionary created with the locations. This code also creates a table in an already created database with the appropriate columns. 


____________________________________________________
# app.py

this is the main file you run to access the API I created. You can navigate to the API with the following paths:
>‘/’ is the default path that welcomes you 
>‘/all_temp’ represents the first question and returns the latest forecast for each location for every day
>'/the_temp' represents the second question and returns the average the_temp of the last 3 forecasts for each location for every day
>'/top/n' represents the third question and returns the top n locations based on each available metric where n is a parameter given to the API call. Where is n you can use any number.

____________________________________________________
# forecast.py

this is where all the processing of the queries is done, I created a class with variables the columns of the table, some function that fetch the data from the database connection created in the other file(db.py) as well as a function to transform a query to json format

____________________________________________________
# db.py

Here are the database connections and query executions