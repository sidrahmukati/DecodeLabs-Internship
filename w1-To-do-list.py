print("My to-do list")
day = input(str("Day: " ))
date = input(str("date: " ))

my_task = []
while True:
    task = input(str("Enter task or quit to stop: "))
    if task.lower() == "quit":
        break
    my_task.append(task)

for i, task in enumerate(my_task, start=1):
    print(f"{i} {task}")
        