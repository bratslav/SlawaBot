#!D:\SlawaBot\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'barcode==1.0.1','console_scripts','barcode'
__requires__ = 'barcode==1.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('barcode==1.0.1', 'console_scripts', 'barcode')()
    )
