sightings = []
next_id = 1

def add_sighting():
    global next_id
    while True:
        species = input("Species: ").strip()
        if species == "":
            print("Invalid\n")
            continue
        location = input("Location: ").strip()
        if location == "":
            print("Invalid\n")
            continue
        count = int(input("Number seen: "))
        if count <=0:
            print("Number must be greater than 0")
            continue
        else:
            break
    dictionary = {"ID": next_id, "species": species, "location": location, "count": count}
    sightings.append(dictionary)
    next_id += 1

def view_sightings():
    if len(sightings) == 0:
        print("No sightings found")
    else:
        for i in enumerate(sightings):
            print(i)
    pass

def search_sightings():
    term = input("Species to search: ").strip().lower()
#    for A,B in enumerate(sightings):
 #       if term == A[""]:
  #          print(A)
    # TODO: Show 'No matches' if none are found.
    pass

def update_sighting():
    finding = int(input("ID: "))
    for A, B in enumerate(sightings):
        if finding == A["ID"]:
            print()
    # TODO: Find that ID and change its count.
    # TODO: Report if the ID does not exist.
    pass

def delete_sighting():
    # TODO: Ask for a sighting ID.
    # TODO: Confirm deletion before removing it.
    pass

while True:
    print("\n1 Add  2 View  3 Search  4 Update  5 Delete  6 Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_sighting()
    elif choice == "2":
        view_sightings()
    elif choice == "3":
        search_sightings()
    elif choice == "4":
        update_sighting()
    elif choice == "5":
        delete_sighting()
    elif choice == "6":
        break
    else:
        print("Invalid menu choice")
