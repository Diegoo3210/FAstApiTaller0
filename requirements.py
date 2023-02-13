import os
from collections import Counter
import numpy as np
abs_path=os.path.dirname(__file__)

#Estilo: PEP8
def path_contructor(nombre="",path=None)->str:
    """
    Devuelve un path creado a partir de un nombre
    y path relativo.

    Argumentos:
    nombre  : nombre del file con extensión (si es "" este pide el nombre por consola)
    path  : path relativo de la file (si es None, pide el path relativo)

    """
    if path==None:
        path = input("Si el file esta en el mismo path relativo del script dejar en blanco \n"+
                            "(sin nombre del file y con / al final)\n" +
                            "Path ubicación del file :\n" )     
    if nombre=="":
        nombre = input('Nombre del file con extensión (ej: hola.txt): \n')

    fullpath=path+nombre
    path = os.path.join(abs_path, fullpath)
    return path
#print(path_contructor("hola.txt"))

def question_a(nombre:str)->int:
    """
    Devuelve la cantidad de words que hay 
    en el file {poner nombre del file}

    Argumentos:
    nombre  : nombre del file con extensión

    """
    path = path_contructor(nombre,"")
    file = open(path, "rt")
    data = file.read().lower()
    words = data.split()
    print('Numero de words :', len(words))
    return (len(words))

#question_a("hello.txt")
def question_b(nombre:str)->dict:
    """
    Devuelve el numero de veces que se repite cada palabra

    Argumentos:
    nombre  : nombre del file con extensión

    """
    path = path_contructor(nombre,"")
    rep_words = {}
    file = open(path, "rt")
    data = file.read().lower()
    words = data.split()
    for palabra in words:
        if palabra in rep_words:
            rep_words[palabra]+=1
        else:
            rep_words[palabra]=1
    return rep_words
#print(question_b("hello.txt"))

def question_cd(nombre:str, n=5)->list:
    """
    Devuelve el numero de veces que se repiten las N 
    words que más aparecen, devuelve una lista de 
    las palabras que más ocurrencia tienen junto a 
    las veces que ocurre

    Argumentos :
    nombre  : nombre del file con extensión

    Argumentos por consola:
    n : numero de words más frecuentes

    """
    #n  = input('Numero de words con mayor aparicion: \n')
    n= int(n)
    path = path_contructor(nombre,"")
    file = open(path, "rt")
    data = file.read().lower()
    words = data.split()
    counter = Counter(words)
    most_ocurr = counter.most_common(n)
    return most_ocurr

#print(question_cd("hello.txt"))

def question_ef(nombres: list)->list:
    """
    Funcion que devuelve las preguntas anteriores 
    para N files, en una lista desde la pregunta
    a hasta la d

    Argumentos :
    nombres  : lista de nombres de files

    """
    final_list=[]
    for i in range(len(nombres)):
        arr=[]
        arr.append(question_a(nombres[i]))
        arr.append(question_b(nombres[i]))
        arr.append(question_cd(nombres[i]))
        arr.append(question_cd(""))
        final_list.append(arr)
    return final_list

def question_g(nombres: list)->tuple:
    """
    Devuelve en cuál archivo aparece más veces 
    cierta palabra y cuál archivo tiene más 
    palabras, dentro de un grupo de X archivos 
    seleccionados como parámetro

    Argumentos :
    nombres  : lista de nombres de files

    """
    max_words=0
    index_maxwords=0
    for i in range(len(nombres)):
        if question_a(nombres[i])>max_words:
            max_words = question_a(nombres[i])
            index_maxwords=i
    palabra_buscar = input('Palabra a buscar: \n')
    word_file = []
    repetition = np.zeros(len(nombres))
    for i in range(len(nombres)):
        path = path_contructor(nombres[i])
        file = open(path, "rt")
        data = file.read().lower()
        words = data.split()
        word_file.append(words)
    for i in range(len(nombres)):
        for j in range(len(word_file[i])):
            if palabra_buscar == word_file[i][j]:
                repetition[i]+=1
    max_count=0
    index_max=0
    for i in range(len(repetition)):
        if repetition[i]>max_count:
            max_count = repetition[i]
            index_max=i
    return (max_count,index_max,max_words,index_maxwords)
#question_g(["hello.txt","adios.txt"])


print(question_a("./dataTesting/reut2-000.sgm"))