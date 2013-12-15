#coding=utf-8

import httplib
import urllib, urllib2
import json
import base64
import functools
import logging
import time


class RequestApi(object):

    TimeOut = 3
    DEBUG_LEVEL = 7
    HOST = "api.douban.com"

    @classmethod
    def request(cls, method, path, params, headers={}, newHost=''):
        """test ---  http://api.douban.com/book/subject/1220562?alt=json """
        _headers = {'Accept-Language': 'zh-cn', 'User-Agent': 'Python/Automate', "Accept-Charset": "utf-8"}
        _headers.update(headers)

        host = newHost == '' and cls.HOST or newHost
        conn = httplib.HTTPConnection(host, timeout=cls.TimeOut)
        
        for k, v in params.items():
            if v == '' or v == None:
                del params[k]

        params = urllib.urlencode(params)
        if method == "GET":
            path = "%s?%s" % (path, params)
            params = ''
        else:
            path = "%s" % path
            
        logging.debug("*[Requst]* %s %s %s" % (method, host + path, params))
        conn.request(method, path, params, _headers)
        conn.set_debuglevel(cls.DEBUG_LEVEL)
        try:
            r = conn.getresponse()
            data =  r.read()
            return data
        except Exception,e:
            logging.error("*[Requst]* %s %s %s request error:%s" % (method, host + path, params,e))
            raise e
        finally:
            conn.close()

    @classmethod
    def get(cls, path, params, headers={}, newHost=''):
        return cls.request("GET", path, params, headers, newHost)

    @classmethod
    def get_json(cls, path, params, headers={}, newHost=''):
        return json.loads(cls.request("GET", path, params, headers, newHost))

    @classmethod
    def post(cls, path, params, headers={}, newHost=''):
        return cls.request("POST", path, params, headers, newHost)

    @classmethod
    def post_json(cls, path, params, headers={}, newHost=''):
        return json.loads(cls.request("POST", path, params, headers, newHost))

        
