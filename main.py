from auth.gmail_auth import get_gmail_service
from gmail.reader import get_latest_unread_email
from openai.gpt_drafter import generate_draft_reply

def main():
    print("🔐 Authenticating with Gmail...")
    service = get_gmail_service()

    print("📥 Checking for new emails...")
    email_data = get_latest_unread_email(service)

    if email_data:
        print(f"\n📧 Subject: {email_data['subject']}")
        print(f"📝 Body:\n{email_data['body']}")

        print("\n🤖 Generating a draft reply with ChatGPT...")
        draft = generate_draft_reply(email_data['subject'], email_data['body'])

        print("\n✍️ Draft Reply:")
        print(draft)

        # (Next step: Save the draft via Gmail API)

    else:
        print("✅ No unread emails found.")

if __name__ == "__main__":
    main()
