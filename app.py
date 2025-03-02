from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos en Neon PostgreSQL
DB_URL = "postgresql://neondb_owner:npg_Tztdo6RxWyF7@ep-tiny-wildflower-a5shc9ma-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"

def connect_db():
    return psycopg2.connect(DB_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        dui = request.form['dui']
        edad = request.form['edad']
        telefono = request.form['telefono']
        grupo = request.form['grupo']
        municipio = request.form['municipio']
        comunidad = request.form['comunidad']
        area = request.form['area']
        procesos_actuales = request.form['procesos_actuales']
        procesos_previos = request.form['procesos_previos']
        total_procesos = request.form['total_procesos']
        
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO personas (nombre_completo, dui, edad, telefono, grupo_organizacion, municipio, comunidad, area, procesos_actuales, procesos_previos, total_procesos_actuales)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombre, dui, edad, telefono, grupo, municipio, comunidad, area, procesos_actuales, procesos_previos, total_procesos))
        conn.commit()
        cur.close()
        conn.close()
        
        return "Datos ingresados correctamente"
    
    return render_template('form.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
