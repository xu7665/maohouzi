# -*- coding: utf-8 -*-
import hashlib
import web
class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello , this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "vincent"

            list = [token,timestamp,nonce]
            list.sort()
            shal = hashlib.sha1
            map(shal.update,list)
            hashcode = shal.hexdigest()
            print "handle/GET func: hashcode,signature:;",hashcode,signature
            if hashcode == signature:
                return echostr
            else::
            return ""
        except Exception,Argument:
            return Argument