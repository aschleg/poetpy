import requests
from urllib.parse import urljoin


def get_poem(input_term, search_term, search_type=None, output=None, output_format=None):
    uri = 'http://poetrydb.org'

    if input_term not in ('author', 'title', 'lines', 'linecount'):
        raise ValueError("input term must be one of 'author', 'title', 'lines', or 'linecount'.")

    parameters = (input_term, search_term, search_type, output, output_format)
    parameters = [para for para in parameters if para not in {None, ''}]

    for p in parameters:
        uri = urljoin(uri, p) + '/'

    if uri[-2:] == '//':
        uri = uri[:-2]
    elif uri[-1:] == '/':
        uri = uri[:-1]

    return uri
