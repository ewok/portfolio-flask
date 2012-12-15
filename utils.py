import Image
from os import path
from config import IMAGES_PATH, IMAGES_URL

def generate_and_save_thumbnail(image_file, h, w):

    try:

        image_file_with_pass = IMAGES_PATH + image_file
        image_path = path.dirname(path.abspath(image_file_with_pass)) + '/'
        prefix = path.dirname(image_file) + '/'
        basename = path.basename(image_file_with_pass)
        thumb_name = 'T_' + basename

        if path.isfile(image_path + thumb_name):
            return prefix + thumb_name

        image = Image.open(image_path + basename)
        image.thumbnail((w, h), Image.ANTIALIAS)
        image.save(image_path + thumb_name)

        return prefix + thumb_name

    except:
        import sys
        print sys.exc_info()
        return None

# Make mail message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import quopri
def QuoHead(String):
    s = quopri.encodestring(String.encode('UTF-8'), 1, 0)
    return "=?utf-8?Q?" + s.decode('UTF-8') + "?="

def get_mail_body(name, email_from, email_to, subject, message):
    msg = MIMEMultipart()
    msg["Subject"] = QuoHead(subject).replace('=\n', '')
    msg["From"] = (QuoHead(name) + "  <" + email_from + ">").replace('=\n', '')
    msg["To"] = (" <" + email_to + ">").replace('=\n', '')
    text = MIMEText(message.encode('utf-8'), 'plain', 'UTF-8')
    msg.attach(text)
    return msg
