import numpy as np
from PIL import Image
from tqdm import tqdm
# create x, y plane (start:stop:num_elementsj)
x,y=np.ogrid[-5.4:0.8:9500j,-1.6:1.6:5000j]

# c is complex number (a +bi), plot by setting
# a to x and b to y
c = x + 1j*y

z = c * 0
# make nparray of ones/zeros in same shape as x * y
ones = np.ones_like(x*y)
zeros = np.ones_like(x*y)

max_check = 200
for n in tqdm(range(max_check)):
    np.putmask(zeros, abs(z) <= 20, n*ones)
    np.putmask(z, abs(z) <= 20, z**2 + c)


smooth = zeros - np.log(np.log(np.maximum(2.0, abs(z))))/np.log(2.6)
v = np.where(abs(z) <= 20, 0, np.log(smooth * 1.1 + 1.0) * 0.3)
greys = np.array((v,v,v)).T
blues = np.array((v**4, v**2.5, v)).T
w = np.maximum(0, 2-v)
sepias = np.array((w, w**1.5, w**3)).T
color = np.where(greys<1.0, blues, sepias)
rgb = np.uint8(np.minimum(1.0, color) * 255)
img = Image.fromarray(rgb, mode="RGB")

img.save("mand.png")
