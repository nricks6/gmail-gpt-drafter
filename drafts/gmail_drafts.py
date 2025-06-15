import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import Resource

def create_draft_reply(service: Resource, original_message_id: str, to_email: str, subject: str, body: str):
    # Construct the email
    message = MIMEText(body)
    message['to'] = to_email
    message['subject'] = f"Re: {subject}"
    message['In-Reply-To'] = original_message_id
    message['References'] = original_message_id

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    draft_body = {
        'message': {
            'raw': raw
        }
    }

    try:
        draft = service.users().drafts().create(userId='me', body=draft_body).execute()
        print(f"✅ Draft created with ID: {draft['id']}")
    except Exception as e:
        print(f"⚠️ Failed to create draft: {e}")
