##################### Normal Starting Project ######################
import random
from datetime import datetime
import pandas
import smtplib

my_email = "mypython92@gmail.com"
password = "jklfpaefxiaagwqk"

now = datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        replaced = contents.replace("[NAME]", birthdays_person['name'])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person.email,
                            msg=f"Subject:Happy Birthday\n\n{replaced}")
