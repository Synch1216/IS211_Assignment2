import datetime
import urllib2
import csv
import logging
import sys
import argparse

def downloadData(url):
    url = ' http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    response = urllib2.urlopen(url)
    return response

def processData():
    try:
    csv_is = csv.reader(response)
    format= "%d %m %Y"
    bday = datetime.strptime(personData[id],[1], format)
    
    except:
        print "Invalid ID"
        
    finally:
        response.close
        
        