class Config:
    # Flask configurations
    DEBUG = False
    SWAGGER = {
        'title': 'My API',
        'uiversion': 3,
        'openapi': '3.0.2',
        'specs': [
            {
                'endpoint': 'api',
                'route': '/apispec.json',
                'rule_filter': lambda rule: True,  # all in
                'model_filter': lambda tag: True,  # all in
            }
        ]
    }
    # ... other config settings