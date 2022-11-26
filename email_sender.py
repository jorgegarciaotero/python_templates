from pretty_html_table import build_table
from datetime import timedelta
import numpy as np
import math
import sqlalchemy
import sys

def sendEmail(my_ip,fileDirectory, filename, subject, body, from_addr, to_addrs, cc_addrs=None, bcc_addrs=None):
    '''
    Method for sending emails. receives
    filename: entry file
    from_addr: email sender
    to_addrs:  email receiver
    cc_addrs:  email copy receivers
    bcc_addrs: email hidden receivers
    '''
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = from_addr
    message["To"] = ", ".join(to_addrs)
    message["Subject"] = subject
    if (cc_addrs and len(cc_addrs) > 0):
        message['Cc'] = ','.join(cc_addrs)
    if (bcc_addrs and len(bcc_addrs) > 0):
        message['Bcc'] = ','.join(bcc_addrs)
    # Add body to email
    message.attach(MIMEText(body, "html"))
    # Open PDF file in binary mode
    if not (filename is None):
        with open(fileDirectory+filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        # Add attachment to message and convert message to string
        message.attach(part)
    text = message.as_string()
    # Log in to server using secure context and send email
    server = smtplib.SMTP(my_ip, 25)
    server.ehlo()
    server.starttls()
    server.ehlo()
    if (bcc_addrs == None) and (cc_addrs == None):
        recipients = to_addrs
    elif (bcc_addrs != None):
        recipients = to_addrs+bcc_addrs
    else:
        recipients = to_addrs+cc_addrs
    server.sendmail(from_addr, recipients, text)
    server.quit()
    return


def configureEmail(absolutepath,fileDirectory,filename,priority,lvl,group,vertical,df,logger):
    absolutepath = os.path.abspath(__file__)
    fileDirectory = os.path.dirname(absolutepath)+'/'
    from_addr = dpo_whispering@vodafone.com
    table= """
        <html>
            <head>
            </head>
            <body>
                {0}
            </body>
        </html>
    """.format(build_table(df, 'blue_light'),font_size='small')
    to_addrs=['email1@email.com','email2@email.com']
    body="""Hello \n Lorem. \n
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
            dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
            ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat.
            """ +table+"""
            Thanks in advance \n Jorge."""

    subject = "[EMAIL]  "+lvl+" Prio "+priority+" "+vertical+ " "+group
    my_ip='123.123.123.123'
    es.sendEmail(my_ip,fileDirectory,filename,subject,body,from_addr,to_addrs)
    return



def main(argv):
    print('hello word')
    '''email_sender.py'''

    
if __name__ == "__main__":
    main(sys.argv[1:])
