## Application and routes

- In django we create sub applicatin within a application, by using command : `python manage.py startapp appname`
- The routing of application happens from `urls.py` file
- We match the url by linking the path from the project to route


## How to link the path of new app

- We need to import the `include` function from `django.urls`
- The path which I need to include from the app should be added in `urlpatters`
```python
path('routeName/', include('appname.urls'))
```

for example, we need create route `/blog`
```python
path('blog/', include('blog.urls'))
```

- Now in our sub app folder we need to create new file `views`, where we'll define our function which will be called when the url is hit by user.
- And also we need to call that fuction using path in `urls.py` file of our sub app

Example:

- `views.py` in `blog` 
```python
def home(request):
    return HttpResponse("<h1> This is blog home page</h1>")
```

- `urls.py` in `blog`
```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "blog-home"),
]
```