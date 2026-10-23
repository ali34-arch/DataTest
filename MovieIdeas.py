from pathlib import Path
global ID
ID = 0

FILE_NAME = Path(__file__).with_name("Ideas.txt")  #creates a line to the file
def id_load(List): #hopefully update id to ensure each item has a unique id
    for i in List:
        global ID #would that work??
        ID += 1
    else:
        pass

def load_properties():
    List = []
    if not FILE_NAME.exists(): #opens file   b
        return List #opens file and stores the data in file in variable called file
    with FILE_NAME.open("r", encoding="utf-8") as file:
        for line in file:  #goes through each line
            fields = line.strip().split("|") #removes lines and segments each piece of data into its own string
            if len(fields) == 5: #grabs the first 6 data pieces and stores it in the list
                List.append({
                    "ID": fields[0], "Name": fields[1],
                    "Concept": fields[2], "Characters": fields[3],
                    "Plot": fields[4]
                })
    return List

def save_properties(List):
    with FILE_NAME.open("w", encoding="utf-8") as file:
        for prop in List:
            result = "|".join([prop["ID"], prop["Name"], prop["Concept"], prop["Characters"], prop["Plot"]]) + "\n"
            file.write(result)
    pass

def add_property(List, ID):
    print("\n--- Idea ---")
    Name = input("Name: ")
    Concept = input("Concept: ")
    Characters = input("Characters: ")
    Plot = input("Plot: ")
    for i in List: #runs through each id in properties to find a match
        if i["Name"] == Name:
            print("\n--- PROPERTY ALREADY EXISTS ---")
            return
    Dict= {
        "ID": ID,
        "Name": Name,
        "Concept": Concept,
        "Characters": Characters,
        "Plot": Plot,
    }
    List.append(Dict) #adds dictionary to list
    save_properties(List) #list is then added to text file



def main():
    properties = load_properties()
    while True:
        print("\n=== Idea MANAGEMENT ===")
        print("1. Add Idea")
        print("2. View Idea")
        print("3. Update Idea")
        print("4. Delete Idea")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_property(List, ID)
 #       elif choice == "2":
 #           view_properties(properties)
  #      elif choice == "3":
 #           update_property(properties)
 #       elif choice == "4":
  #          delete_property(properties)
    #    elif choice == "5":
  #          break
    #    else:
   #         print("Invalid choice.")


if __name__ == "__main__":
    main()