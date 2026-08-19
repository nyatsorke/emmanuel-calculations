num_years=4
days_per_year=365
hours_per_day=24
mins_per_hour=60
secs_per_min=60

#Calculate the number of seconds in 4 years
total_secs=secs_per_min*mins_per_hour*hours_per_day*days_per_year*num_years
print(total_secs)

#Update to leap years
days_per_year=365.25
total_secs=secs_per_min*mins_per_hour*hours_per_day*days_per_year*num_years
print(total_secs)

