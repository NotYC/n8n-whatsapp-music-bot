# n8n-whatsapp-music-bot 🎵🤖

A WhatsApp automation built with n8n, Twilio, and Spotify API that lets users request songs directly over WhatsApp. The bot fetches the requested song, downloads it, and sends it back to the user.

🚀 How It Works

A user sends a WhatsApp message in the format:

play <song name>


The message is received via Twilio and passed to the n8n workflow.

The bot replies instantly:

Your song is being prepared 🎶 Please wait a moment...


Using the Spotify API, the bot fetches the requested track link.

The song is downloaded on the local server where automation is running.

The file is uploaded to Google Drive (to generate a public link, since Twilio requires it).

Finally, the bot sends the song link back to the user on WhatsApp.

⚙️ Tech Stack

n8n → Orchestration and workflow automation

Twilio → WhatsApp messaging integration

Spotify Web API → Fetching song metadata and links

Local Server → Downloading tracks

Google Drive API → Hosting files with public links

📂 Project Structure
n8n-whatsapp-music-bot/
│── workflows/        # n8n exported workflow JSON
│── scripts/          # helper scripts (download, upload, etc.)
│── docs/             # documentation and diagrams
│── README.md         # project overview

🖼️ Workflow Overview

Trigger: Incoming WhatsApp message via Twilio

Logic: Parse command and song name

Spotify API: Search for requested track

Server: Download track

Google Drive: Upload and generate link

Twilio: Send song link back to user

🌟 Features

Request any song from WhatsApp using a simple play <song> command

Fully automated pipeline (no manual intervention)

Supports multiple users simultaneously

Reusable n8n workflow that can be extended to other APIs

📸 Demo

(Add screenshots or GIFs of WhatsApp chat + workflow here)

🔮 Future Improvements

Direct audio file sending (if WhatsApp/Twilio allows)

Add YouTube integration for wider track availability

User-friendly error handling for unavailable songs

🧑‍💻 Author

Created by Yuvraj Chawla

LinkedIn

GitHub
