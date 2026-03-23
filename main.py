#------Mood & Habit Tracker------

mood_list = []
habit_list = []

#Save data to file
def save_to_file(data):
    file = open("records.txt","a")
    file.write(str(data) + "\n")
    file.close()

#Function to find best and worst day
def find_best_worst(data_list):
    best_day = max(data_list, key=lambda x: (x["Sleep"] + x["Study"] + x["Exercise"]))
    worst_day = min(data_list, key=lambda x: (x["Sleep"]  + x["Study"] + x["Exercise"]))

    return best_day["Day"], worst_day["Day"]

print("\n-----Welcome to Mood & Habit Tracker-----\n")


while True:
    print("\n1. Add Daily Record")
    print("2. View All Records")
    print("3. Show Weekly Report")
    print("4. Exit")

    choice = input("n\Enter your choice: ")

    #1. Add Daily Record
    if choice =="1":

        day = input("\nEnter Day (Example: Day 1, Day2): ")

        print("\nEnter your mood:")
        print("Happy / Sad / Angry / Normal / Stressed / Excited")
        mood = input("Mood:")

        sleep = float(input("Enter sleep hours: "))
        study = float(input("Enter study hours: "))
        exercise = float(input("Enter exercise time (in hours): "))
        water = int(input("Enter water intake (glasses): "))

        mood_list.append(mood)

        day_data = {
            "Day": day,
            "Mood": mood,
            "Sleep": sleep,
            "Study": study,
            "Exercise": exercise,
            "Water": water,
        }

        habit_list.append(day_data)
        save_to_file(day_data)

        print("\n Data added and saved successfully!")

   #2. View All Records
    elif choice == "2":

       if len (habit_list) ==0:
           print("\nNo data available.")
       else:
           print("\n----- ALL RECORDS -----")
           for data in habit_list:
               print(data)

    #3. Show Weekly Report
    elif choice == "3":

        if len(habit_list) ==0:
            print("\nNo data available for report.")
        else:
            total_sleep = 0
            total_study = 0
            total_exercise = 0
            total_water = 0

        for data in habit_list:
            total_sleep += data["Sleep"]
            total_study += data["Study"]
            total_exercise += data["Exercise"]
            total_water += data["Water"]

        avg_sleep = total_sleep / len(habit_list)
        avg_study = total_study / len(habit_list)
        avg_exercise = total_exercise / len(habit_list)
        avg_water = total_water / len (habit_list)  

        #Most common mood
        most_common_mood = max(set(mood_list), key=mood_list.count)


        #Best & Worst Day
        best, worst = find_best_worst(habit_list)


        print("\n------WEEKLY REPORT------")
        print("Most Common Mood:", most_common_mood)
        print("Average Sleep:", round(avg_sleep, 2), "hours")
        print("Average Study:", round(avg_study, 2), "hours")
        print("Average Exercise:", round(avg_exercise, 2), "hours")
        print("Average Water Intake:", round(avg_water, 2), "glasses")
        print("Best Day:", best)
        print("Worst Day:", worst)


        print("\nSuggestion:")
        if avg_sleep < 6:
            print("- Try to improve your sleep.")
        if avg_exercise < 1:
            print("- Do at least 30 minutes of exercise daily.")
        if avg_water < 6:
            print("- Drink more water!")


   #4. Exit
    elif choice =="4":
       print("\nThank you for using Mood & Habit Tracker")
       break
    else:
       print("\n Invalid choice! Try again:")
        
