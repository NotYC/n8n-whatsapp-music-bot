# n8n-whatsapp-music-bot 🎵🤖  

A WhatsApp automation built with **n8n**, **Twilio**, and **Spotify API** that lets users request songs directly over WhatsApp. The bot fetches the requested song, downloads it, and sends it back to the user.  

---

## 🚀 How It Works  

1. A user sends a WhatsApp message in the format:  
   ```text
   play <song name>
   
2. The message is received via Twilio and passed to the n8n workflow.
   
3. The bot replies instantly:
  ```text
   Your song is being prepared 🎶 Please wait a moment...
  ```
4. Using the Spotify API, the bot fetches the requested track link.
5. The song is downloaded on the local server where automation is running.
6. The file is uploaded to Google Drive (to generate a public link, since Twilio requires it).
7. Finally, the bot sends the song link back to the user on WhatsApp.

---

## ⚙️ Tech Stack

• n8n → Orchestration and workflow automation

• Twilio → WhatsApp messaging integration

• Spotify Web API → Fetching song metadata and links

• Local Server → Downloading tracks

• Google Drive API → Hosting files with public links

---

## 📂 Project Structure

n8n-whatsapp-music-bot/
│── workflows/        # n8n exported workflow JSON
│── scripts/          # helper scripts (download, upload, etc.)
│── docs/             # documentation and diagrams
│── README.md         # project overview

---

## 🖼️ Workflow Overview

1. Trigger: Incoming WhatsApp message via Twilio

2. Logic: Parse command and song name

3. Spotify API: Search for requested track

4. Server: Download track

5. Google Drive: Upload and generate link

6. Twilio: Send song link back to user

---

## 🌟 Features

• Request any song from WhatsApp using a simple play <song> command

• Fully automated pipeline (no manual intervention)

• Supports multiple users simultaneously

• Reusable n8n workflow that can be extended to other APIs

---

## 📸 Demo

<img width="857" height="145" alt="image" src="https://github.com/user-attachments/assets/9e0cfce3-69d5-4339-97c8-159901f22891" />


<img width="1552" height="664" alt="image" src="https://github.com/user-attachments/assets/e3ac2923-0c09-4075-8c78-dd6ccf0764e7" />

---
## 😉Bonus Pointers

1. Use ngrok, given in repo, for port forwarding as Twilio require a public link
2. Use Google Drive API to store music file and share that public link to twilio, bonus, make a public folder first and store songs in that folder so you dont have to change share attribute of every file.

---
## 🧑‍💻 Author

~YuvrajChawla

[LinkedIn](https://www.linkedin.com/in/ycnomore/)

[Email](yuvrajchawla.work@gmail.com)



