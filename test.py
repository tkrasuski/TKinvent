# -*- coding: utf-8 -*-
import helper as hlp
#import simplejson as js
talk = hlp.Talk()
def test_login():
    '''
    tests login to service
    '''
    talk.login_()
#test_login()
print "get some data"
service = '/default/service' 
#data = talk.get_(service)
#data=data['content']
#print data
#for i in data:
 #   print i['jedn_kierujaca']
data = dict(line='to jest linia')
talk.data=data
ret = talk.post_(service)
print ret
