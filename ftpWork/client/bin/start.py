import os
import sys

sys.path.append(os.path.dirname(os.getcwdb()))

from core import client
if __name__ == '__main__':
    client.main()