from django.shortcuts import render

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.padre = None

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def en_lista(self, lista):
        return any(self.datos == n.datos for n in lista)

def buscar_solucion_BFS(conexiones, inicio, destino):
    visitados = []
    frontera = [Nodo(inicio)]

    while frontera:
        nodo = frontera.pop(0)
        visitados.append(nodo)

        if nodo.get_datos() == destino:
            return nodo

        for vecino in conexiones.get(nodo.get_datos(), []):
            hijo = Nodo(vecino)
            hijo.set_padre(nodo)

            if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                frontera.append(hijo)

    return None

def index(request):
    resultado = None

    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Queretaro': {'Zacatecas', 'Sinaloa', 'Jiloyork'}
    }

    if request.method == "POST":
        inicio = request.POST.get("inicio")
        destino = request.POST.get("destino")

        nodo = buscar_solucion_BFS(conexiones, inicio, destino)

        resultado = []
        while nodo and nodo.get_padre():
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        if nodo:
            resultado.append(inicio)
            resultado.reverse()

    return render(request, "index.html", {"resultado": resultado})
