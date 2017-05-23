#!/usr/bin/python

import re
import os.path
import sys

def month_to_number(month):
    if month == 'Jan':
        return '01'
    elif month == 'Feb':
        return '02'
    elif month == 'Mar':
        return '03'
    elif month == 'Apr':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'Jun':
        return '06'
    elif month == 'Jul':
        return '07'
    elif month == 'Aug':
        return '08'
    elif month == 'Sep':
        return '09'
    elif month == 'Oct':
        return '10'
    elif month == 'Nov':
        return '11'
    else:
        return '12'

def print_info(alert):
    lines = alert.split('\n')
    timestamp = regex_timestamp.findall(lines[1])[0]
    rule_id = regex_integer.findall(regex_rule_id.findall(lines[2])[0])[0]
    rule_level = regex_integer.findall(regex_rule_level.findall(lines[2])[0])[0]
    log_file = regex_log_file.findall(lines[1])[0].split("->", 1)[1]
    print "Timestamp: " + timestamp
    print "Rule ID: " + rule_id
    print "Rule Level: " + rule_level
    print "Log file: " + log_file

def get_last_alert(date, alerts):
    split_date = date.split("/")
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]
    out = ''
    for alert in alerts:
        lines = alert.split('\n')
        timestamp = regex_timestamp.findall(lines[1])[0]
        split_timestamp = timestamp.split(" ")
        log_year = split_timestamp[0]
        log_month = month_to_number(split_timestamp[1])
        log_day = split_timestamp[2]
        if year == log_year and month == log_month and day == log_day:
            out = alert
        else:
            if out: # logs are ordered and we have read all of them that match with the given date
                return out
    return out

fname = '/var/ossec/logs/alerts/alerts.log'
regex_date = re.compile('\d{4}/\d{2}/\d{2}')
regex_timestamp = re.compile('\d{4} \w{3} \d{2} \d{2}:\d{2}:\d{2}')
regex_rule_id = re.compile('Rule: \d*')
regex_rule_level = re.compile('\(level \d*\)')
regex_log_file = re.compile('->.*')
regex_integer = re.compile('\d+')
usage = "Usage:\n  " + sys.argv[0] + "   for getting last alert information\n  " + sys.argv[0] + " -d YYYY/MM/DD   for getting last alert information giving a day"

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if os.path.isfile(fname):
        file_content = open(fname, 'r').read()
        alerts = file_content.split('\n** ')
        if len(alerts) > 1:
            if len(sys.argv) == 1:
                alert = alerts[len(alerts) - 1]
                print_info(alert)
            else:
                if sys.argv[1] == "-d" and regex_date.match(sys.argv[2]) is not None:
                    alert = get_last_alert(sys.argv[2], alerts)
                    if alert:
                        print_info(alert)
                    else:
                        print "There is no alert for the day given"
                else:
                    print "Bad usage of arguments\n" + usage
        else:
            print "The file " + fname + " does not content any alert log"
    else:
        print "The file " + fname + " does not exist"
else:
    print "Incorrect number of arguments\n" + usage
