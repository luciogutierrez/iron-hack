from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about') 
def about():
    notas = ("nota1","nota2","nota3","nota4","nota5","nota6")
    return render_template('about.html', notas=notas)
    
if __name__ == '__main__':
    app.run(debug=True)
