print("=== omoikane task Manager ===")
FILE_NAME = "todo.txt"
tasks = {}

try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        tasks = f.readlines()
except FileNotFoundError:
    pass
def add_task():
    task = input("追加するタスク: ")
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(task + "\n")
    print("追加した")

def show_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = f.readlines()
    except FileNotFoundError:
        tasks = []

    if not tasks:
        print("タスクなし")
        return

    print("====タスク一覧====")
    for i, t in enumerate(tasks, 1):
        print(f"{i}: {t.strip()}")

def delete_task():
    show_tasks()
    num = int(input("削除する番号: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("削除した")
    else:
        print("番号おかしい")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = f.readlines()

        tasks.pop(num - 1)

        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for t in tasks:
                f.write(t)

        print("削除した")
    except:
        print("削除できん")
    
    print("=====タスク管理アプリ=====")
    for i, t in enumerate(tasks, 1):
            print(f"{i}: {t.strip()}")

while True:
    print("\n1:追加 2:表示 3:削除 4:終了")
    choice = input("選択: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("終了")
        break
    else:
        print("1〜4で選んで")