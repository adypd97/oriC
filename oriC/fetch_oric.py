#!/usr/bin/env python3

''' 
Just get the oriC of a given organism 
from the DoriC database website. 
The oriC sequence is stored in a <p> tag
in the html itself. we just scrape that from 
the website[1].

[1] WEBSITE LINK: http://tubic.tju.edu.cn/doric/public/index.php/information/bacteria/ori10010002.html

since, we are directly scraping, there could be 
issues in the future with this module as and when
the website changes (or goes down permanently).

NOTE: The nomenclature for the files saved at 
./data/ORG_TYPE/ORICXXXXXXXX.txt is same as 
one mentioned in the above website. The link 
is also an example link (default link)
'''

import sys
import os

# please check http://tubic.tju.edu.cn/doric/public/index.php/information
# for more on how to find ORG_UID.
ORG_TYPE = ["bacteria", "archaea", "plasmid"]
ORG_UID = sys.argv[1] if  (len(sys.argv) > 1) else "ORI10010002"
ORG_INDEX = sys.argv[2] if (len(sys.argv) > 2) else 0
URL = "http://tubic.tju.edu.cn/doric/public/index.php/information/{0}/{1}.html".format(ORG_TYPE[ORG_INDEX], ORG_UID)

# TODO: add other attributes
class oricBucket:
    ''' Holds information about the 
        organism (including oric sequence)
    '''
    def __init__(self, URL):
        self.URL = URL
        self._seq = oricBucket.fetch_oric(self.URL)

    @property
    def seq(self):
        return self._seq

    @staticmethod
    def is_cached(FILE_PATH):
        return True if os.path.exists(FILE_PATH) else False

    @staticmethod
    def fetch_oric(URL):
        '''Return all relevant data
           for organism
        '''
        from bs4 import BeautifulSoup as bs
        import bs4
        import requests

        terms = URL.split('/')
        DIR = os.getcwd() + "/data/{0}/".format(terms[-2])
        FILE_PATH = DIR + "/" + terms[-1].split(".")[0] + ".txt"

        if oricBucket.is_cached(FILE_PATH):
            ''' return from cache'''
            print("Available on disk\n")
            with open(FILE_PATH, 'r') as f:
                return f.read()
        else:
            response = requests.get(URL)
            soup = bs(response.content, 'html.parser')
            res = soup.find("table")
            for child in res.children:
                if isinstance(child, (bs4.element.Tag,)):
                    if "OriC Sequence" in child.td.string:
                        siblings = list(child.children)
                        oric_seq = siblings[3].p.string
                        oric_seq = oric_seq.lower()
            if not os.path.exists(DIR):
                os.mkdir(DIR)
            with open(FILE_PATH, 'w') as f:
                f.write(oric_seq)
            return oric_seq


if __name__ == "__main__":
    vibcho = oricBucket(URL)
    #print(vibcho.seq)
