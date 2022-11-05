import datetime
import os

def print_footer(start_time):
    print("")
    print(f"date:       {datetime.datetime.now()}")
    print(f"script:     {os.path.realpath(__file__)}")
    print(f"user:       {os.environ['USER']}")
    print(f"host:       {os.environ['HOSTNAME']}")
    print("")
    print(f"sub:        {sub}")
    print(f"ses:        {ses}")
    print("")
    print(f"duration:   {datetime.datetime.now() - start_time}")
    print("")