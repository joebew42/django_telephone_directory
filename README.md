django_telephone_directory(1)
====================

This is a sample of a KISS/DRY web application based upon [Django framework] (https://www.djangoproject.com/). You can use this application as a skeleton for build other web application or to study how django works.
Which features of django are included in this simple project? Form handling and validation (with regular expressions), basic templates system (with extentions) and  URLs reverse matching (for a well urls handling within application). No extra applications or features were used (such us: admin, site, session, auth or localization), but feel free to enable them and discover how they works.

How to install and run it
====================
Simply, you have to install the latest django framework. After that, download and extract this project, enter the directory and execute this command **python manage.py runserver**. By default a development server will listen at localhost:8000. You can chek how the application works by inserting *localhost:8000/address_book/* in the URL address bar of your browser. Enjoy!

Configure MySQL Database
---------------------
This project uses a MySQL database to storing data. You have to set up a new database and a new user in your MySQL installation, and then update the information in the setting file that is located at *django_telephone_directory/settings.py*

> DATABASES = {
>     'default': {
>         'ENGINE': 'django.db.backends.mysql',
>         'NAME': 'django_telephone',
>         'USER': 'django',
>         'PASSWORD': 'django',
>         'HOST': '',
>         'PORT': '',
>     }
> }

