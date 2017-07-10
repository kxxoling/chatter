=======
Chatter
=======

Chatter is an open source chat application based on `Django Channels <https://github.com/django/channels/>`_.
Feel free to use an fork!


Pre-requirements
================

This is project based on Django Channels and Vue.js, so you need these technologies
installed before trying to run it on your own machine:

* Python 3;
* `pipenv` as Python environment manager is suggested, but `pip` is also accepted;
* SQLite3 as the database;
* Redis as Django Channles layer;
* Node.js and npm for Vue staff;


Run
===

1. Set up a clean Python environment: ``pipenv install``;
2. Install the frontend requirements: ``npm install``;
3. Start ASGI server for Django Channles layer: ``daphne chatter.asgi:channel_layer --port 8000``;
4. Start Django server for API requests: ``./manage.py runserver``;
5. Start Vue.js dev-server: ``npm run dev``;


Preview
=======

.. image:: https://raw.githubusercontent.com/kxxoling/chatter/master/chatter.png
