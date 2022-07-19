import requests
from PIL import Image
import hashlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

url = 'https://png.pngtree.com/png-clipart/20210310/original/pngtree-a-gray-pet-cat-animal-png-image_5955801.jpg'
r = requests.get(url, stream = True).raw

img = Image.open(r)
img.show()
img.save('src.png')

BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)
        
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())
print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))

dst_img = mpimg.imread('dst.png')
print(dst_img)
pseudo_img = dst_img [:,:,0]
print(pseudo_img)

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)
plt.title('Pseudo Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img [:,:,0]
plt.imshow(pseudo_img)
plt.show()
