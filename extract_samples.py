# encoding: utf-8

import gvsig

# Teniendo:
# - Capa raster
# - Capa vectorial de poligono

def main(*args):

    raster = gvsig.currentView().getLayer("Resultado")
    poligonos = gvsig.currentView().getLayer("aleatoria_geom_pol")

    fset = poligonos.getFeatureStore().getFeatureSet()
    for f in fset:
      print f
    pass
