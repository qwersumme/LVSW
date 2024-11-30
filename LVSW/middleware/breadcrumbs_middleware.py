# middleware/breadcrumbs_middleware.py
from django.urls import resolve

class BreadcrumbsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Erzeuge Breadcrumbs basierend auf der URL
        path = request.path.strip('/').split('/')
        breadcrumbs = [{'name': segment, 'url': '/' + '/'.join(path[:i+1])} for i, segment in enumerate(path)]
        
        # An den Request anhängen
        request.breadcrumbs = breadcrumbs
        response = self.get_response(request)
        return response
