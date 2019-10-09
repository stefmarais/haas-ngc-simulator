import telnetlib
import time

tn = telnetlib.Telnet('192.168.137.226', 5051)
#tn.write(b"Client")
time.sleep(1)

for i in range(5):
    print("Now writing ?Q102")
    tn.write(b"?Q102\n")
    status = tn.read_until(b"\n",timeout=1).decode("utf-8") 
    print(f"Data received: {status}")
    print("Now writing ?Q104")
    tn.write(b"?Q104\n")
    status2 = tn.read_until(b"\n",timeout=1).decode("utf-8") 
    print(f"Data received: {status2}")
    print("Now writing ?Q200")
    tn.write(b"?Q200\n")
    status2 = tn.read_until(b"\n",timeout=1).decode("utf-8") 
    print(f"Data received: {status2}")
    print("Now writing ?Q500")
    tn.write(b"?Q500\n")
    status2 = tn.read_until(b"\n",timeout=1).decode("utf-8") 
    print(f"Data received: {status2}")
tn.close()
