import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celibrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to the database: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    print("")

    option = input("Enter an option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
        return doc
    except:
        print("error getting the record")
    if not doc:
        print("Error! No results found")


def add_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter dob: ")
    gender = input("Enter gender: ")
    hair_color = input("Enter hair color: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }
    try:
        coll.insert_one(new_doc)
        print("succesfully added")
    except:
        print("an error occured")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [ " + v + " ] >> ")
                if update_doc[k] == "":
                    update_doc[k] = v
        try:
            coll.update_one(doc, {"$set": update_doc})
        except:
            print("üpdating failed.")


def delete_record():
    doc = find_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + " : " + v.capitalize())
        print("")
        confirmation = input("Is the right document to delete? Y/N")
        if confirmation.tolower() == "y":
            try:
                coll.remove(doc)
                print("document succesful deleted")
            except:
                print("deleting failed.")
        else:
            print("document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
