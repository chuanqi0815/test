#!/usr/bin/env php  
<?php  
$GLOBALS['THRIFT_ROOT'] = '/usr/lib/php';  
  
require_once $GLOBALS['THRIFT_ROOT'].'/Thrift.php';  
require_once $GLOBALS['THRIFT_ROOT'].'/protocol/TBinaryProtocol.php';  
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TSocket.php';  
require_once $GLOBALS['THRIFT_ROOT'].'/transport/THttpClient.php';  
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TBufferedTransport.php';  
  
require_once './gen-php/hello/UserManager.php';  
  
try {  
    $socket = new TSocket('localhost', 9090);  
    $transport = new TBufferedTransport($socket, 1024, 1024);  
    $protocol = new TBinaryProtocol($transport);  
    $client = new UserManagerClient($protocol);  
  
    $transport->open();  
    $client->ping();  
    printf("%s\n", $client->get_user('World', 'Hello'));  
  
} catch (UserException $e) {  
    echo $e->error_msg;  
}  
