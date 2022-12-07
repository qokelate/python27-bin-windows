#!F:\windows\tools\IDA_v7.0.170914_english\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wasm==1.2','console_scripts','wasmdump'
__requires__ = 'wasm==1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wasm==1.2', 'console_scripts', 'wasmdump')()
    )
