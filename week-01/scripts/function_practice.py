def count_characters(text):
    return len(text)

def build_summary(name, note):
    character_count = count_characters(note)
    return f"{name}'s note has {character_count} characters. \nNote:{note}"

name = input("What's your name? ")
note = input("Write one learing note: ")

summary = build_summary(name, note)

print(summary)