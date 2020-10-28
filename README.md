# WebsiteEmailCollector

You can collect e-mails by using the Website Email Collector script. 

Create a TXT file that includes the list of website names in the file for each line.

E.G.

https://finage.co.uk
https://blog.finage.co.uk


Run the script by using the command given below.

>python3 app.py

It will ask you for the full path of the TXT file. Enter the full path and then press enter to continue.

Depending on the TXT file size, that might take some time. When the process is done, it will create a CSV file in the project file that includes the email list.


### Required Module

You can install the email_extractor module with the command given below.

>pip install email_extractor