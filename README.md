# ⚽ Football Data Warehouse

<p align="center">
  <b>ETL Pipeline • PostgreSQL • Data Warehouse • Power BI</b>
</p>

---

## 🚀 Overview

Football Data Warehouse è un progetto di Data Engineering sviluppato in Python.

L'obiettivo è costruire una pipeline ETL completa che:

- Estrae dati calcistici tramite API REST
- Trasforma i dati con Pandas
- Carica i dati in PostgreSQL
- Implementa un Data Warehouse con Star Schema
- Fornisce analisi statistiche tramite SQL
- Visualizza i KPI tramite Power BI

---

## 🏗️ Architettura

```text
Football Data API
        │
        ▼
    Extract
        │
        ▼
   Transform
        │
        ▼
      Load
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

| Categoria | Tecnologie |
|------------|------------|
| Language | Python |
| Data Processing | Pandas |
| API | Requests |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| BI & Reporting | Power BI |
| Data Modeling | Star Schema |

---

## 📊 Data Warehouse Model

### Fact Table

- `fact_matches`

### Dimension Tables

- `dim_team`
- `dim_competition`
- `dim_date`

---

## ⚙️ ETL Pipeline

### Extract

- Acquisizione dati tramite Football Data API

### Transform

- Pulizia dati
- Conversione strutture JSON
- Preparazione dataset

### Load

- Caricamento dati in PostgreSQL
- Aggiornamento Data Warehouse

---

## 📈 Analytics

Statistiche implementate:

- Top Scoring Teams
- Match Count
- Average Goals
- Goals by Competition
- Matches by Competition
- Average Goals by Competition

---

## 📋 Dashboard Power BI

La dashboard permette di monitorare:

✅ Numero totale di partite

✅ Numero totale di squadre

✅ Numero totale di competizioni

✅ Gol realizzati per squadra

Dashboard disponibile nel file:

```text
report.pbix
```

Screenshot disponibile in:

```text
docs/report.png
```

---

## 🎯 Competenze Dimostrate

- ETL Development
- REST API Integration
- Pandas Data Processing
- PostgreSQL
- SQL
- SQLAlchemy
- Data Warehouse Modeling
- Star Schema
- Fact & Dimension Tables
- Power BI Reporting

---

## 👨‍💻 Autore

**Iadelise Giovanni**

📧 iadelisegiovanni2000@gmail.com

🐱 GitHub: github.com/IadeliseGiovanni
