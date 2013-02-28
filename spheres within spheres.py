#spheres within spheres
import maya.cmds as cmds
import random

cmds.select(all=True);
cmds.delete();

random.seed()


#create honey plane
def createHoneyPiece(n):
    planeName = 'plane'+str(n)
    print planeName
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
    print len(edgeArray)
    del edgeArray[:]
    print len(edgeArray)
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
    
    cmds.scale(1, 1, 0.5, planeName);
    #cmds.select(planeName+'.f[0:113]')
    cmds.polyExtrudeFacet(planeName+'.f[0:113]', constructionHistory=1, keepFacesTogether=0, pvx=4.7, pvy=-1.058, pvz=2.38, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30)
    cmds.setAttr("polyExtrudeFace"+str(n*2+1)+".localScale", 0.833333, 0.833333, 0.829938, type="double3")
    cmds.delete();
    cmds.select(planeName+'.f[0:723]')
    cmds.polyExtrudeFacet(constructionHistory=1, keepFacesTogether=1, pvx=-4.7, pvy=-1.058, pvz=2.38, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30)
    cmds.setAttr("polyExtrudeFace"+str(n*2+2)+".localTranslate", 0, 0, 1, type="double3")
    #cmds.select(planeName);

PI = 3.14
#cut honey plane
def createHoneySphere(i):
    pn = 'plane'+str(i)
    #turn into sphere
    #bend1
    cmds.select(pn);
    cmds.nonLinear(type='bend', lowBound=-1, highBound=1, curvature =  PI)
    cmds.setAttr("bend"+str(i*2+1)+"Handle.rotateX", 90);
    cmds.setAttr("bend"+str(i*2+1)+"Handle.rotateZ", 90);
    #bend2
    cmds.select(pn);
    cmds.nonLinear(type='bend', lowBound=-1, highBound=1, curvature =  PI)
    cmds.setAttr("bend"+str(i*2+2)+"Handle.rotateZ", 90);

pieceNumber = 0
for i in range(10):
    cmds.select(clear=False);
    createHoneyPiece(i);
    createHoneySphere(i);
    cmds.setAttr("plane0.translateY", i*5)
    pieceNumber += 1