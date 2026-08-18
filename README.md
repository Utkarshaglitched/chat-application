# Real-Time Chat Application

A lightweight, real-time messaging web application. This mini project was built to learn and practice WebSockets and modern backend development.

## Tech Stack
- **Backend:** Python, FastAPI, WebSockets
- **Frontend:** Jinja2 templates, HTML, CSS, JavaScript

## Features
- **Real-time WebSocket communication:** Instant bidirectional messaging between clients and server.
- **Username-based connections:** Simple identity assignment based on user-provided names.
- **Online user discovery:** Dynamic fetching of currently connected active users.
- **One-to-one message routing:** Direct message delivery targeted to specific recipients.
- **Text messaging:** Send and receive text messages instantly.
- **PNG/JPG/JPEG image sharing using Base64:** Upload and share image attachments in chat.
- **Separate conversations per user:** Client-side storage and rendering of distinct chat histories per user connection.
- **Connection/disconnection handling:** Graceful cleanup of user state upon WebSocket disconnection.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Open in browser:**
   - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.
   - Enter your desired username and click **Continue**.
   - Open a second browser tab or incognito window, navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000), and enter a different username.
   - Select the other user from the dropdown to start chatting in real time!

## Project Purpose
This project was created to gain practical experience with asynchronous programming (`async`/`await`), WebSocket protocols, real-time connection management, and Object-Oriented Programming (OOP) concepts in Python.
