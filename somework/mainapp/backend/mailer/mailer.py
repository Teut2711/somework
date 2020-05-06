from xlrd import open_workbook
import pandas as pd
import codecs
import os
import mimetypes
import pathlib
import smtplib
from django.core.mail import EmailMessage
from itertools import islice

from django.core import mail
connection = mail.get_connection()

class MessagePrep:
    from_ = None

    def prevent_failure(func):
        def inner_function(self, arg):
            arg = arg.strip()
            if arg:
                func(self, arg)
        return inner_function

    def __init__(self, row):
        self.msg = EmailMessage()
        self.prep_to(row[0])
        self.prep_file(row[1])
        self.prep_subject(row[2])
        self.prep_message(row[3])

    def prep_from(self):
        self.msg.from_email(self.from_)

    def prep_to(self, to):
        to = list(lambda x:x.strip(), to.split())
        self.msg.to(to)
        
    @prevent_failure
    def prep_file(self, file_paths):
        for fil in map(lambda x: x.strip(), file_paths.split(",")):
            if os.path.exists(fil):
                with open(os.path.join(fil), "rb") as f:
                    file_data = f.read(fil)
                    file_name = pathlib.Path(fil).name
                self.msg.attach(file_name, file_data, get_mime(fil))

    def prep_subject(self, subject):
        subject = subject.strip()
        if subject is None:
            raise ValueError(f"Invalid Subject < {subject} >")
        self.msg.subject(subject)

    @prevent_failure
    def prep_message(self, file_path):
        with codecs.open(file_path, "r") as f:

            self.msg.attach_alternative('''
            <!DOCTYPE html>
                <html>
                    <body>
                    %s    
                    </body>
                </html>'''.format(f),
                subtype='html')

    @staticmethod
    def get_mime(path):
        mime = mimetypes.guess_type(path)[0]
        if mime:
            return mime
        elif path.endswith(".rar"):
            return "application/x-rar-compressed"
        else:
            raise TypeError("Filetype not supported invalid")


def main(host, email_address, password, excel_file_obj):
    MessagePrep._from = email_address
    for index, rows in islice(pd.read_excel(
        excel_file_obj.read(),
        dtype=str,
        keep_default_na=False).iterrows(),
            20):

        msg = [MessagePrep(row.tolist() )    for row in rows]
    
        with smtplib.SMTP(host,
                          587) as smtp:
            smtp.starttls()
            smtp.login(user=email_address,
                       password=password)
            smtp.send_message(msg)
