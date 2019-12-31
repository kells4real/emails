import os, csv, smtplib, ssl

message = """Subject: Testing Python Message Capabilities

Hi {name}, welcome to the world of python... """
from_address = os.environ.get("EMAIL_HOST_USER")
password = os.environ.get("EMAIL_HOST_PASSWORD")

get_file = input("""Enter File Name Plus Extension, E.g: contacts.csv
             Make Sure It's A .csv File,
             If The File Isn't In The Same Directory As The Program,
             Then Be Sure To Copy The Full Path Of The File With Extension
             E.g: C:/Users/james/Documents/New/contacts.csv
             : """)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open(get_file) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            try:  
                server.sendmail(
                  from_address,
                  email,
                  message.format(name=name),
                  )
                print(f"Message Sent To {name}")
                
            except Exception:
                  print()
                  print(f"Message Was Not Sent To {name}, Please Confirm Email Address Is Correct")
                  print()
print()
print("Messages Have Been Sent...")

# import csv

# with open("users.csv") as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip header row
#     for name, email in reader:
#         print(f"Sending message to {name} with email address: {email}")
        


