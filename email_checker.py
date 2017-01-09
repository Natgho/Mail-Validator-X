# Coded by : Sezer Yavuzer Bozkır - 2017

from validate_email import validate_email
mails = tuple(open('mails.txt', 'r').read().split('\n'))

with open("results.txt", "w") as myfile:
    for mail in mails:
        is_valid = validate_email(mail, verify=True, check_mx= True)
        myfile.write("Mail:{}, Validation: {}\n".format(mail, is_valid))