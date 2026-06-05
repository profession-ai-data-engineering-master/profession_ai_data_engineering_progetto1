#!/usr/bin/env python
# coding: utf-8

# =====================================================================
# FILE AUTO-GENERATO - NON MODIFICARE A MANO
# Export leggibile (via `jupyter nbconvert --to script`) del prototipo
# proto/programmazione-con-python-progetto1.ipynb.
# Serve come riferimento testuale del codice durante la migrazione in
# src/ (milestone M1). La fonte di verita' resta il notebook.
# Rigenerare con:
#   python -m nbconvert --to script \
#     proto/programmazione-con-python-progetto1.ipynb --output _notebook_readable
# =====================================================================

# # Gestore delle Spese Domestiche
# ## Contesto del Progetto
# In un'epoca in cui il controllo delle spese personali e familiari è diventato cruciale per una gestione finanziaria sostenibile, un'applicazione semplice ma efficace può rappresentare un importante valore aggiunto per i consumatori. Il progetto di un gestore delle spese domestiche mira a fornire uno strumento utile e immediato per il monitoraggio delle transazioni economiche quotidiane, con un'interfaccia utente chiara e funzionale.
# 
# ## Obiettivo del Progetto
# L'obiettivo è sviluppare un'applicazione in Python che consenta agli utenti di tracciare le loro spese, generare report mensili e identificare le spese più significative. Questo strumento fornirà una panoramica finanziaria trasparente, aiutando gli utenti a prendere decisioni consapevoli per migliorare la gestione del budget familiare.
# 
# ### **Funzionalità Chiave**
# 1. **Aggiunta di una transazione**: Gli utenti possono registrare facilmente ogni spesa, completando campi come data, descrizione e importo.
# 2. **Report Mensile**: Generazione di un resoconto mensile che raggruppa le spese per anno e mese, fornendo una chiara visione delle transazioni effettuate nel periodo.
# 3. **Top 10 Transazioni**: Visualizzazione delle 10 spese più importanti, utile per monitorare le voci di spesa più rilevanti.
# 
# ## Valore Aggiunto
# L'applicazione offre diversi benefici agli utenti:
# - **Monitoraggio immediato**: Ogni transazione viene registrata in un file CSV, consentendo di tenere traccia in tempo reale delle spese quotidiane.
# - **Gestione consapevole del budget**: Il report mensile fornisce una visione aggregata delle spese, aiutando l'utente a comprendere meglio come e dove vengono spesi i propri soldi.
# - **Identificazione delle spese principali**: La funzione "Top 10" consente di individuare velocemente le spese di maggior impatto economico, favorendo il risparmio e una gestione più oculata delle finanze personali.
# 
# ## Descrizione delle Funzionalità
# ### **Menu delle Operazioni**
# L'applicazione presenta un menu interattivo che offre all'utente tre opzioni principali:
# - [1] **Aggiungi una transazione**: L'utente può registrare una nuova spesa fornendo data, descrizione e importo. I dati vengono salvati in un file CSV, che funge da registro delle spese.
# - [2] **Report Mensile**: Questa opzione genera un resoconto totale delle transazioni, raggruppate per anno e mese, permettendo all'utente di avere un quadro complessivo delle spese nel corso del tempo.
# - [3] **Top 10 Transazioni**: L'utente può visualizzare le dieci spese più alte, ordinate per importo, ottenendo così informazioni utili su quali siano state le transazioni di maggior impatto economico.
# 
# ### **Dettaglio delle Operazioni**
# 1. **Aggiunta di una Transazione**:
#   - L'utente inserisce la data della transazione (formato GG/MM/AAAA), una breve descrizione e l'importo totale.
#   - Il dato immesso (es. "18/05/2024 Cena al ristorante 45") viene salvato in un file CSV e l'applicazione ritorna al menu principale.
# 
# 2. **Generazione del Report Mensile**:
# - L'utente seleziona questa opzione per visualizzare un riepilogo delle spese suddivise per anno e mese.
# - Il report viene visualizzato nel seguente formato:
#   2024-05 324
#   2024-05 123
#   2024-06 834
# - Questo fornisce una visione chiara delle spese nel tempo, agevolando il monitoraggio dei flussi di cassa mensili.
# 
# 3. **Top 10 Transazioni**:
# - L'applicazione visualizza le dieci transazioni con l'importo più elevato, includendo data, descrizione e importo. Ad esempio:
#   18/06/2023 Rata mutuo 1231
#   15/02/2021 Acquisto scooter 4323
# - Questa funzionalità aiuta l'utente a identificare le spese maggiori e a monitorare potenziali aree di risparmio.
# 
# ## Implementazione Tecnica
# L'applicazione sarà realizzata utilizzando Python e i dati saranno gestiti attraverso l'uso di file CSV, garantendo leggerezza e semplicità di utilizzo. La gestione delle operazioni avverrà tramite un menu interattivo che guiderà l'utente attraverso le varie opzioni.
# 
# ### **Commenti e Documentazione**
# Il codice Python sarà ampiamente documentato, con commenti chiari che descrivono ogni blocco funzionale. Questo garantirà che sia facile da mantenere e migliorare nel tempo, in linea con gli standard di programmazione appresi durante il corso.
# 
# Conclusione
# L'applicazione di gestione delle spese domestiche offre una soluzione semplice ma potente per il monitoraggio finanziario. Fornirà agli utenti gli strumenti per una gestione più consapevole delle spese e delle entrate, favorendo la trasparenza e l'efficienza nella pianificazione del budget personale o familiare.

# --- 

# # Pianificazione e Scelte Progettuali
# ## Premessa
# Per approcciarmi all'implementazione richiesta ho deciso di orientarmi ad un adattamento della metodologia DDD (Domain Driven Design). Per questo specifico progetto tale metodologia può risultare
# overkill ma cercherò di aderirvi il più possibile per ottenere un codice chiaro e ben strutturato nel pieno rispetto dei principi SOLID.
# ## Prototipazione
# In base a quanto visto nel corso e alle condizioni poste per la consegna del progetto mi limiterò a strutturare un prototipo dell'applicativo in un notebook jupyter. Salverò questo prototipo nella cartella `proto` e cercherò di strutturarlo nelle sue parti in maniera modulare, in modo da poterlo dividerlo in più file facilmente in futuro.
# Per fare ciò indicherò all'inizio di ogni blocco di codice la cartella dove lo andrei a collocare una volta finita la fase di prototipazione, aggiungendo l'informazione in questo formato `# @title cartelle/file.py`.
# ## Test Unitari
# Per garantire la qualità del codice scriverò per ogni modulo/classe del progetto i suoi test unitari, per assicurare qualità del codice ed evitare errori.
# 
# per fare ciò ho trovato questo spunto su Stack overflow per eseguire test unitari all'interno di jupyter [link](https://stackoverflow.com/questions/40172281/unit-tests-for-functions-in-a-jupyter-notebook),
# di seguito uno snippet del codice che userò:
# 
# ``` python
#     # This executes the unit test/(itself)
#     import sys
# 	import unittest
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestAgent)
#     unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)
# ```
# 
# ## Versione Python
# Per questo progetto verrà utilizzata la versione Python 3.12.9
# 
# ## TL;DR
# - Essendo che python non possiede interfacce ma classi astratte, utilizzerò la dicitura `Abstract` per indicare le classi astratte che userò per massimizzare l'astrazione del mio codice.
# - Per le docstring utilizzerò lo standard `reStructuredText` per futura compatibilità con strumenti di produzione automatica di documentazione come **Sphinx**. Come esempio utilizzerò questa struttura 
#   poposta online [link](https://stackoverflow.com/questions/71249750/utilizing-sphinx-with-restructuredtext-formatted-docstrings):
# 
# > ``` python
# > py:function:: send_message(sender, recipient, message_body, [priority=1])
# >    """
# >    Send a message to a recipient
# > 
# >    :param str sender: The person sending the message
# >    :param str recipient: The recipient of the message
# >    :param str message_body: The body of the message
# >    :param priority: The priority of the message, can be a number 1-5
# >    :type priority: integer or None
# >    :return: the message id
# >    :rtype: int
# >    :raises ValueError: if the message_body exceeds 160 characters
# >    :raises TypeError: if the message_body is not a basestring
# >    """
# > ```
# 
# - Per l'indentazione userò 4 spazi come da standard **PEP 8**.

