FILEPATH = "day1task1.txt"

def read_todo(filepath=FILEPATH):  # ✅ логичное имя
    with open(filepath, "r") as file:
        return file.readlines()

def write_todo(todos, filepath=FILEPATH):  # ✅ логичное имя
    with open(filepath, "w") as file:
        file.writelines(todos)



if __name__ == "__main__":
    print("working")
    print(write_todo())