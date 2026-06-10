def build_profile(name, goal, city):
    return f"{name} from {city} is learning {goal}."


name = input("What is your name? ")
city = input("Where are you from? ")
goal = input("What are you learning? ")

message = build_profile(name, goal, city)
print(message)