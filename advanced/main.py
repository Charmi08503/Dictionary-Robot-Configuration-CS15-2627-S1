robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 100,
    "speed": 6,
    "color": "Blue"
}

choice = ""

while choice != "5":
    print("Robot Configuration Manager")
    print("1. View All Settings")
    print("2. Look Up a Setting")
    print("3. Change a Setting")
    print("4. Add a Setting")
    print("5. Exit")

    try:
        choice = input("Enter your choice: ")

        if choice == "1":
            for key, value in robot.items():
                print(key, ":", value)

        elif choice == "2":
            key = input("Enter the setting you want to look up: ")
            print(key, ":", robot.get(key, "Setting not found"))

        elif choice == "3":
            key = input("Enter the setting you want to change: ")

            if key in robot:
                value = input("Enter the new value: ")
                robot[key] = value
                print("Setting updated.")
            else:
                print("Setting does not exist.")

        elif choice == "4":
            key = input("Enter the new setting name: ")

            if key in robot:
                print("Setting already exists.")
            else:
                value = input("Enter the setting value: ")
                robot[key] = value
                print("Setting added.")

        elif choice == "5":
            print("Exiting Robot Configuration Manager.")

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please try again.")


