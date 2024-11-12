from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

def get_db_connection():
    conn = psycopg2.connect(
        dbname='evi_db',
        user='pg',
        password='***',
        host='localhost',
        port='5432'
    )
    return conn

# Endpoint na získanie zoznamu tabuliek
@app.route('/api/tables', methods=['GET'])
def get_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_name LIKE 'classified_%' OR table_name = 'evi_classified_mean_reclassified';
    """
    cur.execute(query)
    tables = cur.fetchall()
    cur.close()
    conn.close()

    table_list = [table[0] for table in tables]
    return jsonify(table_list)

# **Nový endpoint pre načítanie GeoJSON dát z konkrétnej tabuľky**
@app.route('/api/evi', methods=['GET'])
def get_evi_data():
    table_name = request.args.get('table')
    if not table_name:
        return jsonify({"error": "Table name is required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # Dynamický dotaz na získanie GeoJSON z vybranej tabuľky
        query = f"""
            SELECT ST_AsGeoJSON((gv).geom) AS geometry, (gv).val AS value
            FROM (SELECT ST_DumpAsPolygons(rast) AS gv FROM "{table_name}") subquery;
        """
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        conn.close()

        # Transformácia výsledkov na GeoJSON formát
        features = [{
            "type": "Feature",
            "geometry": json.loads(row[0]),
            "properties": {"value": row[1]}
        } for row in data]

        geojson = {
            "type": "FeatureCollection",
            "features": features
        }

        return jsonify(geojson)

    except Exception as e:
        cur.close()
        conn.close()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