# In[ ]:


# @title Notebook utilities
# Ho trasformato lo snippet trovato online in una funzione per evitare di ripetere lo stesso codice (DRY)
import unittest
from typing import Type

def esegui_tests(test: Type[unittest.TestCase], verbosity: int = 4, stream: ipykernel.iostream.OutStream=sys.stderr):
    """
    Funzione di utility del notebook per eseguire tutti i test presenti in una Classe di test
    
    :param Type[unittest.TestCase] sender: Classe di test da eseguire (non un'istanza!)
    :param int verbosity: Livello di verbosità del risultato
    :param ipykernel.iostream.OutStream stream: flusso su cui stampare
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(test)
    return unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)


# # src/domain/entities/
# Cartella del progetto che conterrà classi che rappresenteranno le entità del nostro **Dominio**. Queste entità conterranno le regole di business della nostra applicazione.

# In[53]:


# @title src/domain/entities/abstract_spesa.py

from abc import ABC,abstractmethod
from datetime import datetime

class AbstractSpesa(ABC):
    """
    Classe astratta che definirà i metodi che dovra necessariamente implementare un oggetto di tipo spesa
    """
    @property
    @abstractmethod
    def data(self)->datetime:
        """
        ritorna la data della spesa
        
        :return: data della spesa
        :rtype: datetime
        """
        pass
    
    @data.setter
    @abstractmethod
    def data(self,data:datetime)->None:
        """
        setta la data della spesa
        
        :param datetime data: nuova data della spesa
        """
        pass
    
    @property
    @abstractmethod
    def descrizione(self)->str:
        """
        ritorna la descrizione della spesa
        
        :return: descrizione della spesa
        :rtype: str
        """
        pass
    
    @descrizione.setter
    @abstractmethod
    def descrizione(self,descrizione:str)->None:
        """
        setta la descrizione della spesa
        
        :param str descrizione: nuova descrizione della spesa
        """
        pass
    
    @property
    @abstractmethod
    def importo(self)->float:
        """
        ritorna l'importo della spesa
        
        :return: importo della spesa
        :rtype: float
        """
        pass
    
    @importo.setter
    @abstractmethod
    def importo(self,importo:float)->None:
        """
        setta l'importo della spesa
        
        :param float importo: nuovo importo della spesa
        """
        pass
    
    @abstractmethod
    def __repr__(self)->str:
        """
        definisce la rappresentazione human readable delle istanze di spesa
        
        :return: rappresentazione human readable delle istanze di spesa
        :rtype: str
        """
        pass
    
    @abstractmethod
    def __eq__(self,other)->bool:
        """
        definisce come stabilire l'uguaglianza di due istanze di spesa
        
        :return: True se uguali, se no False
        :rtype: bool
        """
        pass
        
    
    

# In[54]:



# @title src/domain/entities/spesa.py
from datetime import datetime
class Spesa(AbstractSpesa):
    
    """
    Rappresenta un entità di tipo Spesa che implementa il contratto AbstractSpesa.
    """
    
    def __init__(self, data:datetime, descrizione:str, importo:float):
        self.data = data
        self.descrizione = descrizione
        self.importo = importo
        
    @property
    def data(self)->datetime:
        """
        ritorna la data della spesa
        
        :return: data della spesa
        :rtype: datetime
        """
        return self._data
    
    @data.setter
    def data(self,data:datetime)->None:
        """
        setta la data della spesa
        
        :param datetime data: nuova data della spesa
        :raises TypeError: se la data è None o non è di tipo datetime
        """
        if(data is None or not isinstance(data,datetime)):
            raise TypeError("La data deve essere di tipo datetime e non può essere None")
        self._data = data
    
    @property
    def descrizione(self)->str:
        """
        ritorna la descrizione della spesa
        
        :return: descrizione della spesa
        :rtype: str
        """
        return self._descrizione
    
    @descrizione.setter
    def descrizione(self,descrizione:str)->None:
        """
        setta la descrizione della spesa
        
        :param str descrizione: nuova descrizione della spesa
        :raises TypeError: se la descrizione non è di tipo str
        :raises ValueError: se la descrizione ha meno di 3 caratteri che non siano spazi
        """
        if(descrizione is None or not isinstance(descrizione,str)):
            raise TypeError("La descrizione essere di tipo str")
        if(len(descrizione.strip()) < 3 ):
            raise ValueError("La descrizione deve avere minimo 3 caratteri che non siano spazi")
        self._descrizione = descrizione
    
    @property
    def importo(self)->float:
        """
        ritorna l'importo della spesa
        
        :return: importo della spesa
        :rtype: float
        
        """
        return self._importo
    
    @importo.setter
    def importo(self,importo:float)->None:
        """
        setta l'importo della spesa
        
        :param float importo: nuovo importo della spesa
        :raises TypeError: se l'importo non è di tipo numerico
        :raises ValueError: se l'importo è minore o uguale a 0
        """
        if(importo is None or not isinstance(importo,(int,float))):
            raise TypeError("L'importo deve essere di tipo numerico")
        if(importo <= 0 ):
            raise ValueError("L'importo deve essere maggiore di 0")
        self._importo = float(importo)
    
    def __repr__(self)->str:
        """definisce la rappresentazione tecnica delle istanze di spesa"""
        return f"Spesa(data={self.data},descrizione='{self.descrizione}',importo={self.importo})"
    
    def __str__(self)->str:
        """definisce la rappresentazione human readable delle istanze di spesa"""
        return f"Data: {datetime.strftime(self._data, '%d/%m/%Y')}, Descrizione: '{self.descrizione}', Importo: {self.importo}"
    
    def __eq__(self,other)->bool:
        """
        definisce come stabilire l'uguaglianza di due istanze di spesa
        
        :return: True se uguali, se no False
        :rtype: bool
        """
        return self.data == other.data and self.descrizione== other.descrizione and self.importo == other.importo
    

# In[55]:


import unittest
from datetime import datetime
import sys

class TestSpesa(unittest.TestCase):
    
    def setUp(self):
        self._data = datetime(2025,5,1)
        self._descrizione = 'spesa di test'
        self._importo = 30.41
        self._spesa = Spesa(self._data, self._descrizione, self._importo)
        
    def test_costruttore(self):
        """Verifica che il costruttore funzioni correttamente"""
        self.assertEqual(self._spesa.data,self._data)
        self.assertEqual(self._spesa.descrizione,self._descrizione)
        self.assertEqual(self._spesa.importo,self._importo)
    
    def test_setter_data(self):
        """Verifica che la data venga impostata correttamente"""
        new_data = datetime(2025,5,7)
        self._spesa.data = new_data
        self.assertEqual(self._spesa.data,new_data)
        with self.assertRaises(TypeError):
            new_data = 0.0
            self._spesa.data = new_data
        with self.assertRaises(TypeError):
            new_data = None
            self._spesa.data = new_data
        with self.assertRaises(TypeError):
            new_data = 'ciao'
            self._spesa.data = new_data
    
    def test_setter_descrizione(self):
        """Verifica che la descrizione venga impostata correttamente"""
        new_descrizione = 'nuova spesa di test'
        self._spesa.descrizione = new_descrizione
        self.assertEqual(self._spesa.descrizione,new_descrizione)
        with self.assertRaises(ValueError):
            new_descrizione = ''
            self._spesa.descrizione = new_descrizione
        with self.assertRaises(ValueError):
            new_descrizione = 'ab'
            self._spesa.descrizione = new_descrizione
        with self.assertRaises(TypeError):
            new_descrizione = None
            self._spesa.descrizione = new_descrizione
        with self.assertRaises(TypeError):
            new_descrizione = 5050
            self._spesa.descrizione = new_descrizione
            
    
    def test_setter_importo(self):
        """Verifica che l'importo venga impostato correttamente"""
        new_importo = 99.99
        self._spesa.importo = new_importo
        self.assertEqual(self._spesa.importo,new_importo)
        with self.assertRaises(ValueError):
            new_importo = -1.0
            self._spesa.importo = new_importo
        with self.assertRaises(ValueError):
            new_importo = 0.0
            self._spesa.importo = new_importo
        with self.assertRaises(TypeError):
            new_importo = None
            self._spesa.importo = new_importo
        with self.assertRaises(TypeError):
            new_importo = 'ciao'
            self._spesa.importo = new_importo   
        
    
    def test_repr(self):
        """Verifica che repr restituisca la rappresentazione corretta"""
        expected = f"Spesa(data={self._data},descrizione='{self._descrizione}',importo={self._importo})"
        self.assertEqual(repr(self._spesa),expected)
        
    def test_str(self):
        """Verifica che str restituisca la rappresentazione corretta"""
        expected = f"Data: {datetime.strftime(self._data, '%d/%m/%Y')}, Descrizione: '{self._descrizione}', Importo: {self._importo}"
        self.assertEqual(str(self._spesa),expected)
    
    def test_eq_uguali(self):
        """Verifica che eq restituisca true quando uguali"""
        data = datetime(2025,5,1)
        descrizione = 'spesa di test'
        importo = 30.41
        spesa1 = Spesa(data, descrizione, importo)
        spesa2 = Spesa(data, descrizione, importo)
        self.assertEqual(spesa1,spesa2)
        
    def test_eq_diversa_data(self):
        """Verifica che eq restituisca true quando diversa data"""
        data1 = datetime(2025,5,1)
        data2 = datetime(2024,5,1)
        descrizione = 'spesa di test'
        importo = 30.41
        spesa1 = Spesa(data1, descrizione, importo)
        spesa2 = Spesa(data2, descrizione, importo)
        self.assertNotEqual(spesa1,spesa2)
        
    def test_eq_diversa_descrizione(self):
        """Verifica che eq restituisca true quando diversa descrizione"""
        data = datetime(2025,5,1)
        descrizione1 = 'spesa di test1'
        descrizione2 = 'spesa di test2'
        importo = 30.41
        spesa1 = Spesa(data, descrizione1, importo)
        spesa2 = Spesa(data, descrizione2, importo)
        self.assertNotEqual(spesa1,spesa2)
        
    def test_eq_diverso_importo(self):
        """Verifica che eq restituisca true quando diverso importo"""
        data = datetime(2025,5,1)
        descrizione = 'spesa di test'
        importo1 = 30.41
        importo2 = 96.94
        spesa1 = Spesa(data, descrizione, importo1)
        spesa2 = Spesa(data, descrizione, importo2)
        self.assertNotEqual(spesa1,spesa2)

