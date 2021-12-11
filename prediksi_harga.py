# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:06:27 2021

@author: W A Geraldine
"""
import pickle
import numpy as np
import pandas as pd
from keras.models import load_model

def prediksiHarga(rentangHarga):
    scalerfile = 'scaler.sav'
    scaler = pickle.load(open(scalerfile, 'rb'))
    filename = 'model_prediksi_harga_pangan.h5'
    best_model = load_model(filename)
    harga_scaler = np.fromfile('harga_scaler.dat', dtype=float)
    harga_scaler = np.reshape(harga_scaler, (-1, 1))
    
    n_future = rentangHarga
    future = [[harga_scaler[-1,0]]]
    X_new = harga_scaler[-30:,0].tolist()
    
    for i in range(n_future):
        y_future = best_model.predict(np.array([X_new]).reshape(1,30,1))
        future.append([y_future[0,0]])
        X_new = X_new[1:]
        X_new.append(y_future[0,0])
    
    future = scaler.inverse_transform(np.array(future))
    
    date_future = pd.date_range(start=np.datetime64('2021-12-11'), periods=n_future+1, freq='D')
        
    return future[-1]
