# uarte za martin vatermeline
import random
def adv_pwd(spcn, numn, char):
    end = ""
    passwd = ""
    spc = '¦¬`!£$€%^&*()-_=+;:@~#\|,<.>/?'
    num = "1234657890"
    ch = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmMm"
    spcs = ""
    nums = ""
    chs = ""
    for p in range(spcn):
        spcs += random.choice(spc)
    for s in range(numn):
        nums += random.choice(num)
    for ad in range(char):
        chs += random.choice(ch)
    end += spcs + nums + chs
    for x in range(len(end)):
        passwd += random.choice(end)
    return passwd    
def generate_pwd(length):
    character_set = '¦¬`1!23£4$€5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
    pwd = ""
    for x in range(length):
            pwd += random.choice(character_set)
    return pwd
def cyrillic_pwd(length):
     cyrillic_chars = "АаВеЕЗМоНОРрСсТуХхЈјҮԁԌԚԛԜԝ"
     standard_chars = '`1!234$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
     chars = [cyrillic_chars, standard_chars]
     pwd =""
     for x in range(length):
                            pwd += random.choice(random.choice(chars))
     return pwd