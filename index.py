from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html') #Hacer un video de introduccion

@app.route('/carta')
def carta():
    return render_template('carta.html') #Hacer una carta 

@app.route('/teamo')
def video():
    return render_template('video.html') #Hacer un video

if __name__ == '__main__':
    app.run(debug=True)
