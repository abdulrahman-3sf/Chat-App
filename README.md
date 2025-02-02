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
   git clone git@github.com:abdulrahman-3sf/Chat-App.git
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

**Main Menu**: Choose which one you want to use.
- **Global Chat**:
   - Enter the public chat room.
   - Send messages, refresh the chat, or view active users.
   - Exit with option 4 or 5.
- **Multiple Channels**:
  - View/create/join/manage private channels.
  - Send messages, refresh the chat, or view active users.
  - Exit: Quit the application.

**Channel Operations**:

Create Channel: Provide a name to start a new channel (you become the leader).

Join Channel: Enter a channel name to join.

Manage Channels: Leaders can rename channels, remove users, or delete channels.

--- 
## Function Structuering for Further Integration 

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

---

## System Design

<h3>Create Channel</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/d11772bf-5f64-41f5-b479-b2aab0bf0e07" alt="Create Channel">
</p>

<h3>Connect to Channel</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/78b6488e-fb81-4d76-bebb-8bf669d5a5d7" alt="Connect to Channel">
</p>

<h3>Leader ID</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/2049fc6f-78c7-480f-a653-01850959bd94" alt="Leader ID">
</p>

<h3>Join</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/20f5b74d-25f0-4cd3-8e95-338decb11570" alt="Join">
</p>

<h3>Leave</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/6a0fd86b-783b-40e7-8f36-4ac587920729" alt="Leave">
</p>

<h3>Send Message</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/f82b64f1-e1ae-4547-b12c-36fd026603ba" alt="Send Message">
</p>

<h3>Who</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/6a59af3d-a004-4c91-b350-97e2686a017e" alt="Who">
</p>

<h3>Rename</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7637a759-4686-4efd-b66a-09dc70874dd6" alt="Rename">
</p>

<h3>Delete</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/de4c5c5a-8645-48b3-83f5-596e571ee8b4" alt="Delete">
</p>

<h3>Dependency</h3>
<p align="center">
  <img src="https://github.com/user-attachments/assets/bd737045-8a87-4b4f-8df7-49dd38a26094" alt="Dependency">
</p>
