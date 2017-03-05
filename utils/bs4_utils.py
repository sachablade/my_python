from bs4 import BeautifulSoup
from utils.json_utils import Utilsjson
import urllib2


class Bs4(Utilsjson):
    def __init__(self, url):
        super(Bs4, self).__init__()
        resp = urllib2.urlopen(url)
        self.encoding = resp.info().getparam('charset')
        self.soup = BeautifulSoup(resp, "html.parser",
                                  from_encoding=self.encoding)

    def __repr__(self):
        return self.to_json()

    def get_all_links(self, href=True):
        return self.soup.find_all('a', href=href)


