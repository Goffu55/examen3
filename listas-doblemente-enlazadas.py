class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class listaDoblementeEnlazada:
    def __init__(self):
        self.start_node = None
    
    def insertar_a_listaVacia(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("la lista no está vicía")

    def insertar_al_inicio(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("nodo insetrado")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
    
    def insertar_al_final(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insertar_despues_del_elemento(self, x, data):
        if self.start_node is None:
            print("la lista está vacía")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("el elemento no está en la lista")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node
        
    def insertar_antes_del_elemento(self, x, data):
        if self.start_node is None:
            print("la lista está vacía")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("el elemento no está en la lista")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node
    def atravezar_lista(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref

    def eliminar_elemento_del_inicio(self):
        if self.start_node is None:
            print("Esta lista no tiene elementos para eliminar")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None
    
    def eliminar_elemento_del_final(self):
        if self.start_node is None:
            print("Esta lista no tiene elementos para eliminar")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
    
    def eliminar_un_elemento_dado(self, x):
        if self.start_node is None:
            print("Esta lista no tiene elementos para eliminar")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("elemento no encontrado")
            return 

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def invertir_lista(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

lista = listaDoblementeEnlazada()

print("ingresar el primer dato de su lista dato a la lista")
PrimDato=input()
print("ingresar un dato entre el primer y ultimo dato de su lista")
insterDato=input()
print("insterte un numero de referencia dentro de su lista")
Ref1Dato=input()
print("ingrese el dato que quiere que vaya Despues del dato anterior:" + Ref1Dato)
DespDato=input()
print("insterte un numero de referencia dentro de su lista")
Ref2Dato=input()
print("ingrese el dato que quiere que vaya Antes del dato anterior:" + Ref2Dato)
AntDato=input()
print("ingrese el ultimo dato de su lista")
UltDato=input()

# print("insertar a la lista viacía")
lista.insertar_a_listaVacia(insterDato)
# print("insertar al inicio de la lista")
lista.insertar_al_inicio(PrimDato)
# print("insertar despues del siguiente elemento")
lista.insertar_despues_del_elemento(Ref1Dato,DespDato)
# print("insertar antes del siguiente elemento")
lista.insertar_antes_del_elemento(Ref2Dato,AntDato)
# print("insertar al final de la lista")
lista.insertar_al_final(UltDato)
print("su lista es:")
lista.atravezar_lista()

print("desea eliminar un dato? Responda Si o No")
QeliminarDato = input() 
if QeliminarDato == 'si' or QeliminarDato == 'Si' or QeliminarDato == 'no' or QeliminarDato == 'No':
    if QeliminarDato == 'si' or QeliminarDato == 'Si':
        print("ingrese el numero a eliminar")
        elimDato = input()
        lista.eliminar_un_elemento_dado(elimDato)
        print("el dato:" + elimDato + " " + "fue eliminado")
        lista.atravezar_lista()
    if QeliminarDato == 'no' or QeliminarDato == 'No':
        print("no se borró ningún dato")
else:
    print("valor no reconocido")


print("desea invertir la lista? Responda Si o No")
QeliminarDato = input() 
if QeliminarDato == 'si' or QeliminarDato == 'Si' or QeliminarDato == 'no' or QeliminarDato == 'No':
    if QeliminarDato == 'si' or QeliminarDato == 'Si':
        print("invertir la lista doblemente enlazada")
        lista.invertir_lista()
        lista.atravezar_lista()
else:
    print("valor no reconocido")




