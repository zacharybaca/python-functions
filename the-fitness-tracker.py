"""Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5

Task 3: Create a summary function that provides a report of all activities and total calories burned for the day."""



# Task 1

activities = ['Dancing', 'Swimming', 'Biking']
duration = [10, 20, 15]

def fitness_activities(activities_array, duration_array):
    for activity in range(len(activities_array)):
        print(f"You Have Been {activities_array[activity]} for {duration_array[activity]} minutes")




# Task 2

burned = 0
total_burned = 0

def calories_burned(activity_array, activity_duration):
    for activity in range(len(activity_array)):
        global total_burned
        if activity_array[activity] == 'Dancing':
            global burned
            burned = 25 * activity_duration[activity]
        elif activity_array[activity] == 'Swimming':
            burned = 120 * activity_duration[activity]
        elif activity_array[activity] == 'Biking':
            burned = 200 * activity_duration[activity]
        total_burned += burned
    print(f"You Have Burned {total_burned} Calories")

    return total_burned




# Task 3

def summary_function(activity_array, duration_array):
    fitness_activities(activity_array, duration_array)
    calories_burned(activity_array, duration_array)

summary_function(activities, duration)