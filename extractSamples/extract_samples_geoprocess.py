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
    executeName = "Test_004"

    #cityName = "Alicante"
    #rasterName = "PNOA_ANUAL_2017_OF_ETRS89_HU30_h50_0872"
    #layerName = "alicante_muestras_pnoa0872"
    
    #cityName = "Valencia"
    #rasterName = "PNOA_MA_OF_ETRS89_HU30_h50_0722" 
    #layerName = "valencia_25830"

    #cityName = "Barcelona_421"
    #rasterName = "PNOA_MA_OF_ETRS89_HU31_h50_0421"
    #layerName = "barcelona_25831_pnoa_0421"
    
    #cityName = "Pontevedra_152c"
    #rasterName = "PNOA_MA_OF_ETRS89_HU29_h50_0152"
    #layerName = "pontevedra_25829_pnoa_0152"
    
    #cityName = "Toledo_657"
    #rasterName = "PNOA_MA_OF_ETRS89_HU30_h50_0657"
    #layerName = "toledo_25830_pnoa_0657"
    
    cityName = "Salamanca_type"
    rasterName = "PNOA_MA_OF_ETRS89_HU30_h50_0478"
    layerName = "salamanca_25830"

    extractAll = False

    ##
    ## Process
    ##
    
    raster = gvsig.currentView().getLayer(rasterName)
    poligonos = gvsig.currentView().getLayer(layerName)
    
    print "Raster: ", raster
    print "Poligonos: ", poligonos
    if raster==None or poligonos==None:
      print "Capas no encontradas."
      return

    featureTypePoligonos = poligonos.getFeatureStore().getDefaultFeatureType()
    fset = poligonos.getFeatureStore().getFeatureSet()
    total = fset.getSize()
    n = 0
    for f in fset:
      n+=1
      print ("Status: "+str((float(n)/total)*100.0))
      if extractAll:
        manz = f.get("ID_MANZ")
        temporalShape = createTemporalShape(featureTypePoligonos, f)
        tempFile = getTempFile(cityName,"_"+str(manz)+"_-1.tif", tempdir="E:\\TFM_MUESTRAS\\"+executeName+"\\"+ cityName)
      else:
        buildType= f.get("TIPO")
        manz = f.get("ID_MANZ")
        if buildType == -1: 
          continue
        #print ("ID_MANZ:", f.get("ID_MANZ"))
        temporalShape = createTemporalShape(featureTypePoligonos, f)
        tempFile = getTempFile(cityName,"_"+str(manz)+"_"+str(buildType)+ ".tif", tempdir="E:\\TFM_MUESTRAS\\"+executeName+"\\"+ cityName)
        print tempFile
      gvpy.runalg("clipgrid", raster,temporalShape, PATH=tempFile, ADDLAYER=False)