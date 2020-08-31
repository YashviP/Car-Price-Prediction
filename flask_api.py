from flask import Flask,request, url_for, redirect, render_template
import numpy as np
import pickle
import os
import pandas as pd
import flasgger

app=Flask(__name__)
port = int(os.environ.get("PORT", 5000))

pickle_in = open("car_model.pkl","rb")
car_model=pickle.load(pickle_in)


@app.route('/')
def welcome():
	 return render_template("home.html")

@app.route('/predict',methods=["POST"])
def predict():
	features= [x for x in request.form.values()]
	print(features)
	carbody=features[0]
	if carbody=="sedan":
		carbody=3
	elif carbody=="hatchback":
		carbody=2
	elif carbody=="wagon":
		carbody=4
	elif carbody=="hardtop":
		carbody=1
	elif carbody=="convertible":
		carbody=0
	features[0]=carbody
	fuelsystem=features[7]
    
	if fuelsystem=="mpfi":
		fuelsystem=5
	elif fuelsystem=="2bbi":
		fuelsystem=1
	elif fuelsystem=="idi":
		fuelsystem=3
	elif fuelsystem=="1bbi":
		fuelsystem=0
	elif fuelsystem=="spdi":
		fuelsystem=6
	elif fuelsystem=="4bbl":
		fuelsystem=2
	elif fuelsystem=="mfi":
		fuelsystem=7
	elif fuelsystem=="spfi":
		fuelsystem=4
	features[7]=fuelsystem
	
	features =  [float(x) for x in features]
	prediction=float(car_model.predict([features]))
	print(prediction)
	return render_template('home.html',pred='Expected Price will be {}'.format(prediction))
	                								   	
 	  
if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0',port=port)
    
