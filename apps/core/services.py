from datetime import datetime
from ipware import ip
import random
import string


def random_string(length=10, chars='default'):
    if chars == 'default':
        chars = string.ascii_letters + \
                string.digits
    return ''.join(random.choice(chars) for x in range(length))


def unique_filename(filename):
    datetime_stamp = datetime.now().strftime('%y%m%d%H%M%S%f')
    split_filename = filename.split('.')

    timestamped_filename = '%s_%s' % (datetime_stamp, split_filename[0])
    file_extension = '.'.join(split_filename[1:])
    filename = '%s.%s' % (timestamped_filename, file_extension)
    return filename


def get_ip_address(request):
    ip_address = ip.get_real_ip(request)

    if not ip_address:
        ip_address = ip.get_ip(request)
    return ip_address
