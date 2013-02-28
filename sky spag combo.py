#sky spag combo
import maya.cmds as cmds
import random
import math
cmds.select(all=True);
cmds.delete();

random.seed()
a = 0
b = 50

#create honey plane
def createHoneyPiece(n, b):
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
    if(b):
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
    #cmds.scale(10, 10, 50, planeName);

PI = 3.14
#turn into sphere
def createHoneySphere(i):
    pn = 'plane'+str(i)
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
for i in range(1):
    planeNameVar = 'plane'+str(pieceNumber)
    cmds.select(cl=True);
    createHoneyPiece(pieceNumber, True);
    #cmds.move(random.randint(a, b), random.randint(a, b), random.randint(a, b), planeNameVar, a=True);
    cmds.move(0, -5, 0, planeNameVar, a=True)
    createHoneySphere(pieceNumber);
    cmds.select(cl=True);
    #cmds.setAttr(planeNameVar+".translateY",  random.randint(a, b))
    pieceNumber += 1;
'''
for i in range(1):
    planeNameVar = 'plane'+str(pieceNumber)
    cmds.select(cl=True);
    createHoneyPiece(pieceNumber);
    #cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    createHoneySphere(pieceNumber);
    #cmds.rotate(0,0, 0, r=True, ocp=True, os=True)
    pieceNumber += 1;
'''   

i = 0;
size = 75;
radius = 0;
endExtrudeA = -5
endExtrudeB = 5
endExtrudeA2 = -5
endExtrudeB2 = 5

planeNameVar = 'plane'+str(pieceNumber)
cmds.select(cl=True);
createHoneyPiece(pieceNumber, False);
cmds.scale(0.1, 1, 0.1, planeNameVar);
height = 5

iVal = 1
xVal = 1
zVal = 1
for i in range(size):
    heghtTaper1 = random.randint(0, 6)
    heghtTaper2 = random.randint(5, 12)
    #cmds.setAttr("polyExtrudeFace"+str(pieceNumber*2+2)+".localTranslate", 0, 0, 5, type="double3")
    curveName = "curve"+str(i+1)
    #cmds.curve( p=[(0, 1, 0), (3, 5, random.randint(endExtrudeA, endExtrudeB)), (5, 6, 7), (9, 9, random.randint(endExtrudeA, endExtrudeB))] )
    s = sinHeight(iVal)
    if(i > (size/2)):
        s = s*-1
    cmds.curve( p=[(0, 1, 0), (random.randint(endExtrudeA, endExtrudeB), height*s, random.randint(endExtrudeA, endExtrudeB)), (random.randint(endExtrudeA, endExtrudeB), (height+heghtTaper1)*s, random.randint(endExtrudeA, endExtrudeB)), (random.randint(endExtrudeA, endExtrudeB), (height+heghtTaper2)*s, random.randint(endExtrudeA, endExtrudeB))] )
    #cmds.curve( p=[(0, 1, 0), (0, height*s, 0), (0, (height+heghtTaper1)*s,0), (0, (height+heghtTaper2)*s, 0)] )
    
    #cmds.move(0, s , radius, r=True); 
    cmds.xform(ws=True, rp=(0,0,0));
    cmds.rotate(i*15, i*15, 0, r=False, os = True);
    #cmds.curve( p=[(0, 0, 0), (xVal, height, zVal), (xVal, (height+heghtTaper1), zVal), (s, (height+heghtTaper2), s)] )
    
    val = random.randint(0, 151)
    val2 = i * 2
    cmds.polyExtrudeFacet(planeNameVar+'.f['+str(val2)+']', constructionHistory=1, keepFacesTogether=1, pvx=4.7, pvy=-1.058, pvz=2.38, divisions=15, twist=0, taper=10, off=0, thickness=1, smoothingAngle=30, inputCurve=curveName)
    height+=0.09
    if(i == size*0.5):
        height = 5
    if(i > size*0.5):
        iVal-=1
        xVal-=1
        zVal+=1
    else:
        iVal+=1
        xVal+=1
        zVal-=1
        endExtrudeA-=1
        endExtrudeB+=1
    print height
    endExtrudeA2 = endExtrudeA
    endExtrudeB2 = endExtrudeB
    
def sinHeight(n):
    sy = 0
    for i in range(n):
        sy = math.sin( float(i) / n * 2 * math.pi ) * n            
    return sy

print '----'
for i in range(10):
    print pieceNumber
    cmds.select(cl=True);
    planeNameVar = 'plane'+str(pieceNumber)
    cmds.select(cl=True);
    createHoneyPiece(pieceNumber, True);
    cmds.polyExtrudeFacet( kft=False, ltz=10, ls=(0.5, 0.5, 0) )
    cmds.move(random.randint(c, d), random.randint(c, d), 0, planeNameVar, a=True);
    cmds.rotate(random.randint(1, 6), 0, random.randint(1, 6), planeNameVar, a=True)
    createHoneySphere(pieceNumber);
    cmds.select(cl=True);
    #cmds.setAttr(planeNameVar+".translateY",  random.randint(a, b))
    pieceNumber += 1;