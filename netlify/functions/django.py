from guitar_pedals.wsgi import application
from netlify_wsgi import handler

def handle(event, context):
    return handler(event, context, application)
