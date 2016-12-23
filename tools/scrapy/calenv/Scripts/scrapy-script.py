#!c:\users\mloch\desktop\scrapy\calenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scrapy==1.2.1','console_scripts','scrapy'
__requires__ = 'scrapy==1.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scrapy==1.2.1', 'console_scripts', 'scrapy')()
    )
