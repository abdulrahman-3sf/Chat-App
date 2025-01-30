from xmlrpc.server import SimpleXMLRPCServer
import database

class ChannelServer:
    
    # -------------------- User Authentication -------------------- #
    def register_user(self, username, password):
        return database.register_user(username, password)

    def authenticate_user(self, username, password):
        return database.authenticate_user(username, password)
    
    
    # -------------------- Sngle Chat Room -------------------- #
    def join_global_chat(self, user_name):
        return database.join_global_chat(user_name)

    def leave_global_chat(self, user_name):
        return database.leave_global_chat(user_name)
    
    def get_number_of_users_in_global_chat(self):
        return database.get_number_of_users_in_global_chat()

    def send_message_to_global_chat(self, user_name, message):
        return database.send_message_to_global_chat(user_name, message)

    def get_messages_from_global_chat(self):
        return database.get_messages_from_global_chat()
    
    
    # -------------------- Channel Chat Rooms -------------------- #
    def create_channel(self, leader_id, leader_name, channel_name):
        return database.create_channel(leader_id, leader_name, channel_name)

    def join_channel(self, user_name, channel_id):
        return database.add_user_to_channel(user_name, channel_id)

    # if there is no one in the channel, the channel will be deleted
    def leave_channel(self, user_name, channel_id):
        return database.remove_user_from_channel(user_name, channel_id)

    def send_message(self, user_name, channel_id, message):
        return database.add_message_to_channel(user_name, channel_id, message)

    def get_channels(self):
        return database.get_all_channels()

    def get_user_channels(self, user_name):
        return database.get_channels_for_user(user_name)

    def is_leader(self, user_name, channel_id):
        return database.is_user_leader(user_name, channel_id)

    def get_messages(self, channel_id):
        return database.get_messages(channel_id)
    
    def update_channel_name(self, leader_name, channel_id, new_name):
        leader_id = None
        for ch_id, data in database.db["channels"].items():
            if data["leader_name"] == leader_name:
                leader_id = data["leader_id"]
                break
        return database.update_channel_name(leader_id, channel_id, new_name)
    
    def remove_user_by_leader(self, leader_name, channel_id, user_name):
        return database.remove_user_by_leader(leader_name, channel_id, user_name)
    
    def get_users_in_channel(self, channel_id):
        return database.get_users_in_channel(channel_id)

    def get_channel_id_by_name(self, channel_name):
        return database.get_channel_id_by_name(channel_name)
    
    def get_channels_by_user(self, leader_name):
        return database.get_channels_by_user(leader_name)
    
    # continue the code in database
    def delete_channel(self, leader_name, channel_id):
        return database.delete_channel(leader_name, channel_id)
    
# Start the server
server = SimpleXMLRPCServer(("127.0.0.1", 8080), allow_none=True)
channel_server = ChannelServer()

# Register methods

# Authentication functions
server.register_function(channel_server.register_user, "register_user")
server.register_function(channel_server.authenticate_user, "authenticate_user")

# Global chat methods 
server.register_function(channel_server.join_global_chat, "join_global_chat")
server.register_function(channel_server.leave_global_chat, "leave_global_chat")
server.register_function(channel_server.get_number_of_users_in_global_chat, "get_number_of_users_in_global_chat")
server.register_function(channel_server.send_message_to_global_chat, "send_message_to_global_chat")
server.register_function(channel_server.get_messages_from_global_chat, "get_messages_from_global_chat")

# Channel chat methods
server.register_function(channel_server.create_channel, "create_channel")
server.register_function(channel_server.join_channel, "join_channel")
server.register_function(channel_server.leave_channel, "leave_channel")
server.register_function(channel_server.send_message, "send_message")
server.register_function(channel_server.get_channels, "get_channels")
server.register_function(channel_server.get_user_channels, "get_user_channels")
server.register_function(channel_server.is_leader, "is_leader")
server.register_function(channel_server.get_messages, "get_messages")
server.register_function(channel_server.update_channel_name, "update_channel_name")
server.register_function(channel_server.remove_user_by_leader, "remove_user_by_leader")
server.register_function(channel_server.get_users_in_channel, "get_users_in_channel")
server.register_function(channel_server.get_channel_id_by_name, "get_channel_id_by_name")
server.register_function(channel_server.get_users_in_channel, "get_users_in_channel")
server.register_function(channel_server.get_channels_by_user, "get_channels_by_user")
server.register_function(channel_server.delete_channel, "delete_channel")

print("Server is running on http://127.0.0.1:8080")
server.serve_forever()