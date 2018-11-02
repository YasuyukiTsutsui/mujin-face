# ネットの画像で顔認識をして男女の判別と年齢推定を行うプログラム
import cognitive_face as CF
import requests
from IPython.display import HTML

# matplotlib inline
import matplotlib.pyplot as plt

from PIL import Image
from matplotlib import patches
from io import BytesIO

#write API key
KEY = "**************"
CF.Key.set(KEY)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

#APIに指定した画像で顔認識させる
image_url = 'https://how-old.net/Images/faces2/main007.jpg' #画像を指定
faces = CF.face.detect(image_url, landmarks=True, attributes='age,gender')

#結果を出力
print(faces)

#画像を取得
response = requests.get(image_url) #画像データの取得
image = Image.open(BytesIO(response.content))

plt.figure(figsize=(8,8))
ax = plt.imshow(image, alpha=0.6) #alphaが画像の濃度調整

#画像に結果を反映
for face in faces:
    fr = face["faceRectangle"]
    fa = face["faceAttributes"]
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(
        origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
    ax.axes.add_patch(p)
    plt.text(origin[0], origin[1], "%s, %d" % (
        fa["gender"].capitalize(), fa["age"]), fontsize=20, weight="bold", va="bottom")
_ = plt.axis("off")
