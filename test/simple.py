#!/usr/bin/env python
#-------------------------------------------------------------------------------
#-
#-------------------------------------------------------------------------------
#-
#-
#-
#-------------------------------------------------------------------------------
#-
#-    Filename: simple.py
#-
#-    Author:   Stephen Bates
#-    Project:  sbates130272/kinetic
#-
#-  ---------------------------------------------------------------------------
#-
#-  Description
#-  -----------
#-
#-  A very simple test that attempts to connect to a Seagate Kinetic IP drive
#-  at a specified IP address and port and perform a simple key-value
#   put and get. 
#-
#------------------------------------------------------------------------------

import optparse

from kinetic import Client

if __name__=="__main__":

    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", action="store", default="127.0.0.1",
                      help="the domain name or IP address of the Kinetic drive")
    parser.add_option("-p", "--port", action="store", default=8153,
                      help="the open port on the IP drive")
    parser.add_option("-k", "--key", action="store", default="testkey",
                      help="the key of the key-value test pair")
    parser.add_option("-v", "--value", action="store", default="0xdeadbeef",
                      help="the value of the key-value test pair")
    (options, args) = parser.parse_args()

    c = Client(options.ip, options.port)
    c.put(options.key,options.value)
    value = c.get(options.key).value

    if value==options.value:
        print "Test PASSED : key=%s - value=%s" % (options.key,options.value)
        exit(0)
    else:
        print "Test FAILED : key=%s - value=%s/=%s" % \
            (options.key,options.value,value)
        exit(-1)

        
