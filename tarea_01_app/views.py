from django.shortcuts import render
#from tarea_01_app.models import Personaje, Capitulo, Frase
import requests
import operator
from datetime import datetime


def get_temporadas(request):
    temporadas_bb = set()
    temporadas_bcs = set()

    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    response = requests.get(url)
    capitulos = response.json()

    for i in capitulos:
        if i['series'] == "Breaking Bad":
            temporadas_bb.add(i['season'])
        elif i['series'] == "Better Call Saul":
            temporadas_bcs.add(i['season'])

    temporadas_bb_sort = sorted(list(temporadas_bb))
    temporadas_bcs_sort = sorted(temporadas_bcs)

    return render(request, 'series/serie.html', {"temporadas_bb": temporadas_bb_sort,
                                                      "temporadas_bcs": temporadas_bcs_sort})


def listado_capitulos(request, id_serie, n_temp):
    capitulos_necesarios = set()
    real = {}
    url = ''
    if id_serie == 1:
        url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad'
    elif id_serie == 2:
        url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul'
    response = requests.get(url)
    capitulos = response.json()

    for i in capitulos:
        if i['season'] == str(n_temp):
            capitulos_necesarios.add(i['episode_id'])
            #real[i['episode_id']] = i
            real[i['episode_id']] = "Capitulo " + str(i['episode']) + " - " + str(i['title'])
            #real[i['episode_id']]['title'] = real[i['episode_id']]['title'].replace(' ', '_')

    real_ord = dict(sorted(real.items()))

    nombre_serie = ""
    if id_serie == 1:
        nombre_serie = "Breaking Bad"
    elif id_serie == 2:
        nombre_serie = "Better Call Saul"

    return render(request, 'series/listado_capitulos.html', {'nombre_serie': nombre_serie,
                                                             'data_capitulos': real_ord, 'n_temp': n_temp})


def detalle_capitulo(request, id):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/' + str(id)
    response = requests.get(url)
    capitulo = response.json()
    capitulo_ordenado = {}
    personajes = {}
    fecha, hora = capitulo[0]['air_date'].split('T')
    hora_2, extra = hora.split('.')
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    fecha_arreglada = fecha_dt.strftime('%d %B %Y')

    capitulo_ordenado['series'] = capitulo[0]['series']
    capitulo_ordenado['title'] = capitulo[0]['title']
    capitulo_ordenado['season'] = capitulo[0]['season']
    capitulo_ordenado['episode'] = capitulo[0]['episode']
    capitulo_ordenado['air_date'] = fecha_arreglada + " , " + hora_2 + " hrs."
    capitulo_ordenado['characters'] = capitulo[0]['characters']

    return render(request, 'series/detalle_capitulo.html', capitulo_ordenado)


def personaje(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        if not nombre:
            return render(request, 'series/detalle_personaje.html', {'capitulo': 'a'})
        else:
            nombre_bueno = nombre.replace('%20', " ")
            nombre_busqueda = nombre_bueno.replace(' ', "+")

            url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + str(nombre_busqueda)
            response = requests.get(url)
            info_personaje = response.json()

            url_2 = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=' + str(nombre_busqueda)
            response_2 = requests.get(url_2)
            frases = response_2.json()

            solo_frases = []
            for c_frase in frases:
                solo_frases.append(c_frase['quote'])

            info_personaje[0]['frases'] = solo_frases

            return render(request, 'series/detalle_personaje.html', info_personaje[0])


def buscar_personaje(request):
    #if 'name' in request.GET:
    #    nombre_a_buscar = request.GET.get('name')
    if request.method == 'GET':
        nombre = request.GET['name']
        #if not nombre:
            #return render(request, 'series/personajes.html', {'capitulo': 'a'})
        #else:

        data_personajes = {}
        contador_a = len(data_personajes)
        activar = True
        while activar:
            url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + str(nombre)\
                  + '&limit=10&offset=' + str(contador_a)
            response = requests.get(url)
            personajes = response.json()
            cant_p_a = len(data_personajes)
            for i in personajes:
                data_personajes[i['char_id']] = {'img': i['img'], 'name': i['name']}
                contador_a += 1
            cant_p_b = len(data_personajes)
            if cant_p_a == cant_p_b:
                activar = False

        return render(request, 'series/personajes.html', {"data_personajes" : data_personajes})
