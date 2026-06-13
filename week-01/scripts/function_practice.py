def count_characters(text):
    return len(text)

def title_1(text):
    return f"Title: {text}"

def build_summary(name, note):
    character_count = count_characters(note)
    return f"{name}'s note has {character_count} characters. \nNote:{note}"

name = input("What's your name? ")
note = input("Write one learing note: ")
title = input("Write your title: ")

summary = build_summary(name, note)
title2=title_1(title)

print(title2)
print(summary)