# badge_maker function
def badge_maker(name):
    return f"Hello, my name is {name}."

# batch_badge_creator function
def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

#  assign_rooms function
def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers, start=1):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {index}!")
    return room_assignments

# printer function
def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)

# Test the functions
speakers = ["Arel", "Carol"]
printer(speakers)
