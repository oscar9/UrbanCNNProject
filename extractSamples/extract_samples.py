# encoding: utf-8

import gvsig
import random
import string
from org.gvsig.fmap.mapcontext import MapContextLocator
from org.gvsig.fmap.dal import DALLocator
from org.gvsig.fmap.dal.serverexplorer.filesystem import FilesystemServerExplorer
from java.io import File
from org.gvsig.fmap.dal.coverage import RasterLocator
from org.gvsig.tools.dataTypes import DataTypes
from java.awt.geom import AffineTransform
# Teniendo:
# - Capa raster
# - Capa vectorial de poligono
def createRasterGeo():
   buf = RasterLocator.getManager().createBuffer(DataTypes.DOUBLE,100,300,3, True)
   print buf
   #Writer
   manager = RasterLocator.getManager()
   writerBufferServer = manager.createDataServerWriter()
   writerBufferServer.setBuffer(buf, -1)
   name = ''.join(random.choice(string.lowercase) for x in range(10))
   rasterFile = "E:/Atlas_Datos/test/"+name+".tif"
   params = manager.createWriterParams(rasterFile)
   cellSize = 30
   xmin = 300000
   ymax = 4700000
   affineTransform = AffineTransform(cellSize, 0, 0, - cellSize, xmin, ymax)
   projection = gvsig.currentView().getProjection()
   print projection
   writer = manager.createWriter(writerBufferServer, rasterFile, buf.getBandCount(), affineTransform, buf.getWidth(), buf.getHeight(), buf.getDataType(), params, projection)
   writer.dataWrite()
   writer.writeClose()
   
def main(*args):
   createRasterGeo()
   
def main1(*args):
    dataManager = DALLocator.getDataManager()
    newRasterExplorerParameters = dataManager.createServerExplorerParameters(FilesystemServerExplorer.NAME)
    newRasterExplorerParameters.setDynValue("initialpath","E:/Atlas_Datos/test/a")

    explorer = dataManager.openServerExplorer(FilesystemServerExplorer.NAME, newRasterExplorerParameters)
    print explorer
    name = ''.join(random.choice(string.lowercase) for x in range(10))
    rasterFile = File("E:/Atlas_Datos/test/"+name+".tif")
    print rasterFile
    parameters = explorer.createStoreParameters(rasterFile)
    if parameters== None:
      print "[!] parameters es None"
      return
    dataStore = dataManager.openStore(parameters.getDataStoreName(), parameters)
    layer = manager.createLayer(name, dataStore)
    gvsig.currentView().addLayer(layer)

def main2(*args):

    raster = gvsig.currentView().getLayer("Resultado")
    poligonos = gvsig.currentView().getLayer("aleatoria_geom_pol")

    fset = poligonos.getFeatureStore().getFeatureSet()
    for f in fset:
      print f
    pass
    
    manager = MapContextLocator.getMapContextManager()
    name = "miraster"
    dataManager = DALLocator.getManager()
    #dataParameteres = raster.getDataParameters()
    parameters  = raster.getDataStore().getParameters()
    explorer = raster.getDataStore().getExplorer()
    #print dataParameters
    print parameters
    print explorer
    return
    newraster = manager.createLayer(name, parameters)
    gvsig.currentView().addLayer(newraster)
