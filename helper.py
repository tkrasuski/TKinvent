# -*- coding: utf-8 -*-
import json as js
import requests as rq
import settings as stt


class Talk(object):
    '''
    comuniation with ...
    '''
    def __init__(self):
        self.url = None
        self.user = stt.user
        self.password = stt.sign
        self.data= None
        self.session = rq.session()
        self.headers =  {'Content-type': 'application/json', 'Accept': 'text/plain'}
    def post_(self, msg):
        '''
        sends data
        '''
        if msg:
            req = self.session.post(stt.url+msg, data=js.dumps(self.data), headers=self.headers,verify=False)
            if req.status_code == 200:
                
                return req.text
            else:
                return req.status_code
        else:
            return None
    def get_(self, msg):
        '''
        gets data
        '''
        self.login_()
        req = self.session.get(stt.url+msg, headers=self.headers,verify=False)
        if req.status_code ==200:
            ret = js.loads(req.text)
            return ret
        else:
            return 'ERROR:' + req.text
    def put_(self, msg):
        '''
        does nothing 
        '''
        pass
    def login_(self):
        '''
        logs in to service
        '''
        data = dict(login=stt.user, passwd=stt.sign)
        req = self.session.get(stt.url+'/serwisy/logmein?login=%s&passwd=%s'%(stt.user, stt.sign), headers=self.headers,verify=False)
       # req = self.session.get(stt.url+'/serwisy/logmein?login=tomek&passwd=76419c58730d9f35de7ac538c2fd6737', headers=self.headers,verify=False)
        if req.status_code ==200:
            return req.text
        else:
            print req.text
            return 'login error'
