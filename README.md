# Car-Price-Prediction

# Bussiness Goal

We are required to model the price of cars with the available independent variables. It will be used by the management to understand how exactly the prices vary with the 
independent variables. They can accordingly manipulate the design of the cars, the business strategy etc. to meet certain price levels. Further, the model will be a good way
for management to understand the pricing dynamics of a new market.

# Dataset 
You can download the dataset from here - https://www.kaggle.com/hellbuoy/car-price-prediction

# Kaggle notebook 

complete EDA and modelling - https://www.kaggle.com/yashvi/car-price-prediction-eda-rfe-with-random-forest

# STEPS 

1. created a flask application
2. containerise the flask application using Docker and test locally

  2.1 for building docker images , run the following command 
  
        docker build -t image_name:version .
        
  2.2 for running docker image locally,
  
        docker run -d -p 5000:5000 image_name:version
        
3. Deploy the container to Heroku
 
        heroku login
        
        heroku container:login
        
        heroku create your_app_name
        
        heroku container:push web --app your_app_name
 
        heroku container:release web --app your_app_name
  
  # My heroku app link 
  https://car-price-pred-app-29.herokuapp.com
  

