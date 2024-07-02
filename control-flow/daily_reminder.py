def get_task_info():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound
def provide_reminder(task, priority, time_bound):
    reminder = f"Reminder: '{task}' is a {priority} priority task."
    match priority:
        case "high":
            if time_bound == "yes":
                reminder += " It requires immediate attention today!"
            else:
                reminder += " Consider completing it as soon as possible."
        case "medium":
            if time_bound == "yes":
                reminder += " It should be completed today."
            else:
                reminder += " Try to complete it within the next few days."
        case "low":
            if time_bound == "yes":
                reminder += " Try to complete it today if possible."
            else:
                reminder += " Consider completing it when you have free time."
        case _:
            reminder += " Note: Invalid priority level provided."
    print(reminder)
if __name__ == "__main__":
    task, priority, time_bound = get_task_info()
    provide_reminder(task, priority, time_bound)
