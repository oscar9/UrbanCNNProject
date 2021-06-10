# encoding: utf-8

import gvsig
from gvsig.libs import gvpy
from gvsig.geom import *
from gvsig.utils import *

def createTemporalShape(featureType, feature):
        schema = gvsig.createFeatureType(featureType) # DefaultFeatureType
        shape = gvsig.createShape(schema, prefixname="resultado")
        print "Nombre: ", shape.getName(), "\tRuta: ", shape.getDataStore().getFullName()
        shapeStore = shape.getFeatureStore()

        shape.edit()
        newFeature = shapeStore.createNewFeature(feature)
        # Setting arguments
        #shape.append(ID=1, NAME="Valencia", GEOMETRY=createPoint2D(10, 10))
        # Diccionary
        shapeStore.insert(newFeature)
        shape.commit()

        #gvsig.currentView().addLayer(shape)
        return shape

def main(*args):

    raster = gvsig.currentView().getLayer("alicante")
    
    poligonos = gvsig.currentView().getLayer("alicante_muestras_pnoa0872")
    print "Raster: ",raster
    print "Poligonos: ", poligonos
    featureTypePoligonos = poligonos.getFeatureStore().getDefaultFeatureType()
    print poligonos
    fset = poligonos.getFeatureStore().getFeatureSet()
    total = fset.getSize()
    n = 0
    for f in fset:
      n+=1
      print ("Status: "+str((double(n)/total)*100.0))
      buildType= f.get("TIPO")
      if buildType == -1: 
        continue
      temporalShape = createTemporalShape(featureTypePoligonos, f)
      tempFile = getTempFile("tempSample","_"+str(buildType)+ ".tif", tempdir="E:\\Atlas_Datos\\test\\tempTif")
      print tempFile
      gvpy.runalg("clipgrid", raster,temporalShape, PATH=tempFile)