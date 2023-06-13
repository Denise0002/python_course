# variables 

> es un espancion en memoria donde podemos alamcenar datos
cd ~/Documents/Projects
django-admin.py startproject FirstBlog
cd FirstBlog
ls -*- coding: utf-8 -*-
def application(environ, start_response):
    if environ["PATH_INFO"]=="/":
        respuesta = "<p>Página inicial</p>"
    elif environ["PATH_INFO"]=="/suma":
        params=environ["QUERY_STRING"].split("&")
        suma=0
        for par in params:
                suma=suma+int(par.split("=")[1])
        respuesta="<p>La suma es %d</p>" % suma
    else:
        respuesta = "<p><trong>Página incorrecta</strong></p>"
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return respuesta