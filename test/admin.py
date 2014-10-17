#!/usr/bin/env python
#-------------------------------------------------------------------------------
#-
#-------------------------------------------------------------------------------
#-
#-
#-
#-------------------------------------------------------------------------------
#-
#-    Filename: admin.py
#-
#-    Author:   Stephen Bates
#-    Project:  sbates130272/kinetic
#-
#-  ---------------------------------------------------------------------------
#-
#-  Description
#-  -----------
#-
#- Perform a simple set of admin tests on a Seagate Kinetic IP drive.
#-
#------------------------------------------------------------------------------

import optparse
import kinetic

if __name__=="__main__":

    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", action="store", default="127.0.0.1",
                      help="the domain name or IP address of the Kinetic drive")
    parser.add_option("-p", "--port", action="store", default=8153,
                      help="the open port on the IP drive")
    (options, args) = parser.parse_args()

    c = kinetic.admin.AdminClient(options.ip, options.port)

    x = kinetic.common.LogTypes()
    print c.getLog(x.all())
