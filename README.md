django-bootstrap
================

Description
-----------
Boilerplate of a simple [Django](https://www.djangoproject.com/) new-project with [Bootstrap](http://twitter.github.com/bootstrap/), a sleek, intuitive, and powerful front-end framework for faster and easier web development.

Requirements
------------
To use it, you need to install a django valid version (v1.4+ recommended). This can be done by:

        pip install django

To check your current version of django, do the following on an open terminal:

        python
        >>> import django
        >>> django.VERSION
        
For running the project, open a terminal window in django-bootstrap's folder and type the following commands:

        cd my_project
        python manage.py runserver
        
Use "ctrl+c" to exit server mode.

Another useful commands:

* Create a database based on your models.

            python manage.py syncdb
        
Apps
----
This is an overview of the different basic apps included in the project. The objective is to have the most used apps already implemented and just adapt them to the project-specific requirements.

### contact_app
Simple version of a contact section which is based on forms and sends an email.
STMP must be present to send the emails.

### my_app
        
About
-----
Any contribution is welcome to improve this project.
