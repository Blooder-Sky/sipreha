from flask import Flask, render_template, request
#we are importing the function that makes predictions.
from datetime import date

from prediksi_harga import prediksiHarga

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        tanggal_prediksi = request.form['tanggal']
        tanggal_awal = date(2021, 11, 12)
        tanggal_prediksi = date(int(tanggal_prediksi[0:4]), int(tanggal_prediksi[5:7]), int(tanggal_prediksi[8:10]))
        rentang_hari = (tanggal_prediksi - tanggal_awal)
        rentang_hari = int(rentang_hari.days)
        
        harga = prediksiHarga(rentang_hari)
        harga = round(harga[0])           
        results = []
        answer = str(harga)
        results.append(answer)
        return render_template('index.html', len=len(results), results=results)


                        
#here we are setting the port. 
def main():
    app.run()
    

# Create a running list of result
results = []

# Launch Everyting
main()