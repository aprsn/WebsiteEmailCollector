from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser
import datetime
import csv

file_location = input("Enter the TXT path: ")
reader = open(file_location, "r")
email_list = []

print(datetime.datetime.now())
for row in reader:
  print("Looking at: ", row)

  with RequestsBrowser() as browser:
      email_extractor = EmailExtractor(row, browser, depth=2)
      emails = email_extractor.get_emails()

      for email in emails:
          email_list.append(email.as_dict()["email"])
          print(email.as_dict())

      browser.close

current_date = datetime.datetime.now()
exported_file = "emails" + str(current_date) + ".csv"
with open(exported_file, 'w', newline='') as newFile:
     fieldname = ['email']
     wr = csv.DictWriter(newFile, fieldnames=fieldname)
     wr.writeheader()
     for email in email_list:
         wr.writerow({'email': email})


