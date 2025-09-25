import re


def combine_handles(emails):
    return ','.join(re.findall('([\w]+)@',i)[0] for i in emails)