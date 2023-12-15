import socket
#IMPORTA IL MODULO SOCKET che fornisce una libreria di funzioni per la creazione e l'utilizzo di socket

target = input("Inserire un indirizzo IP da scansionare: ")
#Richiede all’utente di inserire l’indirizzo IP del server da scansionare

portrange = input("Inserire un intervallo di porte da scansionare(es 5-200): ") 9-600
#Richiede all'utente di inserire l'intervallo di porte da scansionare. L'intervallo di porte viene inserito come stringa, ma viene convertito in numeri interi prima di essere utilizzato

lowport = int(portrange.split('-')[0]) 
#Assegna il valore del primo numero dell'intervallo di porte alla variabile lowport

highport = int(portrange.split('-')[1])
#Assegna il valore del secondo numero dell'intervallo di porte alla variabile highport
print("\nScannerizzando le porte dalla " , lowport," alla" , highport, " del server con IP " , target)
#Stampa un messaggio a schermo che indica che la scansione delle porte sta per iniziare

for port in range (lowport, highport+1): 
#Inizia un ciclo for che esegue la scansione di tutte le porte nell'intervallo specificato

	s = socket.socket (socket.AF_INET, socket.SOCK_STREAM) 
#CREA UN NUOVO SOCKET TCP

	status = s.connect_ex ((target, port)) 
#Tenta di connettersi al server sull'indirizzo IP e sulla porta specificati

	if (status == 0):
#Verifica se la connessione è riuscita. Se è riuscita, il valore di status è 0

		print("\nPorta", port, "-APERTA") 
#Stampa a schermo un messaggio che indica che la porta è aperta

s.close()
#CHIUDE IL SOCKET
