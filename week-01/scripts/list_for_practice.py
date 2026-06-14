learning_items = []

first_item = input("First item: ")
second_item = input("Second item: ")
third_item = input("Third item: ")

learning_items.append(first_item)
learning_items.append(second_item)
learning_items.append(third_item)

print("Today I practiced: ")

for item in learning_items:
    print(f" - {item}")

print (f"Total: {len(learning_items)} items")