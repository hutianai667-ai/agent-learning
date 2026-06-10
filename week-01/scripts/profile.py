def build_profile(name, goal):
    return f"{name} is learning {goal}."


name = input("What is your name? ")
goal = input("What are you learning? ")

message = build_profile(name, goal)
print(message)