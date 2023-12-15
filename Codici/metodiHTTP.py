import requests                                                  #Importa la libreria per effettuare richieste HTTP

def controlla_verbi_http(url):        				 #Definisce una funzione che accetta un parametro 'url'.
    verbi_http = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH', 'CONNECT']     #Crea una lista che contenente i principali verbi HTTP.
    verbi_abilitati = []       					 #Inizializza una lista vuota di verbi che verrÃ  utilizzata
                             				         #per memorizzare i verbi HTTP supportati dall'URL.

    for verbo in verbi_http:    				 #Entra in un ciclo for che itera attraverso ogni verbo
                                 			 	 #HTTP nella lista verbi_http.
        try:
            response = requests.request(verbo, url)   		 #All'interno del ciclo, prova a effettuare una richiesta HTTP usando il verbo corrente e l'URL fornito.
            if response.status_code < 400:  			 #Se lo status code inferiore a 400), aggiunge il verbo alla  lista
                                             			 #verbi_abilitati e stampa il verbo HTTP e il relativo status code.
                verbi_abilitati.append(verbo)
            print(f"Verbo HTTP: {verbo}")
            print(f"Status code: {response.status_code}\n")
        except requests.exceptions.RequestException as e:   	 #Se si verifica un'eccezione durante la richiesta
            print(f"Errore durante {verbo}: {e}")           	 #viene stampato un messaggio di errore.

    print(f"I verbi HTTP abilitati per {url} sono: {verbi_abilitati}")  #Viene stampata la lista dei verbi HTTP abilitati per un percorso specifico.

path = input("\nInserisci URL: ")				 #Richiede all'utente di inserire un URL tramite input.

verbi_HTTP_abilitati = (path)
controlla_verbi_http(path)
