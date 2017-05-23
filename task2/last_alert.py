#!/usr/bin/python
import re
import os.path

fname = '/var/ossec/logs/alerts/alerts.log'
regex_timestamp = re.compile('[0-9]{4} [a-zA-Z]{3} [0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}')
regex_rule_id = re.compile('Rule: [0-9]*')
regex_rule_level = re.compile('\(level [0-9]*\)')
regex_log_file = re.compile('->.*')
regex_integer = re.compile('[0-9]+')

if os.path.isfile(fname):
    file_content = open(fname, 'r').read()
    alerts = file_content.split('\n** ')
    if len(alerts) > 1:
        alert = alerts[len(alerts) - 1]
        lines = alert.split('\n')
        timestamp = regex_timestamp.findall(lines[1])[0]
        rule_id = regex_integer.findall(regex_rule_id.findall(lines[2])[0])[0]
        rule_level = regex_integer.findall(regex_rule_level.findall(lines[2])[0])[0]
        log_file = regex_log_file.findall(lines[1])[0].split("->", 1)[1]
        print "Timestamp: " + timestamp
        print "Rule ID: " + rule_id
        print "Rule Level: " + rule_level
        print "Log file:" + log_file
    else:
        print "The file " + fname + " does not content any alert log"
else:
    print "The file " + fname + " does not exist"
