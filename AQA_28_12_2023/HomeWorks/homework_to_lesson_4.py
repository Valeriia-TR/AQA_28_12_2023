# Exercise 1

print("You can use next commands:\n"
      "'add' to add a new note;\n"
      "'earliest' to sort notes by earliest;\n"
      "'latest' to sort notes by latest;\n"
      "'longest' to sort notes by length ascending;\n"
      "'shortest' to sort notes by length descending;\n"
      "'Exit' to exit")

notes = []

while True:
    command = input("Enter command: ").lower()
    if command == "add":
        note = input("Enter your note: ")
        notes.append(note)
        print("Your note has been added")
    elif command == "earliest":
        earliest_note = sorted(notes, key=notes.index, reverse=True)
        print("Notes are sorted by earliest:")
        for note in earliest_note:
            print(f"- {note}\n")
    elif command == "latest":
        latest_note = sorted(notes, key=notes.index)
        print("Notes are sorted by latest:")
        for note in latest_note:
            print(f"- {note}\n")
    elif command == "shortest":
        shortest_note = sorted(notes, key=len)
        print("Notes are sorted by length ascending:")
        for note in shortest_note:
            print(f"- {note}\n")
    elif command == "longest":
        longest_note = sorted(notes, key=len, reverse=True)
        print("Notes are sorted by length descending:")
        for note in longest_note:
            print(f"- {note}\n")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid command, please use 'add', 'earliest', 'latest', 'shortest', 'longest', 'exit'")
