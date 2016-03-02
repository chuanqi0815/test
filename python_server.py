#!/usr/bin/env python  
  
import sys  
sys.path.append('./gen-py')  
  
from hello import UserManager  
from hello.ttypes import *  
  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
  
from daemon import runner  
  
class UserManagerHandler:  
    def __init__(self):  
        pass  
  
    def ping(self):  
        print 'Welcome To Thrift...'  
  
    def get_user(self, firstname, lastname):  
        if firstname == '':  
            raise UserException(1, 'firstname is empty')  
        if lastname == '':  
            raise UserException(2, 'lastname is empty')  
        return lastname+' '+firstname+'!'  
  
class App:  
    def __init__(self):  
        self.stdin_path = '/dev/null'  
        self.stdout_path = '/dev/null'  
        self.stderr_path = '/dev/tty'  
        self.pidfile_path = '/tmp/tmp123456.pid'  
        self.pidfile_timeout = 5  
      
    def run(self):  
        handler = UserManagerHandler()  
        processor = UserManager.Processor(handler)  
        transport = TSocket.TServerSocket(port=9090)  
        tfactory = TTransport.TBufferedTransportFactory()  
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()  
        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)  
        print 'Starting the server...'  
        server.serve()  
                  
app = App()  
daemon_runner = runner.DaemonRunner(app)  
daemon_runner.do_action()  
