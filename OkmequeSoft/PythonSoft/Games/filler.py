import random
def fill():
    with open(input("Enter a valid file name to fill : "),"a") as filler:
        chars = '¦¬`1!23£4$€5%6^7&8*9(0-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
        for x in range(int(input("Enter a number.The number will be the bytes of data that will be written to your file : "))):
            filler.write(random.choice(chars))
            print(str(x + 1) + " bytes written.",end='\r')
        print('\n')
    return
fill()
