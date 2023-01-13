
This is a E-commerce backend made with django and DRF. 
Libraries used in it.

simple_jwt: for token authentication.
redis     : for cacheing

Installation:

. clone repo 
>> git clone <repo link>

. create virtual env. 
>> pip install -r requirements.txt

.run migrations
>> python manage.py makemigrations 
>> python manage.py migrate

. create superuser
>> python manage.py createsuperuser

