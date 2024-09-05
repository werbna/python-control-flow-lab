# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = input("Enter the day of the month: ")
    months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
    # seasons = ("winter", "spring", "summer", "fall")

    if month not in months:
      print("Invalid month. Please enter a valid month.")
    elif not day.isdigit() or int(day) < 1 or int(day) > 31:
      print("Invalid day. Please enter a valid day.")
    else:
      if month == "dec" or (month == "mar" and int(day) < 20) or (month == "jun" and int(day) < 21) or (month == "sep" and int(day) < 22):
        season = "winter"
      elif (month == "mar" and int(day) >= 20) or (month == "jun" and int(day) >= 21) or (month == "sep" and int(day) >= 22) or (month == "dec" and int(day) >= 21):
        season = "spring"
      elif (month == "jun" and int(day) < 21) or (month == "sep" and int(day) < 22) or (month == "dec" and int(day) < 21) or (month == "mar" and int(day) >= 20):
        season = "summer"
      else:
        season = "fall"
      print(f"{month.capitalize()} {day} is in {season}.")

# Call the function
determine_season()
