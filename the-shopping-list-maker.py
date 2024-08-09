# Task 1: Add Items to list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

# Task 2: Remove items from the list
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} was not found in your shopping list.")

# Task 3: Print the entire list in a formatted way
def print_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list contains:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def shopping_list_maker():
    shopping_list = []
    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Print List")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            item = input("Enter the item you want to add: ")
            add_item(shopping_list, item)
            print_list(shopping_list)  # Print the list after adding an item

        elif choice == '2':
            item = input("Enter the item you want to remove: ")
            remove_item(shopping_list, item)
            print_list(shopping_list)  # Print the list after removing an item

        elif choice == '3':
            print_list(shopping_list)  # Print the list when option 3 is selected

        elif choice == '4':
            print("Quitting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
shopping_list_maker()