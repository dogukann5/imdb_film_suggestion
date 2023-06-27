from flask import Flask, render_template, request, make_response, jsonify
import analysis

app = Flask(__name__)

#film return
def film_return(emotion):
    film = analysis.random_film(emotion)
    film_info = {
        'Poster': film[0],
        'Title': film[1],
        'Year': film[2],
        'Genre': film[5],
        'Rating': film[6],
        'Metascore': film[8],
        'Description': film[7],
        'Director': film[9],
        'Votes': film[14],
        'Revenue': film[15],
        'Runtime': film[4],
        'Actors': [film[10], film[11], film[12], film[13]],
    }
    return film_info

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            emotion = request.form['emotion']
            film = film_return(emotion)
            return render_template('index.html', film=film)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 