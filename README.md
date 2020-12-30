# Dropbox
A dropbox type utility with user authentication where you can upload documents by clicking on the upload link.
## Project Setup Guide:
- Clone the repository
- Make a `pip install -r requirements.txt` (after going into the required directory)  to install all the requirements/dependencies preferably setup a virtual environment and then do it. 
(**Note**- Your system must have python installed preferably python 3.7.6)
- **Deletions**- Now you will have to delete few files and folders namely `db.sqlite3`, all the previousely uploaded files in `media/users` folder, `__pycache__` and `migrations` inside users folder and finally `__pycache__` inside the `dropbox` folder. Doing these deletions you can freshly setup the project.
- Now afer going to the project folder, you will have to run a few migrations to make the specific tables in the database so run the following commands in terminal:      
 `python manage.py migrate`     
 `python manage.py makemigrations users`     
 `python manage.py migrate`  
- **Creating superuser**- This will give you the access to the admin page of the website. To make a superuser run `python manage.py createsuperuser` in the terminal and specify the details.
- Now you are good to go! Finally run `python manage.py runserver` to run the django server.
- Check out the demo [video](https://youtu.be/AQ3hwDn2vjw) to see the various functionalities.
