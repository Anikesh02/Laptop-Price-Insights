from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
with open('laptop_prices_model.h5','rb') as f:
    model=pickle.load(f)
with open('scalar.h5','rb') as f:
    scalar=pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=request.form.to_dict()
    features=np.zeros(shape=(51,))
    features[0]=float(data['Inches'])
    features[1]=float(data['Ram'])
    features[2]=float(data['weight'])
    if data['company']=='Acer':
        features[3]=1
    if data['company']=='Apple':
        features[4]=1
    if data['company']=='Asus':
        features[5]=1
    if data['company']=='Chuwi':
        features[6]=1
    if data['company']=='Dell':
        features[7]=1
    if data['company']=='Fujitsu':
        features[8]=1
    if data['company']=='Google':
        features[9]=1
    if data['company']=='HP':
        features[10]=1
    if data['company']=='Huawei':
        features[11]=1
    if data['company']=='LG':
        features[12]=1
    if data['company']=='Lenovo':
        features[13]=1
    if data['company']=='MSI':
        features[14]=1
    if data['company']=='Mediacom':
        features[15]=1
    if data['company']=='Microsoft':
        features[16]=1
    if data['company']=='Razer':
        features[17]=1
    if data['company']=='Samsung':
        features[18]=1
    if data['company']=='Toshiba':
        features[19]=1
    if data['company']=='Vero':
        features[20]=1
    if data['company']=='Xiaomi':
        features[21]=1
    if data['cpu_company']=='AMD':
        features[22]=1
    if data['cpu_company']=='Intel':
        features[23]=1
    if data['cpu_company']=='Samsung':
        features[24]=1
    features[25]=float(data['cpu_speed'])
    if data['gpu']=='AMD':
        features[26]=1
    if data['gpu']=='ARM':
        features[27]=1
    if data['gpu']=='Intel':
        features[28]=1
    if data['gpu']=='Nvidia':
        features[29]=1
    features[30]=float(data['memory_flash'])
    features[31]=float(data['memory_hdd'])
    features[33]=float(data['memory_hybrid'])
    features[32]=float(data['memory_ssd'])
    if data['opsys']=='Android':
        features[34]=1
    if data['opsys']=='Chrome OS':
        features[35]=1
    if data['opsys']=='Linux':
        features[36]=1
    if data['opsys']=='Mac OS X':
        features[37]=1
    if data['opsys']=='No OS':
        features[38]=1
    if data['opsys']=='Windows 10':
        features[39]=1
    if data['opsys']=='Windows 10 S':
        features[40]=1
    if data['opsys']=='Windows 7':
        features[41]=1
    if data['opsys']=='macOS':
        features[42]=1
    features[43]=float(data['screen_height'])
    features[44]=float(data['screen_width'])
    if data['typename']=='2 in 1 Convertible':
        features[45]=1
    if data['typename']=='Gaming':
        features[46]=1
    if data['typename']=='Netbook':
        features[47]=1
    if data['typename']=='Notebook':
        features[48]=1
    if data['typename']=='Ultrabook':
        features[49]=1
    if data['typename']=='Workstation':
        features[50]=1
    features=scalar.transform([features])
    prediction=model.predict(features)[0]
    return render_template('index.html',prediction=f'{prediction:.2f}')

app.run()