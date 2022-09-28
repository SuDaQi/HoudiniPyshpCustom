import shapefile #导入shapefile模块
import sys;
reload(sys);
sys.setdefaultencoding("utf-8")
node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

class houPloy:
    def __init__(self,shp):
        self.shapes = shp
    def createLine(self):
        for uatt in self.shapes[0].__geo_interface__["properties"]:
            geo.addAttrib(hou.attribType.Prim, uatt, "")
        geo.addAttrib(hou.attribType.Prim, "polyType", "")
        geo.addAttrib(hou.attribType.Prim, "shpType", "")
        for shape in self.shapes:
            line = geo.createPolygon()
            line.setIsClosed(0)
            line.setAttribValue("polyType",shape.__geo_interface__["geometry"]["type"])
            line.setAttribValue("shpType",shape.__geo_interface__["type"])
            for coord in shape.__geo_interface__["geometry"]["coordinates"]:
                pt = geo.createPoint()
                pt.setPosition((coord[0],0,coord[1]))
                line.addVertex(pt)
            for key in shape.__geo_interface__["properties"].keys():
                line.setAttribValue(key,str(shape.__geo_interface__["properties"][key]))
    def createPoly(self):
        for uatt in self.shapes[0].__geo_interface__["properties"]:
            geo.addAttrib(hou.attribType.Prim, uatt, "")
        geo.addAttrib(hou.attribType.Prim, "polyType", "")
        geo.addAttrib(hou.attribType.Prim, "shpType", "")
        geo.addAttrib(hou.attribType.Prim, "countNumP", 0)
        pg = 1
        geo.addAttrib(hou.attribType.Prim, "polyGourp", pg)
        for shape in self.shapes:
            pg += 1
            poly = geo.createPolygon()
            poly.setAttribValue("shpType",shape.__geo_interface__["type"])
            poly.setAttribValue("polyGourp",pg)
            poly.setAttribValue("polyType",shape.__geo_interface__["geometry"]["type"])
            for coord in shape.__geo_interface__["geometry"]["coordinates"][0][0:-1]:
                pt = geo.createPoint()
                pt.setPosition((coord[0],0,coord[1]))
                poly.addVertex(pt)
            for key in shape.__geo_interface__["properties"].keys():
                poly.setAttribValue(key,str(shape.__geo_interface__["properties"][key]))
            poly.setAttribValue("countNumP",len(shape.__geo_interface__["geometry"]["coordinates"][0][0:-1]))
        return self
    def line(self,on_off):
        if on_off == 1:
            for shape in self.shapes:
                poly = geo.createPolygon()
                poly.setIsClosed(0)
                poly.setAttribValue("shpType",shape.__geo_interface__["type"])
                poly.setAttribValue("polyType",shape.__geo_interface__["geometry"]["type"])
                for coord in shape.__geo_interface__["geometry"]["coordinates"][0][0:-1]:
                    pt = geo.createPoint()
                    pt.setPosition((coord[0],0,coord[1]))
                    poly.addVertex(pt)
                for key in shape.__geo_interface__["properties"].keys():
                    poly.setAttribValue(key,str(shape.__geo_interface__["properties"][key]))
                    
shapes1=shapefile.Reader("C:/Users/ycwb0484/Desktop/GIStest/test/buildings.shp").shapeRecords()
houPloy(shapes1).createPoly().line(1)