esegui_tests(TestSpesa)

# # src/domain/repositories
# Contiene i contratti astratti dei repository

# In[56]:


# @title src/domain/repositories/abstract_spesa_repository.py
from abc import ABC,abstractmethod

class AbstractSpesaRepository(ABC):
    """
    Classe astratta che definirà i metodi che dovra necessariamente implementare un oggetto di tipo SpesaRepository
    """
    
    @abstractmethod
    def aggiungi_spesa(self,spesa:AbstractSpesa)->None:
        """
        Permette di aggiungere una nuova spesa al repository
        
        :param str descrizione: nuova spesa da aggiungere
        """
        pass
    
    @abstractmethod
    def ottieni_tutte_le_spese(self)->list[AbstractSpesa]:
        """
        Permette di ottenere la lista di tutte le spese presenti nel repository
        
        :return: tutte le spese presenti nel repository
        :rtype: list[AbstractSpesa]
        """
        pass

# # src/infrastructure/persistence/datasources/
# Contiene classi e contratti che stabiliranno le regole e i modi che consentiranno di accedere con le medesime modalità a differenti sorgenti dati ( in questo caso solo csv ma volendo è facilmente estensibile ).

# In[57]:


# @title src/infrastructure/persistence/datasources/abstract_spesa_datasource.p
from abc import ABC,abstractmethod

class AbstractSpesaDataSource(ABC):
    """
    Classe astratta che definirà i metodi che dovra necessariamente implementare un oggetto con respontabilità da Datasource
    """
    
    @abstractmethod
    def aggiungi_spesa(self,spesa:AbstractSpesa)->None:
        """
        Permette di aggiungere una nuova spesa alla sorgente dati
        
        :param str descrizione: nuova spesa da aggiungere
        """
        pass
    
    @abstractmethod
    def ottieni_tutte_le_spese(self)->list[AbstractSpesa]:
        """
        Permette di ottenere la lista di tutte le spese presenti nella sorgente dati
        
        :return: tutte le spese presenti nella sorgente dati
        :rtype: list[AbstractSpesa]
        """
        pass

# In[58]:


