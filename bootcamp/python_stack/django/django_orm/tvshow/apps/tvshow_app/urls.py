from django.urls import path	 
from . import views



app_name = 'tvshow_app'

urlpatterns = [
    path('', views.To_shows, name='to_shows'),
    path('shows/', views.ShowList, name='show_list'), # LISTA DE TV-SHOWS
    path('shows/new/', views.ShowCreate, name='show_new'), # FORMULARIO PARA CREAR UN SHOW	   
    path('shows/create/', views.ShowCreate, name='show_create'), # PAGINA EN DONDE ES ENVIADA LA INFORMACION PARA GUARDARLA EN LA DB Y REDERIJIR A TV-SHOWS
    path('shows/<int:id>', views.ShowDetail, name='show_detail'), # PAGINA QUE MUESTRA LA INFORMACION DEL SHOW
    path('shows/<int:id>/edit',views.ShowUpdate, name='show_edit'), # PAGINA QUE MUESTRA EL FORMULARIO DE NEW CON LA INFORMACION PARA PODER EDITARLA 	   	   
    path('shows/<int:id>/update',views.ShowUpdate, name='show_update'), # PAGINA QUE ES ENVIADA LA INFORMACION EDITADA Y REDERIJIR A LISTA DE SHOWS	   	   
    path('shows/<int:id>/destroy',views.ShowDelete, name='show_delete'),	# PAGINA QUE ELIMINA UN SHOW DE LA DB Y REDERIJE A LISTA DE SHOWS   	   
]