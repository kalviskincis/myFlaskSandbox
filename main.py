from flask import Flask, render_template, jsonify, json, request, make_response
# import dati

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/skolenu_izvelne')
def skIzvele():
    return render_template('skolenu_izvelne.html')


@app.route('/IIC')
def iic():
    return render_template('IIC.html')


@app.route('/vecaku_pietekumus')
def vPieteikums():
    return render_template('vecaku_pieteikums.html')


@app.route('/pinfo')
def pinfo():
    return render_template('pulcina_info.html')


@app.route('/registret_IIC', methods=['POST'])
def regIIC():
    with open("dati/iic.json", "r", encoding='utf-8') as f:
        dati = json.loads(f.read())
    jaunsIIC = json.loads(request.data)
    for d in dati:
        if d["iicnosaukums"] == jaunsIIC["iicnosaukums"]:
            # d["forma"]=render_template("forma.html")
            atbilde = {"statuss": "Šī IIC jau ir reģistrēta"}
            atbilde["pulcins"] = render_template('pulcina_info.html')
            return jsonify(atbilde)

    dati.append(jaunsIIC)

    with open("dati/iic.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(dati))

    atbilde = {"statuss": "IIC veiksmīgi piereģistrēta"}
    atbilde["pulcins"] = render_template('pulcina_info.html')
    return jsonify(atbilde)


@app.route('/testForm', methods=["POST"])
def testForm():
    vards = request.form["vards"]
    pulcins = request.form["kas"]
    laiks = request.form["kad"]
    print(vards, pulcins, laiks)
    return "vvv"


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
