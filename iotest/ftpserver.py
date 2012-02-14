from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import FilePasswordDB
from twisted.internet import reactor

portal = Portal(FTPRealm('./'), [FilePasswordDB("passwd")])
ftpFactory = FTPFactory(portal)

reactor.listenTCP(8888, ftpFactory)
reactor.run()