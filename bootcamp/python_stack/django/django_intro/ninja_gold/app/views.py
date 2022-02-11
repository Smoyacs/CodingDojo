from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
    # si no esta en la sesion se normaliza el valor a 0 y se crea un regristro de actividad dentro de una lista
    if 'oro_total' not in request.session:
        request.session['oro_total'] = 0
        print("Oro total = 0")
        request.session['registro_actividad'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == "POST":
        print("*"*25, "Se encuentra en el metodo process_money", "*"*25)

        # Informacion obtenida del formulario
        if request.POST['construccion'] == 'granja':
            request.session['mensaje'] = ''
            num = random.randrange(10,21)
            time = datetime.now().time()
            request.session['oro_total'] += num
            print(f"Oro es incrementado en {num}.")
            print(f"Oro total = {request.session['oro_total']}")
        
            # Registro de actividad
            temp_list = request.session['registro_actividad']
            temp_list.append(f"<div class='ganador'>Gano {num} oro de la Granja! ---- ({time})</div>")
            request.session['registro_actividad'] = temp_list

            for i in range(len(request.session['registro_actividad'])-1, -1, -1):
                request.session['mensaje'] += request.session['registro_actividad'][i]
                
            # Contenido de la sesion
            print("\nContenido de la sesion:")
            for val in request.session.keys():
                print("\n", val, request.session[val])
            print("*"*25, "Termindo el metodo process money", "*"*25)


        # Informacion obtenida del formulario
        elif request.POST['construccion'] == 'cueva':
            request.session['mensaje'] = ''
            num = random.randrange(5,11)
            time = datetime.now().time()
            request.session['oro_total'] += num
            print(f"Oro es incrementado en {num}.")
            print(f"Oro total = {request.session['oro_total']}")
            
            # Registro de actividad
            temp_list = request.session['registro_actividad']
            temp_list.append(f"<div class='ganador'>Gano {num} oro de la Cueva! ---- ({time})</div>")
            request.session['registro_actividad'] = temp_list

            for i in range(len(request.session['registro_actividad'])-1, -1, -1):
                request.session['mensaje'] += request.session['registro_actividad'][i]
            
            # Contenido de la sesion
            print("\nContenido de la sesion:")
            for val in request.session.keys():
                print("\n", val, request.session[val])
            print("*"*25, "Termindo el metodo process money", "*"*25)

        # Informacion obtenida del formulario
        elif request.POST['construccion'] == 'casa':
            request.session['mensaje'] = ''
            num = random.randrange(2,6)
            time = datetime.now().time()
            request.session['oro_total'] += num
            print(f"Oro es incrementado en {num}.")
            print(f"Oro total = {request.session['oro_total']}")
            
            # Registro de actividad
            temp_list = request.session['registro_actividad']
            temp_list.append(f"<div class='ganador'>Gano {num} oro de la Casa! ---- ({time})</div>")
            request.session['registro_actividad'] = temp_list

            for i in range(len(request.session['registro_actividad'])-1, -1, -1):
                request.session['mensaje'] += request.session['registro_actividad'][i]
                
            # Contenido de la sesion
            print("\nContenido de la sesion:")
            for val in request.session.keys():
                print("\n", val, request.session[val])
            print("*"*25, "Termindo el metodo process money", "*"*25)

        # Informacion obtenida del formulario
        elif request.POST['construccion'] == 'casino':
            if request.session['oro_total'] > 0:
                request.session['mensaje'] = ''
                num = random.randrange(-50,51)
                time = datetime.now().time()
                request.session['oro_total'] += num
                if num > 0:
                    print(f"Oro es incrementado en {num}.")
                    
                    # Registro de actividad
                    temp_list = request.session['registro_actividad']
                    temp_list.append(f"<div class='ganador'>Gano {num} oro en el Casino! ---- ({time})</div>")
                    request.session['registro_actividad'] = temp_list
                if num < 0:
                    print(f"oro decreased by {abs(num)}.")
                    
                    # Registro de actividad
                    temp_list = request.session['registro_actividad']
                    temp_list.append(f"<div class='perdedor'>Perdio {abs(num)} oro en el casino ---- ({time})</div>")
                    request.session['registro_actividad'] = temp_list         
                print(f"Oro total = {request.session['oro_total']}") 

                for i in range(len(request.session['registro_actividad'])-1, -1, -1):
                    request.session['mensaje'] += request.session['registro_actividad'][i]
                    
                # Contenido de la sesion
                print("\nContenido de la sesion:")
                for val in request.session.keys():
                    print("\n", val, request.session[val])
                print("*"*25, "Termino el metodo process money", "*"*25)

            # Condicion: Si no tiene el oro suficiente no puede jugar
            elif request.session['oro_total'] <= 0:
                request.session['mensaje'] = ''
                
                # Registro de actividad
                temp_list = request.session['registro_actividad']
                temp_list.append(f"<div>No tienes oro para apostar. Vuelve al casino cuando tengas el dinero suficiente.</div>")
                request.session['registro_actividad'] = temp_list       
                print(f"Oro total = {request.session['oro_total']}")

                for i in range(len(request.session['registro_actividad'])-1, -1, -1):
                    request.session['mensaje'] += request.session['registro_actividad'][i]
                
                # Contenido de la sesion
                print("\nContenido de la sesion:")
                for val in request.session.keys():
                    print("\n", val, request.session[val])
                print("*"*25, "Termindo del metodo process money", "*"*25)

        return redirect("/")
    
    else:
        print("*"*25, "Metodo process money", "*"*25)
        return redirect("/")


def reset(request):
    print("*"*25, "Metodo Reset", "*"*25)
    
    # elimina la informacion de la sesion
    request.session.clear() 
    print("Contenido de la sesion:")
    
    # confirmacion de que no hay nada en la sesion
    for val in request.session.keys():
        print(val, request.session[val], "\n")
        
    print("*"*25, "Termino del metodo Reset", "*"*25)
    return redirect("/")