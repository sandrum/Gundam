import lwsdk
import os, sys, math

# MobileSuit.py
# Layout plugin
# Bit/FinFunnel Plugin:

__author__     = "Ivan Sanchez"
__copyright__  = "Free"
__version__    = "0.01"
__maintainer__ = "Ivan Sanchez"
__email__      = "gundamproject@gmail.com"
__status__     = "Initial"
__lwver__      = "11"

class mobile_suit(lwsdk.IGeneric):
    def __init__(self, context):
        super(mobile_suit, self).__init__()

def process(self, generic_access):
    lwsdk.LWMessageFuncs().info('ガンダム、行きまーす！')
    return lwsdk.AFUNC_OK

ServerTagInfo = [
                    ( "MobileSuit Sortie", lwsdk.SRVTAG_USERNAME | lwsdk.LANGID_USENGLISH ),
                    ( "Gandamu, Ikimasu!", lwsdk.SRVTAG_BUTTONNAME | lwsdk.LANGID_USENGLISH ),
                    ( "Utilities/Python", lwsdk.SRVTAG_MENU | lwsdk.LANGID_USENGLISH )
                ]

ServerRecord = {lwsdk.GenericFactory("LW_MobileSuit", mobile_suit) : ServerTagInfo}


def main():
    print "Calculate Funnel deployment Vectors"

def deploy():
    print "Deploy funnels to target location"
