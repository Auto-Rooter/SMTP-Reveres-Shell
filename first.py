import imaplib
import email

message = imaplib.IMAP4_SSL("imap.gmail.com")
message.login("YOUR_EMAIL_ADDRESS", "YOUR_EMAIL_PASSWORD")
message.select("inbox")
_, data = message.search(None, "UNSEEN") # Get all un-read emails

for x in data[0].split():
    _, msg = message.fetch(x, 'RFC822')
    _, g = msg[0]
    data_email = email.message_from_bytes(g)
    
    for m in data_email.walk():
        if m.get_content_type() == "text/plain":
            body = m.get_payload(decode=True)
            d = body.decode("utf-8")
            print("[*] Email Payload: " + d)