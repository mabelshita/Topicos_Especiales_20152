Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos = readfile('blogdata1.txt')
>>> palabras[:20]
[u'otro', u'otra', u'igual', u'seis', u'haber', u'importantes', u'fuera', u'esos', u'presenta', u'china', u'cr\xedticas', u'funciona', u'concepto', u'cielo', u'cr\xedtica', u'podr\xedan', u'mediante', u'hoy', u'calidad', u'ser\xeda']
>>> datos[0][:20]
[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> clust = hcluster(datos,euclidean)
>>> type(clust)
<type 'instance'>
>>> printclust(clust, blogs)
-
  Hispasec @unaaldia
  -
    Mitos y Timos
    -
      El retorno de los charlatanes
      -
        Astrof�sica    y    F�sica
        -
          Experimentos caseros
          -
            Curistoria - Curiosidades y an�cdotas hist�ricas
            -
              Genbeta Dev
              -
                Cholonymous: Blog Peruano de Actualidad y Tecnolog�a
                -
                  Xataka Ciencia
                  -
                    Hipertextual
                    -
                      Eureka
                      -
                        Tecnolog�a 7
                        -
                          PC World en Espa�ol
                          -
                            PC World Per�
                            -
                              EspacioCiencia.com
                              -
                                Historias de la Historia
                                -
                                  La mentira esta ahi fuera
                                  -
                                    La Ciencia para todos
                                    -
                                      Naukas
                                      -
                                        Tecnolog�a Obsoleta
                                        -
                                          La Ciencia y sus Demonios
                                          -
                                            C�rculo Esc�ptico Argentino
                                            -
                                              FayerWayer
                                              Imagen astronom�a diaria - Observatorio
>>> clust = hcluster(datos,pearson)
>>> type(clust)
<type 'instance'>
>>> printclust(clust, blogs)
-
  -
    PC World Per�
    PC World en Espa�ol
  -
    -
      Tecnolog�a Obsoleta
      -
        C�rculo Esc�ptico Argentino
        -
          La mentira esta ahi fuera
          -
            La Ciencia y sus Demonios
            -
              La Ciencia para todos
              -
                -
                  Tecnolog�a 7
                  -
                    Historias de la Historia
                    EspacioCiencia.com
                -
                  Experimentos caseros
                  -
                    -
                      Cholonymous: Blog Peruano de Actualidad y Tecnolog�a
                      -
                        El retorno de los charlatanes
                        -
                          Mitos y Timos
                          -
                            Astrof�sica    y    F�sica
                            Hispasec @unaaldia
                    -
                      Curistoria - Curiosidades y an�cdotas hist�ricas
                      -
                        -
                          Xataka Ciencia
                          Genbeta Dev
                        -
                          FayerWayer
                          Hipertextual
    -
      Imagen astronom�a diaria - Observatorio
      -
        Naukas
        Eureka
>>> 
