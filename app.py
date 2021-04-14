import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    """int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    """
    price=request.form['presentprice']
    km=request.form['km']
    owner=request.form['pastowner']
    age=request.form['Age']
    fual=request.form['Fual_type']
    seller=request.form['Seller_type']
    Transmission=request.form['Transmission']
    
    if fual=="Diesel" and seller=="Individual" and  Transmission=="Manual":
        final_feature=[[price,km,owner,age,1,0,1,1]]
        prediction=model.predict(final_feature)

    if fual=="Diesel" and seller=="Individual" and  Transmission=="Auto":
        final_feature=[[price,km,owner,age,1,0,1,0]]
        prediction=model.predict(final_feature)

    if fual=="Petrol" and seller=="Individual" and  Transmission=="Manual":
        final_feature=[[price,km,owner,age,0,1,1,1]]
        prediction=model.predict(final_feature)
    
    if fual=="Petrol" and seller=="Individual" and  Transmission=="Auto":
        final_feature=[[price,km,owner,age,0,1,1,0]]
        prediction=model.predict(final_feature)

    if fual=="CNG" and seller=="Individual" and  Transmission=="Manual":
        final_feature=[[price,km,owner,age,0,0,1,1]]
        prediction=model.predict(final_feature)
    if fual=="CNG" and seller=="Individual" and  Transmission=="Auto": 
        final_feature=[[price,km,owner,age,0,0,1,0]]
        prediction=model.predict(final_feature)

    if fual=="Diesel" and seller=="Dealer" and  Transmission=="Manual":
        final_feature=[[price,km,owner,age,1,0,0,1]]
        prediction=model.predict(final_feature)

    if fual=="Diesel" and seller=="Dealer" and  Transmission=="Auto":
        final_feature=[[price,km,owner,age,1,0,0,0]]
        prediction=model.predict(final_feature)  

    if fual=="Petrol" and seller=="Dealer" and  Transmission=="Manual":
        final_feature=[[price,km,owner,age,0,1,0,1]]
        prediction=model.predict(final_feature)

    if fual=="Petrol" and seller=="Dealer" and  Transmission=="Auto":
        final_feature=[[price,km,owner,age,0,1,0,0]]
        prediction=model.predict(final_feature)  

    if fual=="CNG" and seller=="Dealer" and  Transmission=="Manual":
        final_feature=[[price,km,owner,age,0,0,0,1]]
        prediction=model.predict(final_feature)

    if fual=="CNG" and seller=="Dealer" and  Transmission=="Auto": 
        final_feature=[[price,km,owner,age,0,0,0,0]]
        prediction=model.predict(final_feature)


    return render_template('index.html', prediction_text='car selling price will be  {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
