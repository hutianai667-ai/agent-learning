log_path = "week-01/outputs/practice-log.txt"

new_entry = input("Write one learing note: ")

with open(log_path, "a", encoding="utf-8") as file:
    file.write(new_entry + "\n")

print (f"Saved one note to {log_path}")