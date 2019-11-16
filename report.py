#!/usr/bin/env python

#standard lib
import time
import csv
import json
import sys

#open source
import requests


def main(argv):
    i = 0
    geo_data = list()
    data = list()
    with open(str(argv), 'r') as file:
        data = [json.loads(_row) for _row in file]

    for _row in data:
        r =requests.get('http://ip-api.com/json/' + str(_row.get('src_ip'))).json()
        geo_data.append(data_obj(_row.get('src_ip'), r.get('country')))
        curr = data_obj(_row.get('src_ip'), r.get('country'))
        i += 1
        if i == 44:
        	i = 0
        	print(json.dumps(curr, indent=4))
        	time.sleep(61)

   	with open('report.csv', 'w') as file:
   		fieldnames = ['ip', 'country']
   		writer = csv.DictWriter(file, fieldnames=fieldnames)
   		writer.writeheader()
   		for _row in geo_data:
   			writer.writerow(_row)

def data_obj(ip, country):
	data = {
	"ip": ip,
	"country": country
	}
	return data

if __name__ == '__main__':

	main(sys.argv[1])
