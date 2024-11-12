# 🌿 EVI Index Visualization

## 📋 Project Overview
This project is a web application designed to visualize the **Enhanced Vegetation Index (EVI)** using satellite data. The app leverages **PostgreSQL with PostGIS**, **Flask**, and **React** to provide an interactive map displaying classified vegetation data for different years and the ability to calculate averages.

## 📊 Tech Stack
- **Backend**: Python, Flask, PostgreSQL, PostGIS
- **Frontend**: React, Mapbox GL JS, Axios
- **Data Format**: GeoTIFF files imported into PostgreSQL

---

## ⚙️ Prerequisites
Make sure you have the following installed:
- Python 3.x
- PostgreSQL with PostGIS extension
- Node.js and npm
- Git

---

## 🚀 Project Setup

### 1. Clone the Repository
```
git clone https://github.com/FridrichPeter/evi_visualization.git
cd evi-visualization
```

### 2. Backend Setup (Flask + PostgreSQL)
a) Set up a Virtual Environment
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```
b) Create a PostgreSQL Database
```
CREATE DATABASE geotiff_viewer; 
```
c) Enable PostGIS Extension
```
\c geotiff_viewer;
CREATE EXTENSION postgis;
```
d) Import GeoTIFF Data
```
raster2pgsql -s 4326 -I -C -M "/mnt/c/Users/...../file.tif" public.table_name | psql -U postgres -d geotiff_viewer -h localhost -p 5432

```
e) Run the Flask Application
```
python app.py
#....http://localhost:5000
```
### 2. Frontend Setup (React)
```
cd evi-map
npm install
npm start
#....http://localhost:3000
```
🌍 Features
Interactive Map: Visualize classified EVI data with color-coded layers.
Dropdown Menu: Select different years to display vegetation data.
Popup Information: Click on map regions to view detailed EVI values.
Responsive Map Controls: Zoom, pan, and fullscreen options.

🗺️ Map Legend
EVI Value	Description	Color
1	Low vegetation	🔴 Red
2	Medium vegetation	🟠 Orange
3	Dense vegetation	🟡 Yellow
4	Very dense vegetation	🟢 Green
5	Extremely dense veg.	🟣 Teal
