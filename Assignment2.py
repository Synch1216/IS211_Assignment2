__author__ = 'malcolmbarnes'

import urllib2
import argparse
import random
import logging
import pprint
import datetime

# set up objects for main, downloadData, processdATA, DisplayPerson.

def main():

    logging.basicConfig(filename='errors.log', level=logging.ERROR)
    logger = logging.getLogger('assignment2.py')

    def downloadData(url):
        response= urllib2.urlopen(url)
        return response

        def processData(content):
            exccept_file= csv.reader(content)
            dictionary= {}
            date_format= '%d/%m/%Y'

            for row in exccept_file:
                if row [0] == 'id':
                    continue

                else:
                    try:
                        row[1]=datetime.datetime.strptime(row[1],date_format)

                    except:
                        line= int(row[0])+1
                        logger.error('Error on {0} ID {1}'.format(line, id))

                    finally:
                        dictionary[int(row[0])]= (row[1], row[2])

                        return dictionary

                    def displayPerson(id,personData):
                        try:
                            date_format= '%d/%m/%Y'
                            print response.format(id=id, name=personData[id][0],date= str(Data[id][1].split('')[0])
                        except enterError:
                            print 'No such id'

                            url_parser= argparse.ArgumentParser()
                            url_parser.add_argument("url", help='Enter URL to convert to CSV', type=str)
                            args= url_parser.parse_args()

                            if args.url:
                                try:
                                    csv=downloadData(args.url)
                                    person=processData(csv)
                                    enter= "Enter ID (press 0 or negative number to exit):"

                                    boolean= True

                                    while boolean:
                                        try:
                                            user= int(raw_input(enter))

                                        except:
                                            print "Enter a number"

                                            if user>0:
                                                displayPerson(user,personData)

                                            else:
                                                print "Exit"
                                                boolean= False


                                        if __name__=="__main__":
                                            main()
                                            















