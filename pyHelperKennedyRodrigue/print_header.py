import datetime
import os

def print_header():
    print("")
    print(f"date:       {datetime.datetime.now()}")
    print(f"script:     {os.path.realpath(__file__)}")
    print(f"user:       {os.environ['USER']}")
    print(f"host:       {os.environ['HOSTNAME']}")
    print("")
    print(f"sub:        {sub}")
    print(f"ses:        {ses}")
    print("")
    start_time = datetime.datetime.now()
    return start_time