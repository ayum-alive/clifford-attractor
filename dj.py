import numpy as np
a,b,c,d=1.641,1.902,0.316,1.525
x=y=0.1;H=np.zeros((500,500))
for i in range(400000):
    x,y=np.sin(a*y)-np.cos(b*x),np.sin(c*x)-np.cos(d*y)
    if i>100:H[int((y+2)/4*499),int((x+2)/4*499)]+=1
t=np.log1p(H);t/=t.max()
rgb=np.stack([60+195*t**.9,200*t**.6,120*t**.4],-1).astype(np.uint8)
open('dj.ppm','wb').write(b'P6 500 500 255\n'+rgb.tobytes())
