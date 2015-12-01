import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import urllib2
import sys

access_key = ""
secret_key = ""

keypart = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key').read()
access_key, secret_key = keypart.split(':')

print('> Access Key: ' + access_key)
print('> Secret Key: ' + secret_key)
print('> Boto Version: ' + boto.Version)
