# ⚽ Football Data Warehouse

## 🚀 Overview

Football Data Warehouse è un progetto di Data Engineering sviluppato in Python che implementa una pipeline ETL completa per l'acquisizione, la trasformazione e il caricamento di dati calcistici all'interno di un Data Warehouse PostgreSQL.

Il progetto utilizza dati provenienti da una Football Data API, li trasforma tramite Pandas e li organizza secondo un modello Star Schema per supportare attività di analisi e reporting.

---

## 🏗️ Architettura

```text
Football Data API
        │
        ▼
     Extract
    (Requests)
        │
        ▼
    Transform
     (Pandas)
        │
        ▼
       Load
   (SQLAlchemy)
        │
        ▼
    PostgreSQL
        │
        ▼
 Data Warehouse
        │
        ▼
     Power BI
```

---

## 🧰 Tech Stack

- Python
- Requests
- Pandas
- PostgreSQL
- SQLAlchemy
- Power BI

---

## ⚙️ ETL Pipeline

### Extract

Nella fase di Extract ho utilizzato la libreria `Requests` per effettuare chiamate HTTP verso la Football Data API e recuperare i dati in formato JSON.

### Transform

Nella fase di Transform ho utilizzato `Pandas` per lavorare con i DataFrame, pulire i dati, eliminare eventuali ridondanze e prepararli per il caricamento nel Data Warehouse.

### Load

Nella fase di Load ho utilizzato `SQLAlchemy` per gestire la connessione al database PostgreSQL e caricare i dati nelle tabelle del Data Warehouse.

---

## 📊 Data Warehouse Design

Il Data Warehouse è stato modellato secondo uno **Star Schema**.

### Fact Table

- `fact_matches`

Contiene gli eventi principali del business:

- Partite
- Gol realizzati
- Chiavi esterne verso le dimensioni

### Dimension Tables

- `dim_team`
- `dim_competition`
- `dim_date`

Le Dimension Tables contengono informazioni descrittive utilizzate per contestualizzare i dati presenti nella Fact Table.

---

## 🗄️ Database Concepts Implementati

Durante il progetto sono stati utilizzati i principali concetti di modellazione relazionale:

- Primary Key
- Foreign Key
- INNER JOIN
- LEFT JOIN
- Aggregazioni SQL
- GROUP BY
- Star Schema

---

## 📈 Analytics

Sono state sviluppate query SQL per ottenere:

- Top Scoring Teams
- Match Count
- Average Goals
- Goals By Competition
- Matches By Competition
- Average Goals By Competition

---

## 📋 Dashboard Power BI

La dashboard Power BI è collegata direttamente al Data Warehouse PostgreSQL e consente di visualizzare:

- Numero totale di partite
- Numero totale di squadre
- Numero totale di competizioni
- Gol segnati per squadra

---

## 🎯 Competenze Dimostrate

- ETL (Extract, Transform, Load)
- API REST
- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- SQL
- Data Warehouse
- Fact Table
- Dimension Table
- Star Schema
- Data Analysis
- Power BI

---

## 💡 Risultati

Il progetto dimostra la realizzazione end-to-end di una pipeline Data Engineering:

```text
API REST
↓
ETL
↓
PostgreSQL
↓
Data Warehouse
↓
SQL Analytics
↓
Power BI Dashboard
```

---

## 👨‍💻 Autore

**Giovanni Iadelise**
