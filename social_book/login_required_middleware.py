from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Exclude paths that don't require authentication
        exempt_urls = [reverse('signup'), reverse('signin')]
        
        # Check if user is not authenticated and the path is not in the exempt list
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return HttpResponseRedirect(reverse('signup'))
        
        response = self.get_response(request)
        return response
