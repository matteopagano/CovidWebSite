#!/bin/sh


#cd /home/metiupaga/mysite/app/jsonFiles/dati
cd /home/metiupaga/mysite/app/jsonFiles/coviRepo/covidRepo/json/vaccini

wget -N https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.json .

#cd /home/metiupaga/mysite/app/jsonFiles/dati-json
cd /home/metiupaga/mysite/app/jsonFiles/coviRepo/covidRepo/json/andamento

wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json .
wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json .
wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-note.json .
wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json .
wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json .
wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json .
wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json .


