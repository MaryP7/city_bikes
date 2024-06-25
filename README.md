# city_bikes
For the purpose of this project, I have analyzed the use of Citi Bike in 2022 from multiple aspects, including but not limited to:

What are the total trips monthly throughout the year of 2022?
What are the total trips for each hour of the day for every month in 2018? Are there differences in the winter months vs any other months?
What do the total trips look like on the weekday vs weekend? How do weekday vs weekend trips look in Fall, Spring, Summer, and Winter?
What is the proportion of bike usage for each day of the week based on the user type (customer vs subscriber)? How does it look like based on gender?
I am getting my data from Citi Bike’s system data. Data for each trip is made available on the Citi Bike’s website. Each file records monthly data. Each data file is huge, but for this project, I will only be analyzing the data for 2022. Each trip record includes:

Trip duration
Start time
Stop time
Start station ID
Start station name
Start station latitude
Start station longitude
End Station ID
End Station Name
End Station Latitude
End Station Longitude

Packages I am using for this project:

knitr
dplyr
tidyverse
lubridate
maps
tmaptools
ggmap
rmap