
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  SignUp , login_view,logout

app_name ="authentication"

urlpatterns = [

path('signup/', SignUp.as_view(), name='signup'),
path('login/', login_view, name='login'),
path('logout/', logout, name='logout'),





]

# for adding media file settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
