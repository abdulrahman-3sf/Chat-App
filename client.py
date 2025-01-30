import xmlrpc.client
import uuid
import time

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8080/")

def display_main_menu():
    print("\nMain Menu:")
    print("1. Global Chat")
    print("2. Show Channels")
    print("3. Exit")

def display_channel_options():
    print("\nChannel Options:")
    print("1. Create Channel")
    print("2. Join Channel")
    print("3. Leave Channel")
    print("4. Delete Channel")
    print("5. Back to Main Menu")


def display_conversation_menu(is_leader):
    print("\nConversation Menu:")
    print("1. Send Message")
    print("2. Refresh Chat")
    print("3. Show Number of Users in Channel")
    print("4. Leave Channel")
    print("5. Exit Conversation")
    if is_leader:
        print("6. Update Channel Name")
        print("7. Remove User")


def login_or_register():
    while True:
        print("\nWelcome! Please choose an option:")
        print("1. Login")
        print("2. Sign Up")
        choice = input("Enter choice: ")

        username = input("Enter username: ")
        password = input("Enter password: ")

        if choice == "1":
            response = proxy.authenticate_user(username, password)
            print(response)
            if response == "Login successful.":
                return username  # Proceed if login is successful
        elif choice == "2":
            response = proxy.register_user(username, password)
            print(response)
            if response == "User registered successfully.":
                return username  # Proceed if registration is successful
        else:
            print("Invalid option. Please try again.")
            
def show_channels(user_name):
    print("\nAvailable Channels:")
    channels = proxy.get_channels()
    if not channels:
        print("No available channels.")
    else:
        for channel in channels:
            print(f"- {channel['channel_name']} (ID: {channel['channel_id']})")

    print("\nChannels You Joined:")
    joined_channels = proxy.get_user_channels(user_name)
    if not joined_channels:
        print("You have not joined any channels.")
    else:
        for channel in joined_channels:
            print(f"- {channel['channel_name']} (ID: {channel['channel_id']})")

def fetch_messages(channel_id):
    messages = proxy.get_messages(channel_id)
    for message in messages:
        print(f"[{message['user_name']}] {message['message']}")

def enter_global_chat(user_name):
    print("\nEntering Global Chat...")

    response = proxy.join_global_chat(user_name)
    print(response)

    while True:
        print("\nGlobal Chat Menu:")
        print("1. Send Message")
        print("2. Refresh Chat")
        print("3. Show Number of Users in Chat")
        print("4. Leave Chat")
        print("5. Exit Chat")

        choice = input("Select an option: ")

        if choice == "1":
            message = input("Enter your message: ")
            response = proxy.send_message_to_global_chat(user_name, message)
            print(response)

        elif choice == "2":
            messages = proxy.get_messages_from_global_chat()
            if messages:
                print("")
                for msg in messages:
                    print(f"[{msg['user_name']}] {msg['message']}")
            else:
                print("No messages in the Global Chat.")

        elif choice == "3":
            num_users = proxy.get_number_of_users_in_global_chat()
            print(f"There are {num_users} users in the Global Chat.")
    
        
        elif choice == "4":
            response = proxy.leave_global_chat(user_name)
            print(response)
            break

        elif choice == "5":
            print("Exiting Global Chat...")
            break

        else:
            print("Invalid option. Please try again.")

def enter_channel(user_name, channel_id, is_leader):
    print("\nEntering the channel...")
    fetch_messages(channel_id)

    while True:
        display_conversation_menu(is_leader)
        conversation_choice = input("Select an option: ")

        if conversation_choice == "1":
            message = input("Enter your Message: ")
            response = proxy.send_message(user_name, channel_id, message)
            print(response)

        elif conversation_choice == "2":
            print("\nRefreshing chat...")
            fetch_messages(channel_id)

        elif conversation_choice == "3":
            users = proxy.get_users_in_channel(channel_id)
            if isinstance(users, list):
                print(f"There are {len(users)} users in the channel.")
            else:
                print("Failed to retrieve users or channel does not exist.")
    
        elif conversation_choice == "4":
            response = proxy.leave_channel(user_name, channel_id)
            print(response)
            break

        elif conversation_choice == "5":
            print("Exiting conversation...")
            break

        elif conversation_choice == "6" and is_leader:
            new_name = input("Enter New Channel Name: ")
            response = proxy.update_channel_name(user_name, channel_id, new_name)
            print(response)

        elif conversation_choice == "7" and is_leader:
            users_in_channel = proxy.get_users_in_channel(channel_id)
           
            users_in_channel = [user for user in users_in_channel if user != user_name]
            
            if not users_in_channel:
                print("No other users to remove.")
            else:
                print("Users in Channel:")
                for idx, user in enumerate(users_in_channel, start=1):
                    print(f"{idx}. {user}")

                try:
                    choice = int(input("Select a user to remove (enter number): "))
                    if 1 <= choice <= len(users_in_channel):
                        user_to_remove = users_in_channel[choice - 1]
                        response = proxy.remove_user_by_leader(user_name, channel_id, user_to_remove)
                        print(response)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")


def main():
    user_name = login_or_register()
    leader_id = str(uuid.uuid4())

    while True:
        display_main_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            enter_global_chat(user_name)
        
        elif choice == "2":
            show_channels(user_name)

            while True:
                display_channel_options()
                option = input("Select an option: ")

                if option == "1":
                    channel_name = input("Enter Channel Name: ")
                    response = proxy.create_channel(leader_id, user_name, channel_name)
                    print(response)

                    if "channel_id" in response:
                        channel_id = response["channel_id"]
                        enter_channel(user_name, channel_id, is_leader=True)

                elif option == "2":
                    channel_name = input("Enter Channel Name: ")
                    channel_id = proxy.get_channel_id_by_name(channel_name)
                    
                    if channel_id is None:
                        print(f"Channel '{channel_name}' does not exist.")
                
                    else:
                        response = proxy.join_channel(user_name, channel_id)
                        print(response)

                        if "successfully" in response or "already in" in response:
                            is_leader = proxy.is_leader(user_name, channel_id)
                            enter_channel(user_name, channel_id, is_leader)


                elif option == "3":
                    channel_name = input("Enter Channel Name: ")
                    channel_id = proxy.get_channel_id_by_name(channel_name)
                    
                    if channel_id:
                        response = proxy.leave_channel(user_name, channel_id)
                        print(response)
                    else:
                        print(f"Channel '{channel_name}' does not exist.")


                elif option == "4":
                    # Get the channels created by the current user
                    channels = proxy.get_channels_by_user(user_name)
                    
                    if channels:
                        print("\nYour Created Channels:")
                        for channel_id, channel in channels.items():
                            print(f"{channel['channel_name']}")  # Display channel name

                        # Ask the user to choose a channel name to delete
                        channel_name = input("\nEnter Channel Name to Delete: ")

                        # Find the channel by name and get its ID
                        channel_to_delete = None
                        for channel_id, channel in channels.items():
                            if channel['channel_name'].lower() == channel_name.lower():
                                channel_to_delete = channel_id  # Store the channel_id for deletion
                                break
                        
                        if channel_to_delete:
                            # Proceed with deletion using channel_id
                            response = proxy.delete_channel(user_name, channel_to_delete)
                            print(response)  # Output result of deletion
                        else:
                            print(f"No channel found with the name '{channel_name}'.")
                    else:
                        print("You haven't created any channels yet.")




                elif option == "5":
                    print("Returning to Main Menu...")
                    break


                else:
                    print("Invalid option. Please try again.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
