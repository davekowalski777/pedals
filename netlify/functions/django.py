from guitar_pedals.wsgi import application
from netlify_lambda_wsgi import make_aws_lambda_wsgi_handler

handler = make_aws_lambda_wsgi_handler(application)
