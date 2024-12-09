from guitar_pedals.wsgi import application
import awsgi

def handler(event, context):
    # Add debug logging
    print('Received event:', event)
    
    # Handle both /api and non-api routes
    if event.get('path', '').startswith('/.netlify'):
        event['path'] = event['path'].replace('/.netlify/functions/django', '')
    
    # Ensure path is not empty
    if not event.get('path'):
        event['path'] = '/'

    return awsgi.response(application, event, context)
