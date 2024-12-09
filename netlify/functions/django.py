from guitar_pedals.wsgi import application
import awsgi

def handler(event, context):
    return awsgi.response(application, event, context)
