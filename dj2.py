import numpy as np
for k,(a,b,c,d) in enumerate([(-2.24,0.43,-0.65,-2.43),(1.4,-2.3,2.4,-2.1),(-1.7,1.3,-0.1,-1.21)]):
    x=y=0.1;H=np.zeros((300,300))
    for i in range(250000):
        x,y=np.sin(a*y)-np.cos(b*x),np.sin(c*x)-np.cos(d*y)
        if i>100:H[int((y+2)/4*299),int((x+2)/4*299)]+=1
    t=np.log1p(H);t/=t.max()
    rgb=np.stack([255*t**.6,255*t**(1.3+k*.3),255*t**(.5+.4*(2-k))],-1).astype(np.uint8)
    open('t%d.ppm'%k,'wb').write(b'P6 300 300 255\n'+rgb.tobytes())
