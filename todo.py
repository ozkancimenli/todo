"""
To-Do List Application
Author: Ozkan Cimenli
Description:
A simple command-line To-Do list app that lets users add, view, and delete tasks.
"""

# --- Global task storage ---
tasks = []


# --- Functions ---
def show_menu():
    """Displays the main menu options."""
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")


def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task added: {task}")
    else:
        print("⚠️ Task cannot be empty!")


def view_tasks():
    """View all tasks in the list."""
    if not tasks:
        print("⚠️ No tasks to show.")
        return
    print("\n--- Current Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task():
    """Delete a task by its number."""
    if not tasks:
        print("⚠️ No tasks to delete.")
        return
    view_tasks()
    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"🗑️ Task deleted: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    """Main program loop."""
    while True:
        show_menu()
        try:
            choice = input("Choose an option (1-4): ").strip()
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("⚠️ Invalid choice, please try again.")
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")
        finally:
            print("--- End of operation ---")


if __name__ == "__main__":
    main()
