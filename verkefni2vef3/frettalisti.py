from flask import Flask
from flask import render_template

app = Flask(__name__)

frettaListi = [
{
            "id": 0,
            "flokkur": "sport",
            "hofundur": "Afi minn :)",
            "fyrirsogn": "Einhver spilar golf",
            "meginmal": "Þar eru til fólk sem spilar golf. Golf er þar sem maður setur kúlu í holu eða eitthvað idk",
            "mynd": "mynd2.jpg",
        },
        {
            "id": 1,
            "flokkur": "annad",
            "hofundur": "J.K. Rowling",
            "fyrirsogn": "Hákarl í skítugu vatni",
            "meginmal": "Hér er mynd tekin 12/12/9999 af hákarli í skítugu vatni. Myndtakarinn er tímaflakkari og tók mynd.",
            "mynd": "mynd1.jpg",
        },
        {
            "id": 2,
            "flokkur": "sport",
            "hofundur": "Daníel Símon Galvez",
            "fyrirsogn": " Veiði",
            "meginmal": " Einhver veiddi fisk, og það var fiskur. Mjög sjaldgæf sjón.",
            "mynd": "mynd5.jpg",
        },
        {
            "id": 3,
            "flokkur": "annad",
            "hofundur": "Tækniskólinn á Akureyri",
            "fyrirsogn": "Eitthvað með Eurobasket",
            "meginmal": "Körfubolti",
            "mynd": "mynd3.jpg",
        },
        {
            "id": 4,
            "flokkur": "almennt",
            "hofundur": "Fornafn Eftirnafn",
            "fyrirsogn": "Hopp",
            "meginmal": "Hann hoppar :D",
            "mynd": "mynd4.jpg",
        },
        {
            "id": 5,
            "flokkur": "almennt",
            "hofundur": "Walt Disney",
            "fyrirsogn": "Einhver lenti í slysi",
            "meginmal": "Einhver keyrði og búmm slys haha",
            "mynd": "mynd0.jpg",
        }
]

@app.route("/")
def index():
    return render_template('index.html', lf = frettaListi)

@app.route('/frett/<int:id>')
def frett(id):
    frett = frettaListi[id]
    return render_template('frett.html', frett=frett)

@app.route('/frettalisti/<flokkur>')
def frettalisti(flokkur):
    return render_template('frettalisti.html', lf = frettaListi, flokkur = flokkur)

if __name__ == "__main__":
    app.run(debug=True)