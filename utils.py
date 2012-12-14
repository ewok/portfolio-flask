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

