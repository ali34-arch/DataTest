
from pathlib import Path

FILE_NAME = Path(__file__).with_name("properties.txt")  #creates a line to the file


def load_properties():
    properties = []
    if not FILE_NAME.exists(): #opens file   b
        return properties #opens file and stores the data in file in variable called file
    with FILE_NAME.open("r", encoding="utf-8") as file:
        for line in file:  #goes through each line
            fields = line.strip().split("|") #removes lines and segments each piece of data into its own string
            if len(fields) == 6: #grabs the first 6 data pieces and stores it in the list
                properties.append({
                    "id": fields[0], "address": fields[1],
                    "city": fields[2], "type": fields[3],
                    "rent": fields[4], "status": fields[5]
                })
    return properties


def save_properties(properties):
    with FILE_NAME.open("w", encoding="utf-8") as file:
        for prop in properties: #will update current contents + anything new
            result = "|".join([prop["id"], prop["address"], prop["city"], prop["type"], prop["rent"], prop["status"]]) + "\n"
            file.write(result) #line above organizes everything
    pass


def add_property(properties):
    print("\n--- ADD PROPERTY ---")
    property_id = input("Property ID: ")
    address = input("Address: ")
    city = input("City: ")
    property_type = input("Property type: ")
    rent = input("Monthly rent (£): ")
    status = input("Status: ")
    for i in properties: #runs through each id in properties to find a match
        if i["id"] == property_id:
            print("\n--- PROPERTY ALREADY EXISTS ---")
            return
    property = {
        "id": property_id,
        "address": address,
        "city": city,
        "type": property_type,
        "rent": rent,
        "status": status
    }
    properties.append(property) #adds dictionary to list
    save_properties(properties) #list is then added to text file


def view_properties(properties):
    print("\n--- PROPERTY LIST ---")
    if len(properties) == 0:
        print("No properties found.")
        return
    for i in properties: #runs through each property and prints it, keeps going until list is done
        print(i)
    pass


def update_property(properties):
    property_id = input("Property ID to update: ")
    for i in properties: #runs through each property until an id match is found
        if i["id"] == property_id:
            new_rent = input("New rent: ")
            new_status = input("New status: ")
            i["rent"] = new_rent #updates that specific numbered rent with the new input
            i["status"] = new_status
            save_properties(properties)
            break
    else:
        print("Invalid property ID.")
    pass


def delete_property(properties):
    property_id = input("Property ID to delete: ")
    for i in properties: #once again loops through each property
        if i["id"] == property_id:
            choice = input ("Are you sure you want to delete this property? (y/n) ").lower()
            if choice == "y":
                properties.remove(i) #removes the numbered dictionary chosen
                save_properties(properties) #saves updates
                break
            elif choice == "n":
                print("Deletion cancelled")
                break
    else: print("Invalid property ID.")
    pass


def main():
    properties = load_properties()
    while True:
        print("\n=== PROPERTY MANAGEMENT ===")
        print("1. Add property")
        print("2. View properties")
        print("3. Update property")
        print("4. Delete property")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_property(properties)
        elif choice == "2":
            view_properties(properties)
        elif choice == "3":
            update_property(properties)
        elif choice == "4":
            delete_property(properties)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()