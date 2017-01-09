# Coded by : Sezer Yavuzer Bozkır - 2017

from pyisemail import is_email

mails = tuple(open('mails.txt', 'r').read().split('\n'))

with open("results2.txt", "w") as myfile:
    for mail in mails:
        is_valid = is_email(mail, check_dns=True, diagnose=True)
        myfile.write("Mail:{}, Validation: {}\n".format(mail, is_valid))