# @title src/infrastructure/persistence/datasources/spesa_datasource_csv.py
from os import path
import datetime
import csv
class SpesaDataSourceCsv(AbstractSpesaDataSource):
    """
    Classe responsabile dell'interazione con la sorgente dati csv
    """
    def __init__(self):
        self._filepath = path.join('storico_spese.csv')
    
    def _verifica_inizializzazione_sorgente(self)->bool:
        """
        Verifica l'esistenza e la corretta inizializzazione della sorgente dati csv
        
        :return: True se la sorgente esiste ed è inizializzata, se no False
        :rtype: bool
        """
        return path.exists(self._filepath) and path.getsize(self._filepath) > 0
    
    def _inizializza_sorgente(self)->None:
        """Inizializza la sorgente dati creando il file con l'header opportuno"""
        with open(self._filepath,"w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["data","descrizione","importo"])
        
        
    def aggiungi_spesa(self,spesa:AbstractSpesa)->None:
        """
        Permette di aggiungere una nuova spesa alla sorgente dati
        
        :param str descrizione: nuova spesa da aggiungere
        """
        if not self._verifica_inizializzazione_sorgente():
            self._inizializza_sorgente()
        with open(self._filepath,"a",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([spesa.data,spesa.descrizione,spesa.importo])
    
    def ottieni_tutte_le_spese(self)->list[AbstractSpesa]:
        """
        Permette di ottenere la lista di tutte le spese presenti nella sorgente dati
        
        :return: tutte le spese presenti nella sorgente dati
        :rtype: list[AbstractSpesa]
        """
        result: list[AbstractSpesa] = []
        if not self._verifica_inizializzazione_sorgente():
            return result
        with open(self._filepath,"r",newline="",encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader,None) #salto l'intestazione
            for riga in reader:
                result.append(Spesa(datetime.strptime(riga[0],'%Y-%m-%d %H:%M:%S'),riga[1],float(riga[2])))
        return result

# In[59]:


# @title test/infrastructure/persistence/datasources/test_spesa_datasource_csv.py

import unittest
import datetime
from datetime import datetime
from unittest.mock import patch, mock_open, MagicMock, call
import sys

class TestSpesaDataSourceCsv(unittest.TestCase):
    
    @patch("__main__.path.exists",return_value=False)
    def test__verifica_inizializzazione_sorgente_file_non_esiste(self,mock_exists):
        """Verifica che se il file non esiste la funzione deve tornare False"""
        ds = SpesaDataSourceCsv()
        result = ds._verifica_inizializzazione_sorgente()
        self.assertFalse(result)
        
        
    @patch("__main__.path.exists",return_value=True)
    @patch("__main__.path.getsize",return_value=0)
    def test__verifica_inizializzazione_sorgente_file_vuoto(self,mock_exists,mock_getsize):
        """Verifica che se il file è vuoto la funzione deve tornare False"""
        ds = SpesaDataSourceCsv()
        result = ds._verifica_inizializzazione_sorgente()
        self.assertFalse(result)
        
        
    @patch("__main__.path.exists",return_value=True)
    @patch("__main__.path.getsize",return_value=1)
    def test__verifica_inizializzazione_sorgente_file_ok(self,mock_exists,mock_getsize):
        """Verifica che se il file esiste e non è vuoto la funzione deve tornare True"""
        ds = SpesaDataSourceCsv()
        result = ds._verifica_inizializzazione_sorgente()
        self.assertTrue(result)
        
        
    @patch("__main__.csv.writer")
    @patch("__main__.open", new_callable=mock_open)
    def test_inizializza_sorgente(self, mock_file, mock_csv_writer):
        """testa il corretto flusso di chiamate durante l'inizializzazione della sorgente"""
        ds = SpesaDataSourceCsv()
        # Simula l'istanza del writer che scrive sul file
        mock_writer_instance = MagicMock()
        mock_csv_writer.return_value = mock_writer_instance
        ds._inizializza_sorgente()
        # Verifica che open sia stato chiamato correttamente
        mock_file.assert_called_once_with(ds._filepath, "w", newline="", encoding="utf-8")
        # verifica che csv.writer sia stato invocato
        handle = mock_file()
        mock_csv_writer.assert_called_once_with(handle)
        # verifica che sia stata chiamata la funzione writerow per scrivere l'header
        mock_writer_instance.writerow.assert_called_once_with(["data","descrizione","importo"])
        
        
    @patch("__main__.csv.writer")
    @patch("__main__.open", new_callable=mock_open)
    def test_aggiungi_spesa_inizializzazione(self, mock_file, mock_csv_writer):
        """Verifica che in fase di aggiunta e in mancanza della sorgente, venga creata la sorgente e aggiunta la nuova spesa"""
        ds = SpesaDataSourceCsv()
        with patch.object(SpesaDataSourceCsv,"_verifica_inizializzazione_sorgente",return_value=False):
            spesa_mock = MagicMock()
            spesa_mock.data = datetime(2025,5,1)
            spesa_mock.descrizione = 'spesa di test'
            spesa_mock.importo = 30.41
            
            mock_writer_instance_init = MagicMock()
            mock_writer_instance_append = MagicMock()
            
            mock_csv_writer.side_effect = [mock_writer_instance_init, mock_writer_instance_append]
            
            ds.aggiungi_spesa(spesa_mock)
            
            mock_file.assert_has_calls([
                call('storico_spese.csv', 'w', newline='', encoding='utf-8'),
                call().__enter__(),
                call().__exit__(None, None, None),
                call('storico_spese.csv', 'a', newline='', encoding='utf-8'),
                call().__enter__(),
                call().__exit__(None, None, None)
                ],
                any_order = False,
            )
            
            handle = mock_file()
            mock_csv_writer.assert_has_calls([
                call(handle),
                call(handle)
                ],
                any_order = False,
            )
            
            mock_writer_instance_init.writerow.assert_called_once_with(["data","descrizione","importo"])
            mock_writer_instance_append.writerow.assert_called_once_with([spesa_mock.data,spesa_mock.descrizione,spesa_mock.importo])
        
    @patch("__main__.csv.writer")
    @patch("__main__.open", new_callable=mock_open)
    def test_aggiungi_spesa_solo_append(self, mock_file, mock_csv_writer):
        """Verifica che in fase di aggiunta e in presenza della sorgente, aggiunta la nuova spesa"""
        ds = SpesaDataSourceCsv()
        
        with patch.object(SpesaDataSourceCsv,"_verifica_inizializzazione_sorgente",return_value=True):
            spesa_mock = MagicMock(spec_set=AbstractSpesa)
            spesa_mock.data = datetime(2025,5,1)
            spesa_mock.descrizione = 'spesa di test'
            spesa_mock.importo = 30.41
            
            mock_writer_instance_append = MagicMock()
            
            mock_csv_writer.return_value = mock_writer_instance_append
            
            ds.aggiungi_spesa(spesa_mock)
            
            mock_file.assert_called_once_with('storico_spese.csv', 'a', newline='', encoding='utf-8')
            
            handle = mock_file()
            mock_csv_writer.assert_called_once_with(handle)
            
            mock_writer_instance_append.writerow.assert_called_once_with([spesa_mock.data,spesa_mock.descrizione,spesa_mock.importo])


    @patch("__main__.open", new_callable=mock_open)
    def test_ottieni_tutte_le_spese_file_mancante(self, mock_file):
        """Verifica che in fase di lettura e in mancanza della sorgente, la funzione restituisca una lista vuota"""
        ds = SpesaDataSourceCsv()
        with patch.object(SpesaDataSourceCsv,"_verifica_inizializzazione_sorgente",return_value=False):
            expected:list[AbstractSpesa] = []
            
            result = ds.ottieni_tutte_le_spese()
            
            self.assertEqual(result,expected)
      
    @patch("__main__.csv.reader")  
    @patch("__main__.open", new_callable=mock_open)
    def test_ottieni_tutte_le_spese_file_mancante(self, mock_file, mock_csv_reader):
        """Verifica che in fase di lettura e in presenza della sorgente, la funzione restituisca una lista delle Spese contenute nel file"""
        ds = SpesaDataSourceCsv()
        with patch.object(SpesaDataSourceCsv,"_verifica_inizializzazione_sorgente",return_value=True):
            intestazione_mock:list[str] = ["data","descrizione","importo"]
            spesa_mock1:list[str] = ["2025-05-01 00:00:00", 'spesa di test 1', "45.72"]
            spesa_mock2:list[str] = ["2025-06-01 00:00:00", 'spesa di test 2', "0.99"]
            
            expected:iter = iter([intestazione_mock,spesa_mock1,spesa_mock2])
            mock_csv_reader.return_value = expected
            
            
            result = ds.ottieni_tutte_le_spese()
            
            mock_file.assert_called_once_with('storico_spese.csv',"r",newline="",encoding="utf-8")
            
            handle = mock_file()
            mock_csv_reader.assert_called_once_with(handle)
            
            self.assertEqual(len(result),2)
            self.assertEqual(result[0], Spesa(datetime.strptime(spesa_mock1[0], '%Y-%m-%d %H:%M:%S'), spesa_mock1[1], float(spesa_mock1[2])))
            self.assertEqual(result[1], Spesa(datetime.strptime(spesa_mock2[0], '%Y-%m-%d %H:%M:%S'), spesa_mock2[1], float(spesa_mock2[2])))

esegui_tests(TestSpesaDataSourceCsv)

# # src/infrastructure/persistence/repositories/
# Contiene classi e contratti che saranno le repository relative alle entità presenti nel progetto. Il loro compito è fare da interfaccia tra le entità di dominio e i datasources. 

# In[60]:


# @title src/infrastructure/persistence/repositories/spesa_repository.py

class SpesaRepository(AbstractSpesaRepository):
    """
    È l'interfaccia tra le entità di tipo AbstractSpesa e quelle di tipo AbstractSpesaDataSource
    """
    def __init__(self, datasource:AbstractSpesaDataSource):
        self._datasource = datasource
    
    def aggiungi_spesa(self,spesa:AbstractSpesa)->None:
        """
        Permette di aggiungere una nuova spesa al repository
        
        :param str descrizione: nuova spesa da aggiungere
        """
        self._datasource.aggiungi_spesa(spesa)
    
    def ottieni_tutte_le_spese(self)->list[AbstractSpesa]:
        """
        Permette di ottenere la lista di tutte le spese presenti nel repository
        
        :return: tutte le spese presenti nel repository
        :rtype: list[AbstractSpesa]
        """
        return self._datasource.ottieni_tutte_le_spese()

# In[61]:


# @title tests/infrastructure/persistence/repositories/test_spesa_repository.py

import unittest
from unittest.mock import patch, mock_open, MagicMock, call
import sys

class TestSpesaRepository(unittest.TestCase):
    

    def setUp(self):
        self._datasource = MagicMock(spec_set=AbstractSpesaDataSource)
        self._repository = SpesaRepository(self._datasource)
        
    def test_aggiungi_spesa(self):
        """Verifica che il repository utilizzi propriamente il datasource quando viene aggiunta una spesa"""
        spesa_mock = MagicMock(spec_set=AbstractSpesa)
        spesa_mock.data = datetime(2025,5,1)
        spesa_mock.descrizione = 'spesa di test'
        spesa_mock.importo = 30.41
        
        self._repository.aggiungi_spesa(spesa_mock)
        
        self._repository._datasource.aggiungi_spesa.assert_called_once_with(spesa_mock)
        
    def test_ottieni_tutte_le_spese(self):
        """Verifica che il repository utilizzi propriamente il datasource quando viene aggiunta una spesa"""
        
        mock_spese = [MagicMock(spec_set=AbstractSpesa),MagicMock(spec_set=AbstractSpesa)]
        
        self._datasource.ottieni_tutte_le_spese.return_value = mock_spese
        
        
        result = self._repository.ottieni_tutte_le_spese()
        
        self._repository._datasource.ottieni_tutte_le_spese.assert_called_once_with()
        
        self.assertEqual(result,mock_spese)

esegui_tests(TestSpesaRepository)

# # src/domain/services
# Contiene i servizi che hanno lo scopo di gestire la logica di business che coinvolge più di un entità del modello

# In[62]:


# @title src/domain/services/AbstractSpesaService.py
# Può risultare overkill in questo caso ma creo comunque il servizio tenendo conto di possibili implementazioni future quindi getto questa base
# anche se con metodi banali
from abc import ABC,abstractmethod

class AbstractSpesaService(ABC):
    """
    Classe astratta che definirà i metodi che dovrà necessariamente implementare
    il servizio che si occupa di gestire la logica di business che coinvolge più 
    di un entità di tipo AbstractSpesa
    """
    
    @abstractmethod
    def aggiungi_spesa(self,spesa:AbstractSpesa)->None:
        """
        Permette di aggiungere una nuova spesa mediante accesso al repository
        
        :param str descrizione: nuova spesa da aggiungere
        """
        pass
    
    @abstractmethod
    def ottieni_tutte_le_spese(self)->list[AbstractSpesa]:
        """
        Permette di ottenere la lista di tutte le spese mediante accesso al repository
        
        :return: tutte le spese presenti nella sorgente dati
        :rtype: list[AbstractSpesa]
        """
        pass

# In[63]:


# @title src/domain/services/SpesaService.py

class SpesaService(AbstractSpesaService):
    """
    Servizio che definirà i metodi che dovrà necessariamente implementare
    il servizio che si occupa di gestire la logica di business che coinvolge più 
    di un entità di tipo AbstractSpesa
    """
    
    def __init__(self, repository:AbstractSpesaRepository):
        self._repository = repository
    
    def aggiungi_spesa(self,spesa:AbstractSpesa)->None:
        """
        Permette di aggiungere una nuova spesa mediante accesso al repository
        
        :param str descrizione: nuova spesa da aggiungere
        """
        self._repository.aggiungi_spesa(spesa)
    
    def ottieni_tutte_le_spese(self)->list[AbstractSpesa]:
        """
        Permette di ottenere la lista di tutte le spese mediante accesso al repository
        
        :return: tutte le spese presenti nella sorgente dati
        :rtype: list[AbstractSpesa]
        """
        return self._repository.ottieni_tutte_le_spese()

# In[64]:


# @title tests/domain/services/SpesaService.py

import unittest
from unittest.mock import patch, mock_open, MagicMock, call
import sys

class TestSpesaService(unittest.TestCase):
    

    def setUp(self):
        self._repository = MagicMock(spec_set=AbstractSpesaRepository)
        self._service = SpesaService(self._repository)
        
    def test_aggiungi_spesa(self):
        """Verifica che il service utilizzi propriamente il repository quando viene aggiunta una Spesa"""
        spesa_mock = MagicMock(spec_set=AbstractSpesa)
        spesa_mock.data = datetime(2025,12,1)
        spesa_mock.descrizione = 'spesa di test'
        spesa_mock.importo = 50.50
        
        self._service.aggiungi_spesa(spesa_mock)
        
        self._service._repository.aggiungi_spesa.assert_called_once_with(spesa_mock)
        
    def test_ottieni_tutte_le_spese(self):
        """Verifica che il service utilizzi propriamente il repository quando viene aggiunta una Spesa"""
        
        mock_spese = [MagicMock(spec_set=AbstractSpesa),MagicMock(spec_set=AbstractSpesa)]
        
        self._repository.ottieni_tutte_le_spese.return_value = mock_spese
        
        
        result = self._service.ottieni_tutte_le_spese()
        
        self._service._repository.ottieni_tutte_le_spese.assert_called_once_with()
        
        self.assertEqual(result,mock_spese)

esegui_tests(TestSpesaService)

# # src/application/dtos

# In[65]:



# @title src/application/dtos/abstract_report_mensile_dto.py

from abc import ABC,abstractmethod
from datetime import datetime

class AbstractReportMensileDto(ABC):
    """
    Classe astratta che definirà i metodi che dovra necessariamente implementare un oggetto di tipo ReportMensileDto
    """
    @property
    @abstractmethod
    def data(self)->datetime:
        """
        ritorna la data della ReportMensileDto
        
        :return: data della ReportMensileDto
        :rtype: datetime
        """
        pass
    
    @data.setter
    @abstractmethod
    def data(self,data:datetime)->None:
        """
        setta la data della ReportMensileDto
        
        :param datetime data: nuova data della ReportMensileDto
        """
        pass
    
    @property
    @abstractmethod
    def importo(self)->float:
        """
        ritorna l'importo della ReportMensileDto
        
        :return: importo della ReportMensileDto
        :rtype: float
        """
        pass
    
    @importo.setter
    @abstractmethod
    def importo(self,importo:float)->None:
        """
        setta l'importo della ReportMensileDto
        
        :param float importo: nuovo importo della ReportMensileDto
        """
        pass
    
    @abstractmethod
    def __repr__(self)->str:
        """
        definisce la rappresentazione tecnica delle istanze di ReportMensileDto
        
        :return: rappresentazione tecnica delle istanze di ReportMensileDto
        :rtype: str
        """
        pass
    
    @abstractmethod
    def __str__(self)->str:
        """
        definisce la rappresentazione human readable delle istanze di ReportMensileDto
        
        :return: rappresentazione human readable delle istanze di ReportMensileDto
        :rtype: str
        """
        pass
        
    @abstractmethod
    def __eq__(self,other)->bool:
        """
        definisce come stabilire l'uguaglianza di due istanze di ReportMensileDto
        
        :return: True se uguali, se no False
        :rtype: bool
        """
        pass
    
    @abstractmethod
    def __hash__(self)->int:
        """
        ritorna un hash creato dal contenuto dell'istanda di ReportMensileDto
        
        :return: hash dell'istanza
        :rtype: int
        """
        pass


# In[66]:


# @title src/application/dtos/report_mensile_dto.py
from datetime import datetime
class ReportMensileDto(AbstractReportMensileDto):
    
    """
    Rappresenta un entità di tipo ReportMensileDto che implementa il contratto AbstractReportMensileDto.
    """
    
    def __init__(self, data:datetime, importo:float):
        self.data=data
        self.importo = importo
        
    @property
    def data(self)->datetime:
        """
        ritorna la data della ReportMensileDto
        
        :return: data della ReportMensileDto
        :rtype: datetime
        """
        return self._data
    
    @data.setter
    def data(self,data:datetime)->None:
        """
        setta la data della ReportMensileDto
        
        :param datetime data: nuova data della ReportMensileDto
        """
        if(data is None or not isinstance(data,datetime)):
            raise TypeError("La data deve essere di tipo datetime e non può essere None")
        self._data = datetime(data.year,data.month,1)
    
    @property
    def importo(self)->float:
        """
        ritorna l'importo della ReportMensileDto
        
        :return: importo della ReportMensileDto
        :rtype: float
        """
        return self._importo
    
    @importo.setter
    def importo(self,importo:float)->None:
        """
        setta l'importo della ReportMensileDto
        
        :param float importo: nuovo importo della ReportMensileDto
        """
        if(importo is None or not isinstance(importo,(int,float))):
            raise TypeError("L'importo deve essere di tipo numerico")
        if(importo <= 0 ):
            raise ValueError("L'importo deve essere maggiore di 0")
        self._importo = importo
    
    def __repr__(self)->str:
        """definisce la rappresentazione tecnica delle istanze di ReportMensileDto"""
        return f"ReportMensileDto(data={datetime.strftime(self._data, '%Y-%m-%d %H:%M:%S')},importo={self._importo})"
    
    def __str__(self)->str:
        """definisce la rappresentazione human readable delle istanze di ReportMensileDto"""
        return f"Data: {datetime.strftime(self._data, '%Y-%m')}, Importo: {self._importo}"
    
    def __eq__(self,other)->bool:
        """
        definisce come stabilire l'uguaglianza di due istanze di ReportMensileDto
        
        :return: True se uguali, se no False
        :rtype: bool
        """
        if not isinstance(other, ReportMensileDto):
            return NotImplemented
        return self.data== other.data and self.importo == other.importo
    
    
    def __hash__(self)->int:
        """
        ritorna un hash creato dal contenuto dell'istanda di ReportMensileDto
        
        :return: hash dell'istanza
        :rtype: int
        """
        return hash((self.data, self.importo))

# In[67]:


# @title tests/application/dtos/test_report_mensile_dto.py

import unittest
from datetime import datetime
import sys

class TestReportMensileDto(unittest.TestCase):
    
    def setUp(self):
        self._data = datetime(2025,5,1)
        self._importo = 30.41
        self._dto = ReportMensileDto(self._data, self._importo)
        
    def test_costruttore(self):
        """Verifica che il costruttore funzioni correttamente"""
        self.assertEqual(self._dto.data,self._data)
        self.assertEqual(self._dto.importo,self._importo)
    
    def test_setter_data(self):
        """Verifica che la data venga impostata correttamente"""
        new_data = datetime(2025,5,7)
        self._dto.data = new_data
        self.assertEqual(self._dto.data,datetime(new_data.year,new_data.month,1))
        with self.assertRaises(TypeError):
            new_data = 0.0
            self._dto.data = new_data
        with self.assertRaises(TypeError):
            new_data = None
            self._dto.data = new_data
        with self.assertRaises(TypeError):
            new_data = 'ciao'
            self._dto.data = new_data           
    
    def test_setter_importo(self):
        """Verifica che l'importo venga impostato correttamente"""
        new_importo = 99.99
        self._dto.importo = new_importo
        self.assertEqual(self._dto.importo,new_importo)
        with self.assertRaises(ValueError):
            new_importo = -1.0
            self._dto.importo = new_importo
        with self.assertRaises(ValueError):
            new_importo = 0.0
            self._dto.importo = new_importo
        with self.assertRaises(TypeError):
            new_importo = None
            self._dto.importo = new_importo
        with self.assertRaises(TypeError):
            new_importo = 'ciao'
            self._dto.importo = new_importo   
        
    
    def test_repr(self):
        """Verifica che repr restituisca la rappresentazione corretta"""
        expected = f"ReportMensileDto(data={self._data},importo={self._importo})"
        self.assertEqual(repr(self._dto),expected)
        
    def test_str(self):
        """Verifica che str restituisca la rappresentazione corretta"""
        expected = f"Data: {datetime.strftime(self._data, '%Y-%m')}, Importo: {self._importo}"
        self.assertEqual(str(self._dto),expected)
    
    def test_eq_uguali(self):
        """Verifica che eq restituisca true quando uguali"""
        data = datetime(2025,5,1)
        importo = 30.41
        dto1 = ReportMensileDto(data, importo)
        dto2 = ReportMensileDto(data, importo)
        self.assertEqual(dto1,dto2)
        
    def test_eq_diversa_data(self):
        """Verifica che eq restituisca false quando diversa data"""
        data1 = datetime(2025,5,1)
        data2 = datetime(2024,5,1)
        importo = 30.41
        dto1 = ReportMensileDto(data1, importo)
        dto2 = ReportMensileDto(data2, importo)
        self.assertNotEqual(dto1,dto2)
        
    def test_eq_diverso_importo(self):
        """Verifica che eq restituisca true quando diverso importo"""
        data = datetime(2025,5,1)
        descrizione = 'spesa di test'
        importo1 = 30.41
        importo2 = 96.94
        dto1 = ReportMensileDto(data, importo1)
        dto2 = ReportMensileDto(data, importo2)
        self.assertNotEqual(dto1,dto2)

esegui_tests(TestReportMensileDto)

# # src/application/use_cases
# Contiene i casi d'uso che sono sostanzialmente le operazioni previste dal nostro modello nelle specifiche in "funzionalità chiave".
# Nel nostro caso questi casi d'uso saranno poi attivati dall'utente mediante interfaccia console ma si possono utilizzare anche in processi batch
# (Es. servizi schedulati per reportistica periodica) dove l'attore ad eseguire l'operazione non è un utente ma un Sistema (vedi teoria DDD).

# In[68]:


# @title src/application/use_cases/abstract_use_case.py

from abc import ABC,abstractmethod
# Cercavo un modo per generalizzare il tipo di ritorno del metodo dentro l'interfaccia generica (come in C# O java) e
# ho trovato questa soluzione
from typing import Generic, TypeVar

# Dichiarazione del tipo generico (può rappresentare qualunque tipo) da usare come segnaposto in classi e funzioni
I = TypeVar("I")
O = TypeVar("O")

class AbstractUseCase(ABC,Generic[I,O]):
    """
    Classe astratta che definirà i metodi che dovra necessariamente implementare uno usecase
    """
    @abstractmethod
    def execute(self,input: I)->O:
        """
        Esegue lo use case e ritorna un risultato
        
        :param I input: None o eventuali dto forniti come parametro dello use case
        :return: None o eventuali dto prodotti dall'implementazione dello use case
        :rtype: O
        """
        pass

    

# In[69]:


# @title src/application/use_cases/aggiungi_spesa_use_case.py

class AggiungiSpesaUseCase(AbstractUseCase[AbstractSpesa,None]):
    """
    classe che implementa la logica per lo use case per aggiungere una nuova spesa
    """
    def __init__(self, service:AbstractSpesaService):
        self._service = service
        
    def execute(self,input:AbstractSpesa)->None:
        """
        Richiama il service per salvare la nuova Spesa
        
        :param AbstractSpesa input: oggetto che implementa AbstractSpesa da passare al service
        """
        self._service.aggiungi_spesa(input)

# In[70]:


# @title tests/application/use_cases/test_aggiungi_spesa_use_case.py

import unittest
from unittest.mock import patch, mock_open, MagicMock, call
import sys

class TestAggiungiSpesaUseCase(unittest.TestCase):
    

    def setUp(self):
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._use_case = AggiungiSpesaUseCase(self._service)
        
    def test_execute(self):
        """Verifica che lo use case utilizzi propriamente il service quando viene aggiunta una Spesa"""
        spesa_mock = MagicMock(spec_set=AbstractSpesa)
        spesa_mock.data = datetime(2025,12,1)
        spesa_mock.descrizione = 'spesa di test'
        spesa_mock.importo = 50.50
        
        self._use_case.execute(spesa_mock)
        
        self._use_case._service.aggiungi_spesa.assert_called_once_with(spesa_mock)

esegui_tests(TestAggiungiSpesaUseCase)

# In[71]:


# @title src/application/use_cases/report_mensile_use_case.py
from itertools import groupby

class ReportMensileUseCase(AbstractUseCase[None,list[AbstractReportMensileDto]]):
    """
    classe che implementa la logica per lo use case per generare il report mensile
    """
    def __init__(self, service:AbstractSpesaService):
        self._service = service
        
    # per l'implementazione pulita ed efficace ci questo metodo prendo spunto da https://stackoverflow.com/questions/38647928/sum-list-of-list-elements-in-python-like-sql-group-by
    def execute(self,input:None=None)->list[AbstractReportMensileDto]:
        """
        Richiama il Service per reperire la list delle spese,
        raggruppa per mese e anno sommando l'importo e generando il dto,
        ordina per mese e anno e restituisce il risultato in ordine
        decrescente di date
        
        :param AbstractSpesa input: oggetto che implementa AbstractSpesa da passare al service
        """
        results: list[AbstractReportMensileDto] = []
        spese = self._service.ottieni_tutte_le_spese()
        
        dtos = [ ReportMensileDto(spesa.data,spesa.importo) for spesa in spese ]
        dtos_ordinati = sorted(dtos, key = lambda x: x.data,reverse=True)
        
        
        for chiave, dati in groupby(dtos_ordinati, key = lambda x: x.data):
            data = chiave
            importo = sum(dato.importo for dato in dati)
            nuovo_dto = ReportMensileDto(data,importo)
            results.append(nuovo_dto)
                
        return results

# In[72]:


# @title tests/application/use_cases/test_report_mensile_use_case.py

import unittest
from unittest.mock import patch, mock_open, MagicMock, call
import sys

class TestReportMensileUseCase(unittest.TestCase):
    

    def setUp(self):
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._use_case = ReportMensileUseCase(self._service)
        
    def test_execute(self):
        """Verifica che lo use case utilizzi propriamente il service quando deve generare la lista per il report mensile"""
        mock_spese:list[AbstractSpesa] = [
            Spesa(datetime(2026,1,1),'sigarette',3),
            Spesa(datetime(2025,12,1),'sigarette',1),
            Spesa(datetime(2025,12,2),'sigarette',2),
            Spesa(datetime(2026,2,2),'sigarette',4),
            Spesa(datetime(2026,2,2),'sigarette',4),
            ]
        expected: list[AbstractReportMensileDto] = [
            ReportMensileDto(data=datetime(2026,2,2),importo=8),
            ReportMensileDto(data=datetime(2026,1,1),importo=3),
            ReportMensileDto(data=datetime(2025,12,1),importo=3),
            ]
        
        self._service.ottieni_tutte_le_spese.return_value = mock_spese
        
        result: list[AbstractReportMensileDto] = self._use_case.execute()
        
        self._use_case._service.ottieni_tutte_le_spese.assert_called_once_with()
        
        self.assertEqual(result,expected)
        
esegui_tests(TestReportMensileUseCase)

# In[73]:


# @title src/application/use_cases/top_10_spese_use_case.py
from itertools import groupby

class Top10SpeseUseCase(AbstractUseCase[None,list[AbstractSpesa]]):
    """
    classe che implementa la logica per lo use case per generare la lista delle 10 top Spese
    """
    def __init__(self, service:AbstractSpesaService):
        self._service = service
        
    # per l'implementazione pulita ed efficace ci questo metodo prendo spunto da https://stackoverflow.com/questions/38647928/sum-list-of-list-elements-in-python-like-sql-group-by
    def execute(self,input:None=None)->list[AbstractSpesa]:
        """
        Richiama il Service per reperire la list delle spese;
        la ordina in base a import e data in ordine descrescente
        di risultato e crescente di data;
        restituisce il risultato in ordine
        
        :param AbstractSpesa input: oggetto che implementa AbstractSpesa da passare al service
        """
        results: list[AbstractSpesa] = []
        spese = self._service.ottieni_tutte_le_spese()
        # usato tupla per doppio ordinamento, simile a linq in C#
        spese_ordinate = sorted(spese, key = lambda x: (x.importo,x.data), reverse=True)
        
        results = spese_ordinate[0:10]
                    
        return results

# In[74]:


# @title tests/application/use_cases/test_top_10_spese_use_case.py

import unittest
from datetime import datetime
from unittest.mock import patch, mock_open, MagicMock, call
import sys

class TestTop10SpeseUseCase(unittest.TestCase):
    

    def setUp(self):
        self._service = MagicMock(spec_set=AbstractSpesaService)
        self._use_case = Top10SpeseUseCase(self._service)
        
    def test_execute(self):
        """Verifica che lo use case utilizzi propriamente il service quando deve ritornare le 10 top Spese"""
        mock_spese:list[AbstractSpesa] = [
            Spesa(datetime(2025,2,2),'sigarette',2.0),
            Spesa(datetime(2025,2,2),'sigarette',3.0),
            Spesa(datetime(2025,2,3),'sigarette',2.0),
            Spesa(datetime(2025,3,2),'sigarette',5.0),
            Spesa(datetime(2025,4,2),'sigarette',12.0),
            ]

        expected: list[AbstractSpesa] = [
            Spesa(datetime(2025,4,2),'sigarette',12.0),
            Spesa(datetime(2025,3,2),'sigarette',5.0),
            Spesa(datetime(2025,2,2),'sigarette',3.0),
            Spesa(datetime(2025,2,3),'sigarette',2.0),
            Spesa(datetime(2025,2,2),'sigarette',2.0),
            ]
        
        self._service.ottieni_tutte_le_spese.return_value = mock_spese
        
        result: list[AbstractSpesa] = self._use_case.execute()
        
        self._use_case._service.ottieni_tutte_le_spese.assert_called_once_with()
        
        self.assertEqual(result,expected)

esegui_tests(TestTop10SpeseUseCase)

# # src/interfaces/
# Contiene gli elementi reponsabili di consentire all'utente o sistema di utilizzare in maniera propria gli in use case implementati.
# Per il caso specifico implementerò solo una cli per interfaccia input da terminale ma è tranquillamente estensibile con controller rest o altre tipologie di interfaccia esterna.

# # src/interfaces/cli
# Per la mia cli, in base ad un corso che mi ha molto appassionato su design pattern e principi solid seguito su [udemy](https://www.udemy.com/course/basics-of-software-architecture-design-in-java/), applicherò il design pattern "command" di categoria "behavioral". Questo perchè il corso lo consiglia per le interfacce utente ed avendolo sperimentato in java ho notato che è una soluzione elegante che consente di rispettare l'open-closed principle, quindi di rendere il codice aperto all'implementazione e chiuso alla modifica (evitando una possibile cascata immensa di if all'aumentare del numero di comandi e consentendo di non modificare logica già scritta).

# In[75]:


# @title src/interfaces/cli/commands/abstract_command.py

from abc import ABC,abstractmethod

class AbstractCommand(ABC):
    """
    Classe astratta che definirà i metodi che dovra necessariamente implementare un comando della cli
    """
    @abstractmethod
    def execute(self)->None:
        """Esegue il comando relativo alla classe"""
        pass

# In[76]:


# @title src/interfaces/cli/commands/aggiungi_spesa_command.py

class AggiungiSpesaCommand(AbstractCommand):
    """Comando che gestirà l'aggiunta di una nuova spesa"""
    def __init__(self,use_case:AggiungiSpesaUseCase):
        self._use_case = use_case
        
    def _gestisci_input(self)->AbstractSpesa:
        data_testo = input("Inserisci la data della nuova spesa nel formato dd/mm/yyyy")
        data = datetime.strptime(data_testo,'%d/%m/%Y')
        descrizione = input("Inserisci la descrizione della nuova spesa")
        importo = float(input("Inserisci l'importo della nuova spesa"))
        new_spesa = Spesa(data, descrizione, importo)
        return new_spesa
    
    def _mostra_output(self,new_spesa:AbstractSpesa)->None:
        print(f"Aggiunta con successo nuova Spesa: {new_spesa}")
        
        
    def execute(self)->None:
        """Esegue il comando relativo alla classe"""
        new_spesa = self._gestisci_input()
        self._use_case.execute(new_spesa)
        self._mostra_output(new_spesa)
        

# In[77]:


# @title test/interfaces/cli/commands/test_aggiungi_spesa_command.py
import unittest 
from unittest.mock import MagicMock, patch
import sys

class TestAggiungiSpesaCommand(unittest.TestCase):
    """tests del command AggiungiSpesaCommand"""
    def setUp(self):
        self._use_case = MagicMock(spec_set=AggiungiSpesaUseCase)
        self._command = AggiungiSpesaCommand(self._use_case)
        
    @patch.object(AggiungiSpesaCommand, '_mostra_output')
    @patch.object(AggiungiSpesaCommand, '_gestisci_input')
    def test_execute(self, mock_gestisci_input, mock_mostra_output):
        """Verifica il corretto uso dello use case e la corretta invocazione dei metodi di input e output"""
        mock_spesa = MagicMock(spec_set=AbstractSpesa)
        mock_gestisci_input.return_value = mock_spesa
        
        self._command.execute()
        
        mock_gestisci_input.assert_called_once_with()
        self._command._use_case.execute.assert_called_once_with(mock_spesa)
        mock_mostra_output.assert_called_once_with(mock_spesa)

esegui_tests(TestAggiungiSpesaCommand)

# In[78]:


# @title src/interfaces/cli/commands/report_mensile_command.py
class ReportMensileCommand(AbstractCommand):
    """Comando che mostrerà report mensile"""
    def __init__(self,use_case:ReportMensileUseCase):
        self._use_case = use_case
        
    def _mostra_output(self,report:list[AbstractReportMensileDto])->None:
        print("Report Mensile:")
        for dato in report:
            print(dato)
        
    def execute(self)->None:
        """Esegue il comando relativo alla classe"""
        report:list[AbstractReportMensileDto] = self._use_case.execute()
        self._mostra_output(report)

# In[79]:


# @title test/interfaces/cli/commands/test_report_mensile_command.py
import unittest 
from unittest.mock import MagicMock, patch
import sys

class TestReportMensileCommand(unittest.TestCase):
    """tests del command ReportMensileCommand"""
    def setUp(self):
        self._use_case = MagicMock(spec_set=ReportMensileUseCase)
        self._command = ReportMensileCommand(self._use_case)
        
    @patch.object(ReportMensileCommand, '_mostra_output')
    def test_execute(self, mock_mostra_output):
        """Verifica il corretto uso dello use case e la corretta invocazione dei metodi di output"""
        mock_report:list = [
            MagicMock(spec_set=AbstractReportMensileDto),
            MagicMock(spec_set=AbstractReportMensileDto),
            MagicMock(spec_set=AbstractReportMensileDto),
            ]
        self._use_case.execute.return_value = mock_report
        
        self._command.execute()
        
        self._command._use_case.execute.assert_called_once_with()
        mock_mostra_output.assert_called_once_with(mock_report)

esegui_tests(TestReportMensileCommand)

# In[80]:


# @title src/interfaces/cli/commands/top_10_spese_command.py
class Top10SpeseCommand(AbstractCommand):
    """Comando che mostrerà le top 10 Spese"""
    def __init__(self,use_case:Top10SpeseUseCase):
        self._use_case = use_case
        
    def _mostra_output(self,report:list[AbstractSpesa])->None:
        print("Top 10 Spese:")
        for dato in report:
            print(dato)
        
    def execute(self)->None:
        """Esegue il comando relativo alla classe"""
        report:list[AbstractSpesa] = self._use_case.execute()
        self._mostra_output(report)

# In[81]:


# @title test/interfaces/cli/commands/test_top_10_spese_command.py
import unittest 
from unittest.mock import MagicMock, patch
import sys

class TestTop10SpeseCommand(unittest.TestCase):
    """tests del command Top10SpeseCommand"""
    def setUp(self):
        self._use_case = MagicMock(spec_set=Top10SpeseUseCase)
        self._command = Top10SpeseCommand(self._use_case)
        
    @patch.object(Top10SpeseCommand, '_mostra_output')
    def test_execute(self, mock_mostra_output):
        """Verifica il corretto uso dello use case e la corretta invocazione dei metodi di output"""
        mock_report:list = [
            MagicMock(spec_set=AbstractSpesa),
            MagicMock(spec_set=AbstractSpesa),
            MagicMock(spec_set=AbstractSpesa),
            ]
        self._use_case.execute.return_value = mock_report
        
        self._command.execute()
        
        self._command._use_case.execute.assert_called_once_with()
        mock_mostra_output.assert_called_once_with(mock_report)
        
esegui_tests(TestTop10SpeseCommand)

# In[82]:


# @title src/interfaces/cli/main.py
# Ho provato a gestire l'uscita del programma creando un ExitCommand ma al comando exit(0) giustamente crashava il kernel. lo gestirò con un semplice if ma questa idea non mi fa impazzire
class GestoreSpeseCli:
    """classe principale del interfaccia utente, orchestra i componenti della mia infrastruttura e fornisce la cli"""
    def __init__(self) -> None:
        datasource:AbstractSpesaDataSource = SpesaDataSourceCsv()
        repository:AbstractSpesaRepository = SpesaRepository(datasource)
        service:AbstractSpesaService = SpesaService(repository)
        aggiungi_spesa_use_case: AbstractUseCase = AggiungiSpesaUseCase(service)
        report_mensile_use_case: AbstractUseCase = ReportMensileUseCase(service)
        top_10_spese_use_case: AbstractUseCase = Top10SpeseUseCase(service)
        aggiungi_spesa_command: AbstractCommand = AggiungiSpesaCommand(aggiungi_spesa_use_case)
        report_mensile_command: AbstractCommand = ReportMensileCommand(report_mensile_use_case)
        top_10_spese_command: AbstractCommand = Top10SpeseCommand(top_10_spese_use_case)
        
        self._commands: dict[str,AbstractCommand] = {
            "1":{"comando": aggiungi_spesa_command, "descrizione": "Aggiungi una Spesa"},
            "2":{"comando": report_mensile_command, "descrizione": "Mostra Report Mensile"},
            "3":{"comando": top_10_spese_command, "descrizione": "Mostra Top 10 delle Spese"},
            "esci":{"comando": None, "descrizione": "Esci dal programma"}
        }
                
    def run(self) -> None:
        """"""
        print("Gestore Spese")
        while True:
            try:
                print("Scegli fra una delle seguenti opzioni (inserendo il numero):")
                # Per capire come fare ho usato https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
                for key,value in self._commands.items():
                    print(f"[{key}] {value["descrizione"]}")
                comando_inserito = input().strip().lower()
                if (comando_inserito == "esci"):
                    print("Grazie e Arrivederci!")
                    break
                self._commands[comando_inserito]["comando"].execute()
            except KeyError:
                print("Comando non valido, riprova")
            except ValueError:
                print("Valore di input non valido")
                
        
GestoreSpeseCli().run()

