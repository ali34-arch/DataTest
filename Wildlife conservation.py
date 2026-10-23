print("=== WILDLIFE SIGHTING RECORDER ===")
while True:
    species = input("Animal species: ").strip()
    location = input("Reserve or location: ").strip()
    try:
        number = int(input("Number seen: "))
        if number > 0:
            print(f"{species} - {location} - {number}")
            break
        else:
            print("Invalid input\n")
            continue
    except ValueError:
        print("Invalid input\n")


print("Thank you for supporting wildlife conservation!")
