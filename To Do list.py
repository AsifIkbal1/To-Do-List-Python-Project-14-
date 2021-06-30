from prettytable import PrettyTable
print("\n My To-Do list.")

instructions="\n1:Enter A or a to add new To-Do.\n2: Enter D or d to delete To-Do.\n3: Enter U or u to update To-Do.\n4:Enter E or e to exit the program.\n5: Enter L or l to check your To-Do List. "
print(instructions)

my_todo_list=[]

x=PrettyTable()
def my_list():
    x.field_names=['Item Names']
    for i in my_todo_list:
        x.add_row([i])
        print(x.get_string(title="To-Do List"))
        x.clear_rows()

running= True
while running:
    user_input=input("\nWhat do you want to do? (A,D,U,E,L):").lower()
    if user_input=="a":
        new_todo=input("\n Please enter your new To-Do: ").lower()
        print(f"\n Your current To-Do is {new_todo}.")
        my_todo_list.append(new_todo)
    elif user_input=='d':
        while True:
            item_name=input("\n Please enter a name of an item you want to delete.").lower()
            try:
                if item_name in my_todo_list:
                    choice=input(f"Are you sure to delete{item_name}from your To-Do list ? (Y/N): ").lower()
                    if choice=='y':
                        my_todo_list.remove(item_name)
                        print('Your update To-Do List.')
                        my_list()
                        break
                else:
                    print("Item not found.")

            except Exception:
                print("Somethings went wrong.")



    elif user_input=='u':
        while True:
            item_name = input("\n Please enter a name of an item you want to update.").lower()
            try:
                if item_name in my_todo_list:
                    choice=input(f"\n Are you sure to update {item_name}from your To-Do List? (Y/N): ").lower()
                    if choice=='y':
                        update_item=input(f"Please enter a name you want to update {item_name} with. ").lower()
                        index=my_todo_list.index(item_name)
                        my_todo_list[index]=update_item
                        print("Your updated To-Do List.")
                        my_list()
                        break
                    else:
                        print("Item not found.")
            except Exception:
                print("Somethings went wrong.")


    elif user_input=='e':
        ask_user=input("\n Are you sure to exit ? (Y/N): ").lower()
        if ask_user=='y':
            running=False
    elif user_input=='l':
        my_list()
    elif user_input=='' or user_input=='':
        print("Please enter somethings.")

    else:
        print("Enter a valid value.")
