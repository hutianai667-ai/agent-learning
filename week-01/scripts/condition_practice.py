def check_note_length(note):
    character_count = len(note)

    if character_count ==0:
        return "Your note is empty"
    
    elif character_count < 20:

        return f"Your note is short: {character_count} characters. "
    
    else:
        return f"Your note looks good: {character_count} characters. "

note = input("Write one learning note: ")

result = check_note_length(note)

print(result)