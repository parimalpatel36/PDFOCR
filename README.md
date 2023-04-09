# Steps to run server
### Step 1 (Get latest code)
##### Clone the repo: https://github.com/parimalpatel36/PDFOCR.git
### Step 3(Install system level dependencies)
#### For Linux
##### Install poppler
#
```
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```
### Step 4(Make virtual environment)
```
cd PDFOCR
python3 -m venv env
```
### Step 5(Activate virtual environment)
##### For Windows
#
```
cd PDFOCR
env\Scripts\activate
```
##### For Linux
#
```
cd PDFOCR
. env/bin/activate
```
### Step 6(Install requirements.txt)
##### We have to run below commands, when we want to restart server with new python dependencies.
#
```
pip install -r requirements.txt
```
##### Note: Make sure you have activate the virtual enviorment before running the above command
### Step 7(Apply latest migrations)
##### We have to run below command, when we have new database migrations changes.
#
```
python manage.py makemigrations
python manage.py migrate
```
##### Note: Make sure you have activate the virtual enviorment before running the above command
### Step 8(Run server)
##### Run below command to start, stop, restart and delete a server process with worker.
##### For Linux
#
```
python manage.py runserver
```

##### Open swagger doc using (http://localhost:8000/swagger)