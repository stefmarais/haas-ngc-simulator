# Haas NGC Simulator

Basic simulator of the Haas NGC machine data collection protocol.

## The Protocol

The Haas NGC controllers use a TCP server to communicate over networks. The NGC controller accepts queries in the format: ?Q### where ### is the query number.

The controller responds with a message starting with > and ending with \r\n

More detailed information about Haas NGC protocol can be found <a href='https://www.haascnc.com/service/troubleshooting-and-how-to/how-to/machine-data-collection---ngc.html'>here</a>


## The Simulator

The simulator can be used to test data monitoring applications. The simple_server creates a socket that listens on port 5051, the default port for NGC protocol. The simple_server responds to queries with the example query response as per the <a href='https://www.haascnc.com/service/troubleshooting-and-how-to/how-to/machine-data-collection---ngc.html'>machine data collection document</a>

## Usage 

Run the simple_server python script then, from a different terminal, run 
'''
telnet [ip] 5051
'''
Once connected, query at will.
'''
?Q100\n
>SERIAL NUMBER, 1234567
?Q200
>TOOL CHANGES, 35
'''

The simple_client interacts with the simple_server by using Telnetlib and opening a Telnet session to interact with the server.


