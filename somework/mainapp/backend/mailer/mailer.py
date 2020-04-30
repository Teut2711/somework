from xlrd import open_workbook
import pandas as pd
import codecs
import os
import mimetypes
from email.message import EmailMessage
import pathlib
import smtplib


def run(self):

    df = get_dataframe(self.excel_file)
    nrows = df.shape[0]

    for index, row in df.iterrows():
        to, file_path, subject, message_file, from_ = *[
            i.strip() for i in row.tolist()
        ], self.settings["mailfrom"]

        try:
            msg = self.prepMail(from_, to, file_path, subject,
                                message_file)
        except ValueError:
            self.sent_to.emit(
                "Subject is Absent.. Mail not sent  to {to}", -1)
        except Exception as e:
            self.sent_to.emit(
                f"{getattr(e, 'message', repr(e))}\n{index} {to}", -1)
        else:
            try:
                self.fireMail(msg)

            except Exception as e:
                self.sent_to.emit(getattr(e, 'message', repr(e)), -1)

            else:
                self.sent_to.emit("Sent mail to :::  " + to,
                                  ((index + 1) * 100) // nrows)


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
        self.msg['From'] = self.from_

    def prep_to(self, to):
        to = ", ".join(to.split())
        self.msg["To"] = to

    @prevent_failure
    def prep_file(self, file_paths):
        for fil in map(lambda x: x.strip(), file_paths.split(",")):
            if os.path.exists(fil):
                with open(os.path.join(fil), "rb") as f:
                    file_data = f.read(fil)
                    file_name = pathlib.Path(fil).name
                maintype, subtype = get_mime(fil).split("/")
                self.msg.add_attachment(file_data,
                                        maintype=maintype,
                                        subtype=subtype,
                                        filename=file_name)

    def prep_subject(self, subject):
        subject = subject.strip()
        if subject is None:
            raise ValueError(f"Invalid Subject < {subject} >")
        self.msg['Subject'] = subject

    @prevent_failure
    def prep_message(self, file_path):
        with codecs.open(file_path, "r") as f:

            self.msg.add_alternative('''
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
    for index, row in pd.read_excel(excel_file_obj, dtype=str, keep_default_na=False):
        msg = MessagePrep(row)

        with smtplib.SMTP(host,
                          587) as smtp:
            smtp.starttls()
            smtp.login(user=email_address,
                       password=password)
            smtp.send_message(msg)
