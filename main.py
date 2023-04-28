from registro import Registro



if __name__ == '__main__':
    lista = Registro('', '', '')
    lista.escribirarchivo()
    lista.crear()
    lista.cargar()
    lista.mostrarregistro()
    aux = int(input("Ingrese un dia"))
    lista.buscar(aux)
    lista.mostrarmatriz()