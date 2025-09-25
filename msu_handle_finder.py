from html import load_html
from extract import extract_emails
from edufinder import filter_edu
from combine import combine_handles

import sys

def msu_handle_finder(source: str) -> str:
    """
    This main function executes the entire pipeline.

    [save this in finder.py]
    """
    html = load_html(source)
    emails = extract_emails(html)
    edu_emails = filter_edu(emails)
    return combine_handles(edu_emails)


if __name__ == '__main__':
    url = sys.argv[1]
    handles = msu_handle_finder(url)

    if len(handles) > 0:
        print('MSU handles found!')
        print(handles)
    else:
        print('No MSU handles found') 