# gunicorn -w 4 -b '0.0.0.0:80' wsgi:application
# gunicorn wsgi:application
# nohup gunicorn  -b 0.0.0.0:80 wsgi:app &

from app import configure_app
# from app import configure_manager
# from app import manager

application = configure_app()

# if __name__ == '__main__':
#     configure_manager()
#     application
#     manager.run()       # 命令行