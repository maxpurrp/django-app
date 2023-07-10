# How to install
1. Install venv for your OS
	Linux / MacOS
 ```sudo apt install -y python3-venv```
	 Windows
 ```python -m pip install virtualenv```
 2. Creating a virtual environment Linux / MacOS  ```python3 -m venv env```  
 Windows  ```py -m venv env```
 3. Activating a virtual environment Linux / MacOS ```source env/bin/activate``` 
 Windows ```env\Scripts\activate```
 4. Install all modules from requirements.txt ```pip install -r requirements.txt```
 5. Run server  ```python manage.py runserver```
# Docker
1. Clone the repository ```git clone https://github.com/maxpurrp/django-app```
2. Type in console ```cd django-app\swimming && docker-compose up```
3. You can visit your application at http://localhost:8000/
