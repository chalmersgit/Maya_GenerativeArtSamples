#
import maya.cmds as cmds
import random

cmds.select(all=True);
cmds.delete();

random.seed()



def createHoneyPiece(n):
    planeName = 'plane'+str(n)
    cmds.polyPlane(w=20, h=20, sx=12, sy=12, n=planeName)
    edgeNum = 26
    modVal = 1;
    edgeArray = []
    for i in range(52):
        edgeArray.append(planeName+'.e['+str(edgeNum)+']');
        edgeNum += 2
        if(edgeNum == 51):
            edgeNum = 101
        if(edgeNum==50):
            edgeNum = 49
        if(edgeNum == 126):
            edgeNum = 176
        if(edgeNum==125):
            edgeNum = 124
        if(edgeNum==201):
            edgeNum = 251
        if(edgeNum==200):
            edgeNum = 199
        if(edgeNum==275):
            edgeNum = 274
    cmds.polyBevel(edgeArray, offset=1,offsetAsFraction=1,autoFit=1,segments=1,worldSpace=1,uvAssignment=0,fillNgons=1,mergeVertices=1,mergeVertexTolerance=0.0001,smoothingAngle=30,miteringAngle=180,angleTolerance=180,ch=1)
    cmds.select( clear=True)
    del edgeArray[:]
    for i in range(532, 620):
        cmds.select(planeName+'.e['+str(i)+']', toggle=True);
    size = 36;
    edgeNum = 31
    counter = 0
    for i in range(size):
        cmds.select(planeName+'.e['+str(edgeNum)+']', toggle=True);
        edgeNum += 2
        counter += 1
        if(counter == 12):
            counter = 0
            edgeNum += 7;
    cmds.delete();
    for i in range(12):
         cmds.select(planeName+'.f['+str(i)+']', toggle=True);
    for i in range(96, 108):
         cmds.select(planeName+'.f['+str(i)+']', toggle=True);
    for i in range(1,8):
        cmds.select(planeName+'.f['+str(i*12)+']', toggle=True);
    for i in range(1,8):
        cmds.select(planeName+'.f['+str(i*12+11)+']', toggle=True);
    cmds.delete();
    cmds.select(planeName);

for i in range(1):
    createHoneyPiece(i)
    pn = 'plane'+str(i)
    cmds.scale(1, 1, 0.5, pn);
    cmds.select(pn+'.f[0:113]')
    cmds.polyExtrudeFacet(constructionHistory=1, keepFacesTogether=0, pvx=4.7, pvy=-1.058, pvz=2.38, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30)
    cmds.setAttr("polyExtrudeFace1.localScale", 0.833333, 0.833333, 0.829938, type="double3")
    cmds.delete();
    cmds.select( pn+'.f[0:723]')
    cmds.polyExtrudeFacet(constructionHistory=1, keepFacesTogether=1, pvx=-4.7, pvy=-1.058, pvz=2.38, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30)
    cmds.setAttr("polyExtrudeFace2.localTranslate", 0, 0, 1, type="double3")
    
'''
for i in range(1):
    createHoneyPiece(i)
    pn = 'plane'+str(i)
    cmds.scale(1, 1, 0.5, pn);
    #planeName+'.f['+str(i*12+11)+']'
    cmds.select(pn+'.f[0:113]')
    #cmds.polyExtrudeFacet(constructionHistory= True,keepFacesTogether = False, pvx=4.768371582,pvy=1.058791184,pvz=2.384185791,divisions=1,twist=0,taper=1,off=0,thickness=0, smoothingAngle=30, plane0.f[0:113];
    #cmds.polyExtrudeFacet( kft=False )
    
    #cmds.polyExtrudeFacet( kft=False, ltz=0, ls=(0.5, 0.5, 0) )
    
    cmds.polyExtrudeFacet(constructionHistory=1, keepFacesTogether=0, pvx=4.7, pvy=-1.058, pvz=2.38, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30)
    cmds.setAttr("polyExtrudeFace1.localScale", 0.833333, 0.833333, 0.829938, type="double3")
    cmds.delete();
    cmds.select( pn+'.f[0:723]')
    cmds.polyExtrudeFacet(constructionHistory=1, keepFacesTogether=1, pvx=-4.7, pvy=-1.058, pvz=2.38, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30)
    cmds.setAttr("polyExtrudeFace2.localTranslate", 0, 0, 1, type="double3")
    
    
    #cmds.setAttr("polyExtrudeFace2.localScale", 0.833333, 0.833333, 0.829938,type="double3")
    
    #cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    #cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    #cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    #cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    #cmds.rotate(i*10,0, 0, r=True, ocp=True, os=True)
'''
'''
for i in range(40):
    createHoneyPiece(i)
    pn = 'plane'+str(i)
    cmds.scale(1, 1, 0.5, pn);
    cmds.select(pn)
    cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    cmds.rotate(i*10,0, 0, r=True, ocp=True, os=True)
    #cmds.move(random.random()*100, 0, random.random()*100, r=True)
'''
'''
cmds.scale(1, 1, 0.5, 'plane');
cmds.select('plane')
cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
cmds.rotate(0, 0, 0)
'''