import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application")
olapp = outlook.GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
for message in messages:
    subject = message.Subject
    body = message.body
    print(body)
