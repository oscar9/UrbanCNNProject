# encoding: utf-8

import gvsig

def main(*args):

    raster = gvsig.currentView().getLayer("ALICANTE_MUESTRA")
    rstore = raster.getDataStore()
    vectorial = gvsig.currentView().getLayer("MANZANA_32630_muestras")
    vstore = vectorial.getFeatureStore()
    f1 = vstore.first()
    print f1
    print rstore.getBands()
    for band in rstore.getBands():
      print band
    
    #buffer.clip(envelope)
    
