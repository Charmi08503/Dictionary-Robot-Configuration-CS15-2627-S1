robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print("Robot Name:", robot["name"])
print("Robot Model:", robot["model"])

robot["battery"] = 100

robot["color"] = "Blue"

robot.pop("mode")

print("Number of settings:", len(robot))

for key, value in robot.items():
    print(key, ":", value)
    