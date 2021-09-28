from googletrans import Translator
translator=Translator()
def translate(language,text):
    try:
        if language=="Uz":
            response=translator.translate(text,dest="uz")
        elif language=="Eng":
            response=translator.translate(text,dest="en")
        elif language=="Ru":
            response=translator.translate(text,dest="ru")
        elif language=="Tj":
            response=translator.translate(text,dest="tg")
        elif language=="Kyrgyz":
            response=translator.translate(text,dest="ky")
        elif language=="Kz":
            response=translator.translate(text,dest="kk")
        elif language=="Turk":
            response=translator.translate(text,dest="tr")
        elif language=="Arabic":
            response=translator.translate(text,dest="ar")
        elif language=="German":
            response=translator.translate(text,dest="de")
        else:
            response=translator.translate(text,dest="uz")
    except:
        response="Xatolik yuz berdi"
    if response=="Xatolik yuz berdi":
        return response
    else:
        return response.text
        
        
    
    