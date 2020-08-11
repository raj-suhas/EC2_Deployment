# EC2_Deployment
This repository contains basic ML Iris dataset Classifier application that has been deployed on AWS EC2 instance.
## Steps to deploy ML application on EC2

1. Create and train ML model in your local machine.
2. Save the model as Pickle file.
3. Create html template to create web interface. (Note: save the html file inside templates folder)
4. Develop Flask code to load model and connect to template.
5. Run and check in local.
6. Run AWS Console and create an EC2 instance.
7. Transefer the following files into EC2 file system. (templates, app.py, model.pkl, requirements.txt)
8. Connect to EC2 instance and update pip3 package installer. (sudo apt-get update && sudo apt-get install python3-pip)
9. Install all the required packages mentioned in requirements.txt. (pip3 install -r requirements.txt)
10. Update the port in app.py.
11. Run the flask file. (python3 app.py)
12. Check the url&port and vevrify it.
