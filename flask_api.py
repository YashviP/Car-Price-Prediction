from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("car_model.pkl","rb")
car_model=pickle.load(pickle_in)
print(car_model)
@app.route('/')
def welcome():
	return "welcome all"

@app.route('/a',methods=["Get"])
def predict_note_authentication():
    
	"""Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters: 
      - name: carbody
        in: query
        type: string
        description: "enter your car body"
        enum: ["convertible","hatchback","sedan","wagon","hardtop"]
        required: true

      - name: wheelbase
        in: query
        type: number
        required: true

      - name: carlength
        in: query
        type: number
        required: true

      - name: carwidth
        in: query
        type: number
        required: true

      - name: carheight
        in: query
        type: number
        required: true
      
      - name: curbweight
        in: query
        type: number
        required: true

      - name: enginesize
        in: query
        type: number
        required: true

      - name: fuelsystem
        in: query
        type: string
        description: "enter fuel system"
        enum: ["mpfi","2bbi","idi","1bbi","spdi","4bbi","mfi","spfi"]
        required: true

      - name: boreratio
        in: query
        type: number
        required: true

      - name: stroke
        in: query
        type: number
        required: true

      - name: compressionratio
        in: query
        type: number
        required: true

      - name: horsepower
        in: query
        type: number
        required: true

      - name: peakrpm
        in: query
        type: number
        required: true

      - name: citympg
        in: query
        type: number
        required: true

      - name: highwaympg
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values
	""" 
	carbody=request.args.get("carbody")
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
	wheelbase=request.args.get("wheelbase")
	carlength=request.args.get("carlength")
	carwidth=request.args.get("carwidth")
	carheight=request.args.get("carheight")
	curbweight=request.args.get("curbweight")
	enginesize=request.args.get("enginesize")
	fuelsystem=request.args.get("fuelsystem")
    
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
   
	boreratio=request.args.get("boreratio")
	stroke=request.args.get("stroke")
	compressionratio=request.args.get("compressionratio")
	horsepower=request.args.get("horsepower")
	peakrpm=request.args.get("peakrpm")
	citympg=request.args.get("citympg")
	highwaympg=request.args.get("highwaympg")
    
	prediction=car_model.predict([[carbody,wheelbase,carlength,carwidth,carheight,curbweight,enginesize, 				fuelsystem,boreratio,stroke,compressionratio,horsepower,peakrpm,citympg,highwaympg]])
	print(prediction)
	return "Hello The answer is"+ str(prediction)
	                								   	
 	  
if __name__=='__main__':
	app.run()
    
