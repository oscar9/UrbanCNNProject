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

    raster = gvsig.currentView().getLayer("ALICANTE_MUESTRA")
    poligonos = gvsig.currentView().getLayer("MANZANA_32630_muestras")
    featureTypePoligonos = poligonos.getFeatureStore().getDefaultFeatureType()
    print poligonos
    fset = poligonos.getFeatureStore().getFeatureSet()
    for f in fset:
      temporalShape = createTemporalShape(featureTypePoligonos, f)
      tempFile = getTempFile("tempSample", ".tif", tempdir="E:/Atlas_Datos/test/tempTif")
      gvpy.runalg("clipgrid", "Resultado",temporalShape, PATH=tempFile)