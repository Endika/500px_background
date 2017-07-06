import re
import requests
from uuid import uuid4


def get_urls(url_root, html):
    """Get url from html."""
    expression = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
                  '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return [x for x in re.findall(expression, html) if url_root in x]

# html_file_list = [open('photo.html').read(),
#                   open('photo2.html').read(),
#                   open('photo3.html').read()]
html_file_list = [open('YOUR_FILE.html').read(),
                  open('YOUR_FILE.html').read(),
                  open('YOUR_FILE.html').read()]
for html in html_file_list:
    for url in get_urls('https://500px.com/photo/', html):
        try:
            open('{}.jpg'.format(uuid4().hex), 'w').write(
                requests.get(get_urls('https://drscdn.500px.org/photo/',
                             requests.get(url).content)[0][:-1]).content)
        except Exception as e:
            pass
