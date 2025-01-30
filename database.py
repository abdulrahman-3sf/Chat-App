import uuid

db = {
    "users": {},
    
    "channels": {},
    "messages": {},
    
    "global_chat": {
        "channel_id": "global_chat_id",
        "channel_name": "Global Chat",
        "leader_id": None,
        "leader_name": None,
        "users": [],
        "messages": []
    }
}

# ---------------------- User Authentication ---------------------- #
def register_user(username, password):
    if username in db["users"]:
        return "Username already taken. Please choose another."
    db["users"][username] = password  # Storing without encryption (not recommended)
    return "User registered successfully."

def authenticate_user(username, password):
    if username in db["users"] and db["users"][username] == password:
        return "Login successful."
    return "Invalid username or password."


# ---------------------- Global Chat Room ---------------------- #
def join_global_chat(user_name):
    if user_name not in db["global_chat"]["users"]:
        db["global_chat"]["users"].append(user_name)
        return f"User {user_name} joined the Global Chat successfully."
    return f"User {user_name} is already in the Global Chat."

def leave_global_chat(user_name):
    if user_name in db["global_chat"]["users"]:
        db["global_chat"]["users"].remove(user_name)
        return f"User {user_name} left the Global Chat successfully."
    return f"User {user_name} is not in the Global Chat."

def get_number_of_users_in_global_chat():
    return len(db["global_chat"]["users"])

def send_message_to_global_chat(user_name, message):
    if user_name in db["global_chat"]["users"]:
        message_data = {
            "user_name": user_name,
            "message": message
        }
        db["global_chat"]["messages"].append(message_data)
        return f"Message from {user_name} added to Global Chat."
    return f"User {user_name} is not in the Global Chat."

def get_messages_from_global_chat():
    return db["global_chat"]["messages"]


# ---------------------- Channel Chat Rooms ---------------------- #
def create_channel(leader_id, leader_name, channel_name):
    if any(data["channel_name"] == channel_name for data in db["channels"].values()):
        return f"Channel name '{channel_name}' is already in use. Please choose another name."
    
    channel_id = str(uuid.uuid4())
    channel_data = {
        "channel_id": channel_id,
        "leader_id": leader_id,
        "leader_name": leader_name,
        "channel_name": channel_name,
        "users": [leader_name],
        "messages": []
    }
    db["channels"][channel_id] = channel_data
    return channel_data

def add_user_to_channel(user_name, channel_id):
    if channel_id in db["channels"]:
        if user_name not in db["channels"][channel_id]["users"]:
            db["channels"][channel_id]["users"].append(user_name)
            return f"User {user_name} added to channel {channel_id} successfully."
        else:
            return f"User {user_name} is already in the channel."
    return f"Channel {channel_id} does not exist."

def remove_user_from_channel(user_name, channel_id):
    if channel_id in db["channels"]:
        if user_name in db["channels"][channel_id]["users"]:
            lengthOfUsers = len(db["channels"][channel_id]["users"])
            if lengthOfUsers == 1:
                del db["channels"][channel_id]
                return f"User {user_name} removed from channel {channel_id} successfully. Channel {channel_id} has been deleted."
            else:
                if db["channels"][channel_id]["leader_name"] == user_name:
                    for user in db["channels"][channel_id]["users"]:
                        if user != user_name:
                            db["channels"][channel_id]["leader_name"] = user
                            break
                
                return f"User {user_name} removed from channel {channel_id} successfully."
        else:
            return f"User {user_name} is not in the channel."
    return f"Channel {channel_id} does not exist."

def add_message_to_channel(user_name, channel_id, message):
    if channel_id not in db["channels"]:
        return f"Channel {channel_id} does not exist."

    if user_name not in db["channels"][channel_id]["users"]:
        return f"User {user_name} is not a member of channel {channel_id}."

    message_data = {
        "user_name": user_name,
        "message": message
    }
    db["channels"][channel_id]["messages"].append(message_data)
    return f"Message from {user_name} added to channel {channel_id} successfully."

def delete_channel(leader_id, channel_id):
    if channel_id in db["channels"]:
        if db["channels"][channel_id]["leader_id"] == leader_id:
            del db["channels"][channel_id]
            return f"Channel {channel_id} deleted successfully."
        else:
            return f"Only the leader can delete the channel."
    return f"Channel {channel_id} does not exist."

def update_channel_name(leader_id, channel_id, new_name):
    if channel_id in db["channels"]:
        if db["channels"][channel_id]["leader_id"] == leader_id:
            old_name = db["channels"][channel_id]["channel_name"]
            db["channels"][channel_id]["channel_name"] = new_name
            # Notify users about the name change
            notification = {
                "user_name": "System",
                "message": f"The channel name has been changed from '{old_name}' to '{new_name}'."
            }
            db["channels"][channel_id]["messages"].append(notification)
            return f"Channel {channel_id} name updated to '{new_name}' successfully."
        else:
            return f"Only the leader can update the channel name."
    return f"Channel {channel_id} does not exist."

def remove_user_by_leader(leader_name, channel_id, user_name):
    if channel_id in db["channels"]:
        channel = db["channels"][channel_id]
        if channel["leader_name"] == leader_name:
            if user_name == leader_name:
                return "Error: Leader cannot remove themselves."
            if user_name in channel["users"]:
                channel["users"].remove(user_name)
                return f"User {user_name} removed from channel {channel_id} by leader successfully."
            else:
                return f"User {user_name} is not in the channel."
        else:
            return "Only the leader can remove users from the channel."
    return f"Channel {channel_id} does not exist."

def get_all_channels():
    return [
        {
            "channel_id": channel_id,
            "channel_name": data["channel_name"]
        }
        for channel_id, data in db["channels"].items()
    ]

def get_channels_for_user(user_name):
    return [
        {
            "channel_id": channel_id,
            "channel_name": data["channel_name"]
        }
        for channel_id, data in db["channels"].items()
        if user_name in data["users"]
    ]

def is_user_leader(user_name, channel_id):
    if channel_id in db["channels"]:
        return db["channels"][channel_id]["leader_name"] == user_name
    return False

def get_messages(channel_id):
    if channel_id in db["channels"]:
        return db["channels"][channel_id]["messages"]
    return []

def get_users_in_channel(channel_id):
    if channel_id in db["channels"]:
        return db["channels"][channel_id]["users"]
    return f"Channel {channel_id} does not exist."

def get_channel_id_by_name(channel_name):
    for channel_id, data in db["channels"].items():
        if data["channel_name"] == channel_name:
            return channel_id
    return None

def get_users_in_channel(channel_id):
    if channel_id in db["channels"]:
        return db["channels"][channel_id]["users"]
    return []

def get_channels_by_user(leader_name):
    return {channel_id: channel for channel_id, channel in db["channels"].items() if channel["leader_name"] == leader_name}


def delete_channel(leader_name, channel_id):
    if channel_id not in db["channels"]:
        return "Channel does not exist."
    
    channel = db["channels"][channel_id]
    
    if channel["leader_name"] != leader_name:
        return "Only the channel leader can delete this channel."
    
    del db["channels"]["channel_id"]
    
    if channel_id in db["messages"]:
        del db["messages"][channel_id]

    return f"Channel '{channel['channel_name']}' has been deleted."