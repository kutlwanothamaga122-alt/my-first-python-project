def main():
    tasks = []
    print("--- Simple To-Do List ---")
    
    while True:
        task = input("Enter a task (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        tasks.append(task)
        print(f"Added: {task}")
    
    print("\nYour final list:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    main()