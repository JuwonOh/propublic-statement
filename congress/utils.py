"""
Utility functions and error classes used throughout client classes
"""
import math
import six
import requests
import datetime
from time import gmtime, strftime
from bs4 import BeautifulSoup

user_dateformat = '%Y-%m-%d'

class CongressError(Exception):
    """
    Exception for general Congress API errors
    """
    def __init__(self, message, response=None, url=None):
        super(CongressError, self).__init__(message)
        self.message = message
        self.response = response
        self.url = url


class NotFound(CongressError):
    """
    Exception for things not found
    """


def check_chamber(chamber):
    "Validate that chamber is house or senate"
    if str(chamber).lower() not in ('house', 'senate'):
        raise TypeError('chamber must be either "house" or "senate"')


def get_congress(year):
    "Return the Congress number for a given year"
    if year < 1789:
        raise CongressError('There was no Congress before 1789.')

    return int(math.floor((year - 1789) / 2 + 1))


def parse_date(s):
    """
    Parse a date using dateutil.parser.parse if available,
    falling back to datetime.datetime.strptime if not
    """
    if isinstance(s, (datetime.datetime, datetime.date)):
        return s
    try:
        from dateutil.parser import parse
    except ImportError:
        parse = lambda d: datetime.datetime.strptime(d, "%Y-%m-%d")
    return parse(s)


def u(text, encoding='utf-8'):
    "Return unicode text, no matter what"

    if isinstance(text, six.binary_type):
        text = text.decode(encoding)

    # it's already unicode
    text = text.replace('\r\n', '\n')
    return text


CURRENT_CONGRESS = get_congress(datetime.datetime.now().year)

def get_soup(url, headers=None):
    """
    Arguments
    ---------
    url : str
        Web page url
    headers : dict
        Headers for requests. If None, use Mozilla/5.0 as default user-agent

    Returns
    -------
    soup : bs4.BeautifulSoup
        Soup format web page
    """

    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    html = r.text
    page = BeautifulSoup(html, 'lxml')
    if not page:
        page = 'page error'
    return page

def parse_content(soup):
    sub_links = soup.find_all('p')
    content = [i.text for i in sub_links]
    if not content:
        content = soup.find('div', id='content')
    return content

def strf_to_datetime(strf, form):
    return datetime.strptime(strf, form)
