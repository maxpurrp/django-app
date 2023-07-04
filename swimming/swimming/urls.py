from django.urls import path
from main import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.base),
    path('home', views.base),
    path('about_swimming', views.about_swimming),
    path('about_me', views.about_me),
    path('reg_for_training', views.registration),
    path('admin', admin.site.urls),
    path('workout_gym', views.workout_gym),
    path('workout_swimming', views.workout_swimming),
    path('workout_swimming_pro', views.workouts_swimming_pro),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)