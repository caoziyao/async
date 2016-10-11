# gunicorn -w 4 -b '0.0.0.0:80' wsgi:application
# gunicorn wsgi:application
# nohup gunicorn -b '0.0.0.0:80' wsgi:application &

import app 

application = app.configure_app()