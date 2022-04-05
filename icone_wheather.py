import requests
import io
from PIL import Image
from PIL import ImageDraw, ImageFont



def PIL_icon_wheather(icone_ID):
    response = get_url("http://openweathermap.org/img/wn/"+icone_ID+"@2x.png")
    image_bytes = io.BytesIO(response.content)
    img=Image.open(image_bytes)
    myFont = ImageFont.truetype('FreeMono.ttf', 17) 
    T1 = ImageDraw.Draw(img)
    T1.text((0, 0), "Wheather :", fill=(0, 0, 0), font=myFont) 
    return img
def get_url(url,proxy={}):
        if 'http' in proxy:
            return requests.get(url, proxies=proxy)
        else:
            return requests.get(url)

if __name__=="__main__":
    img=PIL_icon_wheather("01n")
    img.show()