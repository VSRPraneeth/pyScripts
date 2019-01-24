import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://media1.popsugar-assets.com/files/thumbor/9c6afTpnNRmDb1Wv2eW1r8REOYs/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2018/06/22/913/n/1922564/b31706b45b2d62162dc757.84031179_/i/Kendall-Jenner-Plunging-Neckline-Outfits.jpg")
