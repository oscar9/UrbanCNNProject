# encoding: utf-8

import gvsig
from gvsig.libs.formpanel import FormPanel
from org.gvsig.tools.dispose import DisposeUtils

class TypeLabelToolPanel(FormPanel):
    def __init__(self):
        FormPanel.__init__(self, gvsig.getResource(__file__, "typeLabelTool.xml"))
        self.layer = gvsig.currentLayer()
        if self.layer == None:
          
          return
        self.store = self.layer.getFeatureStore()
        self.typeField = "TIPO"
        
    def btnTypeU_click(self, *args):
        print "desconocido"
        self.updateValueSelection(-1)
        
    def updateValueSelection(self, value):
        features = self.store.getFeatureSelection()
        for f in features:
            c = f.getEditable()
            c.set(self.typeField, value)
            features.update(c)
        features.deselectAll()
        DisposeUtils.dispose(features)
        self.updateCount()
        
    def btnType0_click(self, *args):
        print "espacio abierto"
        self.updateValueSelection(0)
        
    def btnType1_click(self, *args):
        print "industrial"
        self.updateValueSelection(1)
        
    def btnType2_click(self, *args):
        print "atomistico"
        self.updateValueSelection(2)
        
    def btnType3_click(self, *args):
        print "informal"
        self.updateValueSelection(3)
        
    def btnType4_click(self, *args):
        print "formal"
        self.updateValueSelection(4)
        
    def btnType5_click(self, *args):
        print "urbanizacion"
        self.updateValueSelection(5)
        
    def btnDeleteSelection_click(self, *args):
        print "eliminar seleccion"
        features = self.store.getFeatureSelection()
        for feature in features:
            features.delete(feature)
        features.deselectAll()
        DisposeUtils.dispose(features)

    def btnCount_click(self, *args):
        self.updateCount()
        
    def updateCount(self):
        fset = self.store.getFeatureSet()
        count = {}
        for f in fset:
          tipo = f.get("TIPO")
          if tipo in count:
            count[tipo] = count[tipo]+1
          else:
            count[tipo] = 1
        s = ""
        for k in count.keys():
           s = s + "<br>" + str(k)+": "+str(count[k])+"</br>"
        self.lblStatus.setText("<html>"+s+"</html>")
        DisposeUtils.dispose(fset)
    
def main(*args):
    l = TypeLabelToolPanel()
    l.showTool("TypeLabelToolPanel")
    pass