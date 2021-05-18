import os

try:
    archivo = open("config.txt", "r+")
    linea = archivo.readline()
    lineaIP = linea[5:len(linea)]
    archivo.close()
    print(linea)
    os.system('ssh pi@' + lineaIP)

except:
    ip = input("Ip: ")
    archivo = open("config.txt", "w")
    archivo.write("ip = " + ip)
    archivo.close()
    os.system('ssh pi@' + ip)