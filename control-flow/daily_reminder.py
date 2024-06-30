def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
      case 'high':
       reminder = f"Reminder: '{task}' is a high priority task"
      case 'medium':
       reminder = f"Reminder: '{task}' is a medium priority task"
      case 'low':
       reminder = f"Reminder: '{task}' is a low priority task"
      case _:
       reminder = f"Reminder: '{task}' has an unspecified priority"

    if time_bound == 'yes':
      reminder += " that requires immediate attention today!"
    elif time_bound == 'no':
      reminder += ". Consider completing it when you have free time."
    else:
      reminder += ". Time-bound status unspecified."

    print(reminder)

if __name__ == "__main__":
    main()

