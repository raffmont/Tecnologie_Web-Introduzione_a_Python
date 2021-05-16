# Tecnologie Web: Introduzione a Python

Repository lezione "Tecnologie_Web-Introduzione_a_Python"

https://docs.google.com/presentation/d/1-T7mfJTdL76qesNzaDpLZ8ScxrGUcljYKtFD2aUph14/edit?usp=sharing

Lezione introduttiva a Python 3.x focalizzata sull’uso del linguaggio nell’ambito delle tecnologie web.


* Destinatari: studenti iscritti a un Corso di Laurea triennale in Informatica.


* Insegnamento:
Tecnologie Web (tipicamente secondo o terzo anno, obbligatorio o a scelta).
Si considerano già trattati gli argomenti: “web come documento ipermediale”, paradigma Client/Server, HTTP, HTML, CSS, JavaScript, JQuery, Progressive Web App.
Si considerano già introdotti aspetti relativi allo sviluppo lato server.


* Tipologia: lezione frontale (in presenza, a distanza, o mista) con esempi esplicativi, materiale didattico online (Moodle, Github).
La lezione sarà supportata da una successiva attività laboratoriale con tutor.  


* Durata: 45 minuti.


* Altri ambiti (riferito all’introduzione a Python):
Introduzione agli algoritmi e alle strutture dati; strumento nell’ambito di corsi (tipicamente magistrali) di Cloud Computing o Distributed Computing; Internet of Things; corsi pratici di Data Science e Machine Learning (anche in un contesto digital humanities); introduzione alla programmazione per corsi di studio STEM orientati alle scienze computazionali.

# Organizzazione didattica

* La lezione è organizzata idealmente in 3 parti.


* Parte prima: Introduzione (10 minuti)
Breve riassunto degli argomenti già coperti dal corso in modo da contestualizzare quanto verrà esposto nel resto della lezione.
Si richiama l’architettura di un’applicazione web progettata secondo i criteri attualmente considerati canonici e si presenta il Python come linguaggio scelto per lo scripting lato server.


* Parte seconda: Il linguaggio  (25 minuti)
È introdotto il linguaggio Python come tale e senza riferimenti espliciti alle tecnologie web.
Sono fatti frequenti confronti con il C, di cui si assume l’audience abbia comprensione, in modo da evidenziare similitudini e differenze.


* Parte terza: Il microframework Flask  (10 minuti)
Si mostra come realizzare una API minimale con quanto appreso nella parte precedente della lezione.
Gli argomenti presentati in questa terza parte saranno approfonditi in lezioni successive in cui Python sarà considerato strumento e non argomento di studio. 

# Installazione materiale didattico

* Clonare il repository
```console
git clone https://github.com/raffmont/Tecnologie_Web-Introduzione_a_Python.git
```

* Cambiare la directory corrente in quella del repository
```console
cd Tecnologie_Web-Introduzione_a_Python
```

* Creae un ambiente virtuale con Python3
```console
python3 -m venv venv
```

* Attivare l'ambiente virtuale
```console
. venv/bin/activate
```

* Aggiornare pip
```console
pip install --upgrade pip
```

* Installare le dipendenze
```console
pip install -r requirements.txt
```

# Web API Codice Fiscale

Questa semplice applicazione è l'esmepio finale mostrato a lezione.
```console
cd 06-flask-microframework
export FLASK_APP=flask_3.py
export FLASK_ENV=debug
flask run -h 0.0.0.0 -p 5000
```

Invocare il servizio web tramite curl.
```console
curl --data "surname=montella&name=raffaele&sex=M&birthdate=10/05/1972&birthplace=Napoli" http://localhost:5000/italian-fiscal-code
```
