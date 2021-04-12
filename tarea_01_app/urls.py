from django.urls import  path
from tarea_01_app import views

urlpatterns = [
    path('', views.get_temporadas, name = "get_temporadas"),
    path('serie/<int:id_serie>/temporada/<int:n_temp>', views.listado_capitulos, name = "listado_capitulos"),
    path('detalle_capitulo/<int:id>', views.detalle_capitulo, name = "detalle_capitulo"),
    path(r'personaje/', views.personaje, name = "personaje"),
    path(r'personajes/', views.buscar_personaje, name = "buscar_personaje"),

    #serie/{{'1'}}/temporada/{{temp}}
    # path('meals/<int:id>/',views.meal_detail, name = "meal_detail")
    #path('series/listado_capitulos/<int:id>/', views.listado_capitulos, name = "listado_capitulos")
]