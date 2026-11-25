import email
from email.mime.text import MIMEText
from datetime import datetime
import getpass
import imaplib
import smtplib
import pyttsx3
import speech_recognition as sr

# Initialize TTS engine
engine = pyttsx3.init()


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen(expect_keywords=None):
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            for _ in range(2):
                try:
                    speak("Listening...")
                    audio = r.listen(source, timeout=10, phrase_time_limit=7)
                    command = r.recognize_google(audio).lower()
                    print(f"You said: {command}")

                    if expect_keywords:
                        for word in expect_keywords:
                            if word in command:
                                return word
                        speak("Please say 'yes' or 'no'.")
                    else:
                        return command
                except sr.UnknownValueError:
                    speak("I couldn't understand that.")
                except sr.RequestError as e:
                    speak(f"Speech service error: {str(e)}")
    except Exception as e:
        speak(f"Microphone error: {str(e)}")

    speak("Voice not clear. Please type your response.")
    typed = input("You (typed): ").strip().lower()
    if expect_keywords:
        return typed if typed in expect_keywords else "no"
    return typed


def clean_email_input(raw_input):
    cleaned = raw_input.lower()
    replacements = [
        (" at the rate ", "@"),
        (" attherate ", "@"),
        (" at ", "@"),
        (" dot com ", ".com"),
        (" dotcom ", ".com"),
        (" dot ", "."),
        (" gmail ", "gmail.com"),
        (" gmailcom", "gmail.com"),
    ]
    for old, new in replacements:
        cleaned = cleaned.replace(old, new)

    cleaned = cleaned.replace(" ", "").strip()
    if cleaned.endswith("gmail"):
        cleaned += ".com"
    return cleaned


def classify_email(subject, body):
    keywords = ["urgent", "important", "meeting", "alert", "project", "payment"]
    text = f"{subject} {body}".lower()
    for word in keywords:
        if word in text:
            return "important"
    return "not important"


def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    return payload.decode(errors="ignore")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            return payload.decode(errors="ignore")
    return ""


def check_emails(email_addr, app_password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_addr, app_password)
        mail.select("inbox")

        today = datetime.today().strftime("%d-%b-%Y")
        status, messages = mail.search(None, f'(UNSEEN SINCE "{today}")')
        email_ids = messages[0].split() if messages and messages[0] else []

        if not email_ids:
            speak("You have no new emails today.")
            mail.logout()
            return

        count_to_show = min(2, len(email_ids))
        speak(
            f"You have {len(email_ids)} new email{'s' if len(email_ids) > 1 else ''} today. "
            f"Showing the latest {count_to_show}."
        )

        for i, e_id in enumerate(email_ids[:count_to_show], start=1):
            _, msg_data = mail.fetch(e_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            subject = msg["subject"] or "No subject"
            sender = msg["from"] or "Unknown sender"
            body = get_email_body(msg)

            speak(f"Email {i} from: {sender}")
            speak(f"Subject: {subject}")

            classification = classify_email(subject, body)
            speak(f"This email is marked as {classification}.")

            if classification == "not important":
                speak("Do you want to delete this email? Say 'yes' or 'no'.")
                if listen(expect_keywords=["yes", "no"]) == "yes":
                    mail.store(e_id, "+FLAGS", "\\Deleted")
                    speak("Email deleted.")

            if i < count_to_show and i + 1 <= len(email_ids):
                speak("Do you want to continue to the next email? Say 'yes' or 'no'.")
                if listen(expect_keywords=["yes", "no"]) != "yes":
                    break

        mail.expunge()
        mail.logout()
    except imaplib.IMAP4.error:
        speak("Login failed. Please check your email or app password.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")


def send_email(email_addr, app_password):
    try:
        speak("Please say the recipient name or email.")
        spoken_input = listen()
        if not spoken_input:
            speak("Recipient not provided.")
            return

        contacts = {
            "praneeth": "praneethkumar207576@gmail.com",
            "myself": "praneethkumar207576@gmail.com",
        }
        recipient = contacts.get(spoken_input.strip().lower())
        if not recipient:
            recipient = clean_email_input(spoken_input)

        speak(f"I understood the email as {recipient}")
        if "@" not in recipient or "." not in recipient:
            speak(f"Invalid email format: {recipient}")
            return

        speak("Please say the subject of the email.")
        subject = listen()
        if not subject:
            speak("Subject not provided.")
            return

        speak("Please dictate your message.")
        body = listen()
        if not body:
            speak("Message not provided.")
            return

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = email_addr
        msg["To"] = recipient

        speak("Sending your email...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_addr, app_password)
        server.sendmail(email_addr, recipient, msg.as_string())
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")


def assistant():
    speak("Welcome to Voice-Based Email Assistant.")
    email_addr = input("Enter your Gmail: ").strip()
    app_password = getpass.getpass("Enter your App Password: ").strip()

    try:
        speak("Verifying your account...")
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email_addr, app_password)
        imap.logout()
        speak("Account verified successfully.")
    except imaplib.IMAP4.error:
        speak("Login failed. Invalid email or password.")
        return
    except Exception as e:
        speak(f"Error: {str(e)}")
        return

    check_emails(email_addr, app_password)

    while True:
        speak("Say 'check' to check your inbox, 'send' to send an email, or 'exit' to quit.")
        command = listen()
        if "check" in command:
            check_emails(email_addr, app_password)
        elif "send" in command:
            send_email(email_addr, app_password)
        elif "exit" in command:
            speak("Exiting. Have a great day!")
            break
        else:
            speak("Sorry, I did not understand that.")


if __name__ == "__main__":
    assistant()