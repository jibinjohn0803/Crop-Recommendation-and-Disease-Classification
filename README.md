## Crop Recommendation and Disease Classification
This is a project to classify various crop diseases and recommend crops based on soil contents and temperature.

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. Maximize Crop Yield Using AI.ipynb - This contains code for development/training of Machine Learning models and saving it for further use.
2. app.py - This contains Flask APIs that receives crop details through GUI, computes the precited value based on our model and returns it.
4. templates - This folder contains the HTML template to allow user to enter crop details (images as well) to predict ideal crop (or disease identification for images).

### Running the project
As the trained model is already saved in the repository , the model can be downladed in the location where you intend to run this code. After which you will need to do following things:

1. Run app.py using below command to start Flask API (in Pycharm)
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage, enter the details and see the results.

Enjoy!!
