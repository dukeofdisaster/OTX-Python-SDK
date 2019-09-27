#!/usr/bin/env python
import ConfigParser
import datetime
import json
from OTXv2 import OTXv2
from StixExport import StixExport
import sys
from taxii_client import Client


def main():
  config = ConfigParser.ConfigParser()
  config.read('config.cfg')
  otx = OTXv2(config.get('otx', 'key'))

  # use an ago time to setup a poll with various intervals
  ago = (datetime.datetime.now() - datetime.timedelta(minutes=10)).isoformat()
  # or just grab everything
  # pulses = otx.getall_iter(); #<-- Returns a generator object
  pulses = otx.getsince(ago) # <-- Returns a list
  #pulses = otx.getevents_since(ago)
  all_data = {}
  updated = 0
  for i in pulses:
    all_data.update(i)
    updated += 1
    #print(json.dumps(i))
  with open('dump.txt', 'w+') as f:
    f.write(json.dumps(all_data))

  print("updated:", updated)


if __name__ == "__main__":
  main()
