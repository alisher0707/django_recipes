from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path() is passed route and view (and kwargs and name are optional)
    # the route is the end of the url (minus GET/POST params)
    # django calls the specified view function with an HttpRequest obj and captured values from url as args
    # name is so we can refer to it in templates in our project
    path('', include('book.urls')), # include lets us reference the other url modules! use it for everything 
    path('admin/', admin.site.urls),
]
