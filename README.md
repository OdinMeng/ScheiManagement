# ScheiManagement 
### schèi (o sghèi) s. m. pl. [prob. tratto dall’espressione ted. Schei(demünze) «moneta divisionale» che si leggeva sulle monete austriache circolanti nel Lombardo-Veneto]. – Soldi, denaro, quattrini: essere senza schei; e dove li troviamo gli schei?; è voce veneta, ma nota anche altrove, usata per lo più in frasi di tono scherzoso

- **Obiettivo**: Progettare applicazione per gestire i "schei" (cit.) in debiti all'interno di un gruppo di persone. Per esempio, durante una serata la persona X decide di pagare la cena da €50 per tutti, creando un certo debito N a ognuno dei personaggi. L'applicazione è in grado di gestire questi debiti con le seguenti funzionalità: 
	1. Aggiungere/rimuovere debiti
	2. Ottimizzare debiti (*Esempio*: la persona X deve €20 a Y, che a sua volta deve €18 a X. Per "ottimizzazione" si intende il processo in cui si confrontano i debiti di X e Y e si sottrae il debito minore a entrambi i debiti. In questo caso, si sottrae €18 a entrambi: ora X deve solamente €2 a Y, e Y non deve più nulla a X.)
	3. Creare una rappresentazione grafica relativa ai dati totali.
- **Funzionamento**: Interfaccia CLI che è in grado di interagire con una molteplicità di cartelle, i quali a loro volta contengono persone (rappresentate in file .JSON) con i loro dati.
- **Prospettive future**: Applicazione semplice sviluppata sia per uso personale che per esercizio. Ergo, non avrà particolari prospettive.
- **Project Status**: Appena iniziato. Un po' di pazienza, insomma...