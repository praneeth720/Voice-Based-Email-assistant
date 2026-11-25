# 🎙️ Voice-Based Email Assistant

## 📌 Project Overview

The **Voice-Based Email Assistant** is a Python-based application designed to manage Gmail through voice commands. It enables users to read, compose, send, and manage emails without depending entirely on a keyboard or visual interface.

The system integrates Speech Recognition (STT), Text-to-Speech (TTS), and email communication protocols (IMAP and SMTP) to provide a hands-free email management experience.

This project is especially useful for visually impaired individuals, elderly users, and busy professionals who prefer voice-based interaction.

## 🎯 Objectives

- Enable hands-free email management using voice commands.
- Improve accessibility for visually impaired users.
- Convert speech into text using Speech Recognition.
- Provide spoken responses using Text-to-Speech.
- Read and retrieve incoming emails through IMAP.
- Compose and send emails through SMTP.
- Classify emails based on important keywords.
- Improve productivity and simplify inbox management.

## ✨ Key Features

### 1. Voice-Based Interaction
- Accepts spoken commands through a microphone.
- Converts voice input into text.
- Provides audio feedback and instructions.

### 2. Email Reading
- Connects to Gmail using IMAP.
- Retrieves unread emails.
- Reads sender information and email subjects aloud.
- Allows users to listen to email content.

### 3. Email Sending
- Composes emails using voice commands.
- Accepts recipient email addresses through speech.
- Captures the subject and message body.
- Sends emails using SMTP.

### 4. Automatic Email Classification
- Identifies important emails using keyword-based filtering.
- Uses keywords such as urgent, important, meeting, alert, project, and payment.
- Helps users identify priority messages.

### 5. Email Management
- Supports voice-guided inbox management.
- Provides confirmation before deletion operations.
- Helps reduce unnecessary inbox clutter.

### 6. Error Handling
- Handles unclear voice input.
- Provides feedback for authentication failures.
- Supports text input as a fallback when voice recognition fails.
- Handles network and email communication errors.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| SpeechRecognition | Speech-to-Text |
| pyttsx3 | Text-to-Speech |
| PyAudio | Microphone input |
| IMAP | Retrieving incoming emails |
| SMTP | Sending outgoing emails |
| Regular Expressions (re) | Cleaning spoken email addresses |
| MIMEText | Creating email messages |

## ⚙️ System Architecture

The application follows a voice-driven workflow:

1. The user starts the Voice-Based Email Assistant.
2. The user enters their Gmail address and App Password.
3. The system verifies the email account.
4. The assistant waits for voice commands.
5. Speech Recognition converts the spoken command into text.
6. The system identifies the requested operation.
7. IMAP retrieves emails or SMTP sends emails.
8. pyttsx3 provides spoken responses to the user.
9. The assistant continues until the user says exit.

## 💻 Installation and Setup

### Prerequisites

- Python 3.x
- Git
- Gmail account
- Microphone
- Internet connection
- Gmail App Password

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Voice-Based-Email-Assistant.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Navigate to the Project Folder

```bash
cd Voice-Based-Email-Assistant
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For Linux:

```bash
source venv/bin/activate
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python voice_assistant.py
```

## 🎤 Supported Voice Commands

| Voice Command | Action |
|---|---|
| Check | Check the inbox |
| Send | Compose and send an email |
| Exit | Close the assistant |
| Yes | Confirm a requested operation |
| No | Reject a requested operation |

Additional prompts guide users through recipient, subject, message and email-management operations.

## 🔐 Security and Privacy

- Use a Gmail App Password instead of your primary Gmail password.
- Enable IMAP access in Gmail settings if required.
- Never upload passwords or confidential credentials to GitHub.
- Do not hardcode personal email credentials in the source code.
- Avoid sharing private email information in screenshots or logs.

### Gmail App Password Setup

1. Open your Google Account settings.
2. Enable 2-Step Verification.
3. Find the App Passwords section.
4. Generate an App Password for the application.
5. Use that password when the program requests email authentication.

App Password availability depends on your Google Account configuration.

## 📂 Project Structure

```text
Voice-Based-Email-Assistant/
│
├── voice_assistant.py
│   └── Main Python application
│
├── README.md
│   └── Project documentation
│
├── requirements.txt
│   └── Required Python packages
│
└── .gitignore
    └── Files excluded from Git tracking
```

## 🚀 Future Enhancements

- Voice-based email reply and forwarding.
- Scheduled email sending.
- Multilingual voice recognition.
- AI-powered email summarization.
- Voice authentication.
- GUI or web-based interface.
- Background email notifications.
- Email attachment support.
- Improved offline functionality.

## 🎓 Project Purpose

This project demonstrates the practical application of Python, Speech Recognition, Text-to-Speech and email automation to develop an accessible communication solution.

It aims to make email management easier, faster and more inclusive through voice-based interaction.

## 👨‍💻 Author

**Praneeth Kumar Chikalametla**

GitHub: https://github.com/praneeth720/Voice-Based-Email-assistant

---

⭐ If you find this project useful, consider giving the repository a star!