#!/Users/lcross/anaconda3/bin/python3.7

######################################################################
# Central Process Management Application Server                      #
# Version 1.0                                                        #
# Developed by: Lawrence Cross                                       #
# Date: July 16, 2019                                                #
######################################################################

######################################################################
# Imports                                                            #
######################################################################
import string
import socket
import sys
import json
import requests
from   requests  import Request, Session
from   _thread   import *
from   threading import *


######################################################################
# Variables for the machine to machine communication                 #
######################################################################
TCP_IP         = 'localhost'
TCP_PORT       = 5005
BUFFER_SIZE    = 2008  
DATA           = ''
DATA_EXPECTED  = 0
DATA_RECEIVED  = len(DATA)
TCP_SERVER     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



