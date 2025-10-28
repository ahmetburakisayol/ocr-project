import sys ## Burada modül yüklemesi yapıyoruz
from PIL import Image ## Bu iki satır, Python’a hangi modülleri  kullanacağını söylüyor.
import pytesseract ## 

sys.stdout.reconfigure(encoding='utf-8') ## BURADA ÇIKTI VERİRKEN TÜRKÇE KARAKTERLERİ BOZUK ÇIKARTMASIN DİYE UTF-8'E ÇEVİRİYORUZ.


hadibakalim = pytesseract.image_to_string(Image.open("ocr-dosya.png"), lang="tur") ## yazdırma kısımı
print(hadibakalim) ### maalesef çok beceriksizsin başak :/
