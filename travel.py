# -----------------------------------------------------------------------------------------------------------
# Shreya B Deshpande
# This project is done through Codecademy
# In this project, a TripPlanner V1.0 is created which takes user's name, estimate the time for the travel, 
# provides with origin, destination, and mode of transportation.
# -----------------------------------------------------------------------------------------------------------

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Shreya")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(12.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be travelling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Pune", "Seattle", estimate)