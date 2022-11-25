#By W3bParser

# --- Import the modules ---
import socket
from pystyle import *
import time
import threading

# --- Define the main function ---
from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

# --- Define the target input ---
System.Clear()
target = input(Col.white + '[' + Col.yellow + '!' + Col.white + '] Enter the host to be scanned (type "localhost" for a local scan.)\n$> ')
t_IP = socket.gethostbyname(target)
print (Col.white + '[' + Col.green + '!' + Col.white + '] Starting scan on host: ', t_IP)

# --- Define the port scanning ---
def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'OPEN')
      con.close()
   except:
      pass

# --- Define the thread ---
def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()

# --- Define the threading range ---
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()

# --- Define the scan range ---
for worker in range(1, 10000):
   q.put(worker)

# --- Print the scan results and the time that it's taked ---
q.join()
print(Col.white + '[' + Col.yellow + '!' + Col.white + '] Time taken:', time.time() - startTime)

#1337
