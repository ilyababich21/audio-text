from django.urls import path, re_path
from . import views

app_name='audio'

urlpatterns = [
    path('export_doc',views.export_doc, name='export_doc'),
    path('make_text/',views.make_text, name='make_text'),
    path('', views.home_page)


]
