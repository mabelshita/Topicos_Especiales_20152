Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos = readfile('blogdata1.txt')
>>> palabras[:20]
[u'otro', u'otra', u'igual', u'seis', u'haber', u'importantes', u'fuera', u'esos', u'presenta', u'china', u'cr\xedticas', u'funciona', u'concepto', u'cielo', u'cr\xedtica', u'podr\xedan', u'mediante', u'hoy', u'calidad', u'ser\xeda']
>>> datos[0][:20]
[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> clust = hcluster(datos,manhatan)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    clust = hcluster(datos,manhatan)
  File "G:\mm\TOPICOS\labo\unidad2\CAPITULO 3\clusters.py", line 71, in hcluster
    closest=distance(clust[0].vec,clust[1].vec)  ### la distancia entre cada cluster
  File "G:\mm\TOPICOS\labo\unidad2\CAPITULO 3\clusters.py", line 31, in manhatan
    return sum(abs([(v1[i]-v2[i]) for i in range(len(v1))]))
TypeError: bad operand type for abs(): 'list'
>>> clust = hcluster(datos,euclidean)
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos = readfile('blogdata1.txt')
>>> palabras[:20]
[u'otro', u'otra', u'igual', u'seis', u'haber', u'importantes', u'fuera', u'esos', u'presenta', u'china', u'cr\xedticas', u'funciona', u'concepto', u'cielo', u'cr\xedtica', u'podr\xedan', u'mediante', u'hoy', u'calidad', u'ser\xeda']
>>> datos[0][:20]
[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> clust = hcluster(datos,euclidean)
>>> clust = hcluster(datos,manhatan)
>>> type(clust)
<type 'instance'>
>>> printclust(clust, blogs)
-
  Mitos y Timos
  -
    -
      -
        -
          Cholonymous: Blog Peruano de Actualidad y Tecnología
          Xataka Ciencia
        -
          Genbeta Dev
          -
            Astrofísica    y    Física
            -
              Curistoria - Curiosidades y anécdotas históricas
              Experimentos caseros
      -
        Hipertextual
        -
          -
            PC World Perú
            Tecnología 7
          -
            -
              Imagen astronomía diaria - Observatorio
              -
                Naukas
                Historias de la Historia
            -
              -
                Eureka
                -
                  La mentira esta ahi fuera
                  PC World en Español
              -
                EspacioCiencia.com
                -
                  -
                    Tecnología Obsoleta
                    FayerWayer
                  -
                    La Ciencia y sus Demonios
                    -
                      Círculo Escéptico Argentino
                      La Ciencia para todos
    -
      El retorno de los charlatanes
      Hispasec @unaaldia
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos = readfile('blogdata1.txt')
>>> palabras[:20]
[u'otro', u'otra', u'igual', u'seis', u'haber', u'importantes', u'fuera', u'esos', u'presenta', u'china', u'cr\xedticas', u'funciona', u'concepto', u'cielo', u'cr\xedtica', u'podr\xedan', u'mediante', u'hoy', u'calidad', u'ser\xeda']
>>> datos[0][:20]
[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> clust = hcluster(datos,manhatan)
>>> type(clust)
<type 'instance'>
>>> printclust(clust, blogs)
-
  Mitos y Timos
  -
    -
      -
        -
          Cholonymous: Blog Peruano de Actualidad y Tecnología
          Xataka Ciencia
        -
          Genbeta Dev
          -
            Astrofísica    y    Física
            -
              Curistoria - Curiosidades y anécdotas históricas
              Experimentos caseros
      -
        Hipertextual
        -
          -
            PC World Perú
            Tecnología 7
          -
            -
              Imagen astronomía diaria - Observatorio
              -
                Naukas
                Historias de la Historia
            -
              -
                Eureka
                -
                  La mentira esta ahi fuera
                  PC World en Español
              -
                EspacioCiencia.com
                -
                  -
                    Tecnología Obsoleta
                    FayerWayer
                  -
                    La Ciencia y sus Demonios
                    -
                      Círculo Escéptico Argentino
                      La Ciencia para todos
    -
      El retorno de los charlatanes
      Hispasec @unaaldia
>>> 
