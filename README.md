# Chat Application

A Python-based chat application with global and private channel support, built using XML-RPC for client-server communication.

## Features

- **User Authentication**: Register and login with username/password.
- **Global Chat Room**: Join a public chat visible to all users.
- **Private Channels**: Create, join, and manage private channels.
- **Channel Management**:
  - Leaders can rename channels, remove users, or delete channels.
  - Automatic leader reassignment if the leader leaves.
  - Channels auto-delete when empty.
- **Real-Time Messaging**: Send and receive messages instantly in channels or the global chat.

## Installation

1. **Prerequisites**:  
   Ensure Python 3.x is installed.

2. **Clone the Repository** (if applicable):  
   ```bash
   git clone https://github.com/your-repo/chat-app.git
   cd chat-app

3. **Run the server**
   ```bash
   python server.py

The server starts at http://127.0.0.1:8080.

4. **Run the Client**:
   ```bash
   python client.py

---

## Usage

**Client Workflow**
**Login/Register**:
Choose to sign up or log in with your credentials.

1.Main Menu:

2.Global Chat: Enter the public chat room.

3.Show Channels: View/create/join private channels.

4.Exit: Quit the application.

5.Global Chat:

6.Send messages, refresh the chat, or view active users.

7.Exit with option 4 or 5.

**Channel Operations**:

Create Channel: Provide a name to start a new channel (you become the leader).

Join Channel: Enter a channel id to join.

Manage Channels: Leaders can rename channels, remove users, or delete channels.

--- 
## function structuering for further integration 

**Authentication**:
`register_user(username, password)`

`authenticate_user(username, password)`

**Global Chat**:
`join_global_chat(user_name)`

`send_message_to_global_chat(user_name, message)`

`get_messages_from_global_chat()`

**Channels**:
`create_channel(leader_id, leader_name, channel_name)`

`join_channel(user_name, channel_id)`

`send_message(user_name, channel_id, message)`

`update_channel_name(leader_name, channel_id, new_name)`





