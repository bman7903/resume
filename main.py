from google.appengine.api.logservice import logservice
from google.appengine.api import users, urlfetch

from base64 import urlsafe_b64decode
from random import choice, getrandbits
from time import time
from re import sub
from os import environ

import webapp2, cgi
import requests, json, hashlib
import logging

from ath import mlab
from res import Resume

mongolab_key = str( mlab('mkey') )
tusr_db      = str( mlab('m_db') )

def Headers( headers, proc ):
  g    = str( headers )
  proc = str( proc )
  logging.info( g )
  def all():
     h = []
     for e in str( headers ).split('\n'):
       e = str( e )
       h.append(e)
     return h
  def item():
     for e in str( headers ).split('\n'):
       e = str( e )
       if '-' in e:
          if '_' in e:
            itm = str( e.split('=')[0] )
            id  = str( itm.split('_')[-1] )
            if len( id ) == 25:
               if id[0].isdigit():
                 return itm
  t = eval( proc )
  return t()

class Rez(webapp2.RequestHandler):
  def do(self, proc):
     proc = str( proc )
     HTML = str( Resume( 'one', 'two' ) )
     self.response.write( HTML )
  def post( self ):
     self.do( 'pst' )
  def get( self ):
     self.do( 'get' )


class MainPage(webapp2.RequestHandler):
  def do(self, proc):
        proc = str( proc )
        try:
          offset    = self.request.get('offset') or None
          if offset:
             offset = urlsafe_b64decode(str(offset))
        except:
          offset    = None
        end_time    = time()
        count       = 5
        show_next   = False
        last_offset = None
        i           = 1
        for req_log in logservice.fetch(end_time=end_time, offset=offset, 
        minimum_log_level=logservice.LOG_LEVEL_INFO, include_app_logs=True):
          ip        = str( req_log.ip )
          rq        = str( req_log )
          meth      = str( req_log.method )
          rec       = str( req_log.resource )
          if rec   == '/celtic.png':
             self.response.headers['Content-Type'] = 'image/png'
             a      = open( 'celtik.png', 'rb' )
             for e in a:
                self.response.out.write( e )
          if not rec == '/celtic.png':
             logging.info( 'Bad Request:  %s %s' % ( proc, rec ) )
#             self.response.write( 'You appear to be lost?' )

  def post( self ):
     self.do( 'pst' )
  def get( self ):
     self.do( 'get' )

app = webapp2.WSGIApplication([
    (           '/', MainPage ),
    ( '/celtic.png', MainPage ),
    ( '/resume.html', Rez ),
], debug=True)
