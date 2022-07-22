from cProfile import label
from flask import g, render_template
from app import app
import json
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./jsonFiles/coviRepo/covidRepo/json/andamento/dpc-covid19-ita-andamento-nazionale-latest.json")

f = open(path)
andamentoNazionaleLast = json.load(f)
f.close()

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./jsonFiles/coviRepo/covidRepo/json/andamento/dpc-covid19-ita-andamento-nazionale.json")

f = open(path)
andamentoNazionale = json.load(f)
f.close()

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./jsonFiles/coviRepo/covidRepo/json/andamento/dpc-covid19-ita-regioni-latest.json")


f = open(path)
andamentoRegioniLast = json.load(f)
f.close()

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./jsonFiles/coviRepo/covidRepo/json/andamento/dpc-covid19-ita-note.json")


f = open(path)
note = json.load(f)
f.close()

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./jsonFiles/coviRepo/covidRepo/json/vaccini/vaccini-summary-latest.json")

f = open(path)
vaccini = json.load(f)
f.close()






labelsAttualmentePositivi = []
valuesAttualmentePositivi = []

labelsandamentoRegioniLast = []
valuesandamentoRegioniLast = []

noteObj = []

for x in range(1):
    noteObj.insert(0,note[len(note)-x-1])






labelsTamponiMolecolari = []
valuesPositiviTestMolecolare = []
valuesTestMolecolare = []

for x in andamentoRegioniLast:
    labelsandamentoRegioniLast.insert(0,x["denominazione_regione"])
    valuesandamentoRegioniLast.insert(0,x["totale_positivi"])



for x in range(31):
    g = andamentoNazionale[len(andamentoNazionale)-x-1]['data']

    listData = g.split('-')
    anno = listData[0]
    mese = listData[1]
    giorno = listData[2].split('T')[0]
    labelsAttualmentePositivi.insert(0,giorno+"/"+mese)

    totPos = andamentoNazionale[len(andamentoNazionale)-x-1]['totale_positivi']
    valuesAttualmentePositivi.insert(0,totPos)




    labelsTamponiMolecolari.insert(0,giorno+"/"+mese)

    valuesPositiviTestMolecolare.insert(0,andamentoNazionale[len(andamentoNazionale)-x-1]['totale_positivi_test_molecolare']-andamentoNazionale[len(andamentoNazionale)-x-2]['totale_positivi_test_molecolare'])
    valuesTestMolecolare.insert(0,andamentoNazionale[len(andamentoNazionale)-x-1]['tamponi_test_molecolare']-andamentoNazionale[len(andamentoNazionale)-x-2]['tamponi_test_molecolare'])








@app.route('/')
@app.route('/index')
def index():

    data = andamentoNazionaleLast[0]['data']
    ieri = andamentoNazionale[len(andamentoNazionale)-2]
    oggi = andamentoNazionale[len(andamentoNazionale)-1]
    ieri = andamentoNazionale[len(andamentoNazionale)-2]
    unaSettimanaFa = andamentoNazionale[len(andamentoNazionale)-8]




    listData = data.split('-')
    anno = listData[0]
    mese = listData[1]
    giorno = listData[2].split('T')[0]

    obj = {}

    dataObj = {}
    dataObj["anno"] = anno
    dataObj["mese"] = mese
    dataObj["giorno"] = giorno

    obj["ieri"] = ieri
    obj["oggi"] = oggi
    obj["unaSettimanaFa"] =unaSettimanaFa
    obj["data"] = dataObj

    objChart = {}
    chartAttualmentePositivi = {}
    chartAndamentoRegioniLast = {}
    chartTamponiMolecolari = {}

    chartAttualmentePositivi["labels"] = labelsAttualmentePositivi
    chartAttualmentePositivi["values"] = valuesAttualmentePositivi

    chartAndamentoRegioniLast["labels"] = labelsandamentoRegioniLast
    chartAndamentoRegioniLast["values"] = valuesandamentoRegioniLast

    chartTamponiMolecolari["labels"] = labelsTamponiMolecolari
    chartTamponiMolecolari["values"] = {"positiviTest":valuesPositiviTestMolecolare,"TestMolecolare":valuesTestMolecolare}


    objChart["attualmentePositivi"] = chartAttualmentePositivi
    objChart["andamentoRegioniLast"] = chartAndamentoRegioniLast

    objChart["testMolecolare"] = chartTamponiMolecolari

    obj["note"] = noteObj
    obj["andamentoRegioniLast"] = andamentoRegioniLast


    obj["vaccini"] = vaccini






    return render_template('index.html', title='Home', andamentoNazionaleLast=andamentoNazionaleLast[0], obj=obj, chartData = objChart)