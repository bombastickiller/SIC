from flask import Flask,request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    from leer_confg import velocidadDeParpadeo
    return render_template ('configuracion.html', velocidad=velocidadDeParpadeo)
@app.route('/grabarconfiguracion', methods = ['GET', 'POST'])

def grabarconfiguracion():
    velocidad = request.form['velocidad']
    import leer_confg
    leer_confg.velocidadDeParpadeo = velocidad
    leer_confg.grabarConfiguracion()
    return redirect("/")
    
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')