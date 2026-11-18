import numpy as np
# Clifford attractor
a,b,c,d=-1.4,1.6,1.0,0.7
x=y=0.1;N=400000
H=np.zeros((500,500))
for i in range(N):
    x,y=np.sin(a*y)+c*np.cos(a*x),np.sin(b*x)+d*np.cos(b*y)
    if i>100:
        H[int((y+2.5)/5*499),int((x+2.5)/5*499)]+=1
t=np.log1p(H);t/=t.max()
rgb=np.stack([255*t**.7,160*t**1.2,255*(t**.5)*.9+30],-1).astype(np.uint8)
open('a.ppm','wb').write(b'P6 500 500 255\n'+rgb.tobytes())
