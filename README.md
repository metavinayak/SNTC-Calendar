## GYMKHANA Calendar

__Installing and running__

Clone the repository

Add  `ALLOWED_HOSTS` in `mycalendar/settings.py` for deployment

### Install virtual environment

Install **pip** first

    sudo apt-get install python3-pip

Then install **virtualenv** using pip3

    pip3 install virtualenv 

Now create a virtual environment

    virtualenv venv 

>you can use any name insted of **venv**

Active your virtual environment:

    source venv/bin/activate

Run the following commands in project directory.

You might need to delete **db.sqlite3** to start afresh.

```bash
pip install -r requirements.txt
python manange.py makemigrations
python manage.py migrate --run-syncdb
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```


### Adding Google OAuth2.0 API Key's credentials in admin Social Applications.
1. create a Google Cloud Console Project.
2. Go to Credentials, Auth consent, add a new app.
3. Create new OAuth Credentials and download the json.
![](./resources/gcp.png)

4. Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and sign in as superuser.
5. Add a new `Site`.
6. Add the `Social Applications` and the credentials and the site.
7. You are ready to run the App!

For running the web-app on the server as a background process, use **nohup**.
```bash
nohup python manage.py runserver &  
```
This will output a *PID*, which can be later used to kill the process.