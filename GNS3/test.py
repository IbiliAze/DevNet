import os
import json
import xmltodict
import yaml
from ncclient import manager

with open('vars.yml', 'r') as handle:
    host_root = yaml.safe_load(handle)
print(host_root)