from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('measurements/', views.MeasurementList),
    path('measurementcreate/', csrf_exempt(views.MeasurementCreate), name='measurementCreate'),
    path('createmeasurements/', csrf_exempt(views.MeasurementsCreate), name='createMeasurements'),
]