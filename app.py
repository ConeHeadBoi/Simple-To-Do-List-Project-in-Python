import sys

def display_menu():
	print("\nSimple To-Do List")
	print("1. Add a task")
	print("2. Remove a task")
	print("3. Mark task as done/undone")
	print("4. Display all tasks")
	print("5. Exit")

def display_tasks(tasks):
	if not tasks:
		print("No tasks in the list.")
		return
	print("\nTo-Do List:")
	for idx, task in enumerate(tasks, 1):
		status = "[✓]" if task['done'] else "[ ]"
		print(f"{idx}. {status} {task['desc']}")

