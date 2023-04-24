from PIL import Image, ImageFilter, ImageColor 
import os
import time

def show():
    print("there are a variety of pictures i wanna show u \
;")
    list = ['(b)ingus', '(bl)ack cat', '(be)erus', '(f)at cat', '(l)oaf cat', '(m)anwha \
cat', '(o)range cat', '(s)impson cat', '(st)anding cat', '(w)hite cat']
    for i in list:
        print(i)
        time.sleep(.7)
    pick = input('choose an image to open from the corresponding \
brackets: ')
    while True:
        if pick == "b":
            image1 = Image.open('bingus.jpeg')
            image1.show()
        if pick == "bl":
            image2 = Image.open('black.jpeg')
            image2.show()
        if pick == "be":
            image3 = Image.open('beerus.jpeg')
            image3.show()
        if pick == "f":
            image4 = Image.open('fatcat.jpeg')
            image4.show()
        if pick == "l":
            image5 = Image.open('loafcat.jpeg')
            image5.show()
        if pick == "m":
            image6 = Image.open('manwhacat.jpeg')
            image6.show()
        if pick == "o":
            image7 = Image.open('orangecat.jpeg')
            image7.show()
        if pick == "s":
            image8 = Image.open('simpcat.jpeg')
            image8.show()
        if pick == "w":
            image9 = Image.open('white.jpeg')
            image9.show()
        if pick == "st":
            image10 = Image.open('standcat.jpeg')
            image10.show()
        break

def png():
    print('im gonna save all these images above into png stuff \
    is that cool with u?')
    while True:
        pick1 = input("wanna do it or nah(y/n): ").lower()
        if pick1 == 'n':
            print("no? then imma leave")
            quit()
        if pick1 == 'y':
            for f in os.listdir(','):
                if f.endswith('.jpeg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))
        else:
            print('typo! try again')

def size():
    size_200 = (200,200)
    size_400 = (400,400)
    size_600 = (600,600)
    print('i have the ability to change the size to either 200, 400 or 600')
    pick2 = input('what size do want: ')
    while True:
        if pick2 == '200':
            for f in os.listdir('.'):
                if f.endswith('.jpeg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    
                    i.thumbnail(size_200)
                    i.save('200/{}_200{}'.format(fn, fext))
            size_200.show()
            break
        if pick2 == '400':
            for f in os.listdir('.'):
                if f.endswith('.jpeg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    
                    i.thumbnail(size_400)
                    i.save('400/{}_400{}'.format(fn, fext))
            size_400.show()
            break
        if pick2 == '600':
            for f in os.listdir('.'):
                if f.endswith('.jpeg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    
                    i.thumbnail(size_600)
                    i.save('600/{}_600{}'.format(fn, fext))
            size_600.show()
            break
        else:
            print('did really think i would do that size? im lazy to code another set for that size')

def rotate():
    print('i can also turn images around ')
    while True:
        pick3 = input('enter a desire degree u wish to rotate: ')
        if pick3 != int:
            print('that aint a number')
            continue
        else:
            break
    
    if not os.path.exists('rotate_image'):
        os.makedirs('rotate_image')
    
    for f in os.listdir(','):
        if f.endswith('.jpeg'):
            i = Image.open(f)
            rotate_image = i.rotate(pick3)
            rotate_image.save('rotate_image' + f )
    i.show()

def bnw():
    while True:
        pick = input('black and white now yes (y/n): ').lower()
        if pick == 'n':
            print('nah we have to do it but bye')
            exit()
        if pick =='y':
            break
        else:
            print('thats a typo try again')
        
    if not os.path.exists('converted_images'):
        os.makedirs('converted_images')
        
        for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                i = Image.open(f)
                i.convert(mode='L').save('converted_images/' + f)
    i.show()

def blur():
    print('imma blur the image of my pet black cat')
    while True:
        pick = int(input('how much blurryness assuming u dont wear glasses and have 20/20 vision \
        so plz enter a number: '))
        if pick != int:
            print('thats not a number......try again')
            
        else:
            break
    image3 = Image.open('black.jpeg')
    image3.filter(ImageFilter.GaussianBlur(pick)).save('black.jpeg')

def color():
    print('ill let u choose which to pic to filter')
    for i in list:
        print(i)
    pick = input('enter the first or two letters in their brackets: ')
    
    while True:
        if pick == "b":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image1 = Image.open('bingus.jpeg')
        image_rotate = image1.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "bl":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image2 = Image.open('black.jpeg')
        image_rotate = image2.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "be":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image3 = Image.open('beerus.jpeg')
        image_rotate = image3.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "f":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image4 = Image.open('fatcat.jpeg')
        image_rotate = image4.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "l":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image5 = Image.open('loafcat.jpeg')
        image_rotate = image5.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "m":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image6 = Image.open('manwhacat.jpeg')
        image_rotate = image6.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "o":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image7 = Image.open('orangecat.jpeg')
        image_rotate = image7.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "s":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image8 = Image.open('simpcat.jpeg')
        image_rotate = image8.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "w":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image9 = Image.open('white.jpeg')
        image_rotate = image9.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        if pick == "st":
            while True:
                pick1 = int(input('ok and how much should i rotate: '))
                if pick1 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick2 = int(input('now how much red (enter a number 0-220):  '))
                if pick2 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick3 = int(input('now how much green (enter a number 0-220):  '))
                if pick3 != int:
                    print('not a number, try again')
                else:
                    break
            while True:
                pick4 = int(input('now how much blue? (enter a number 0-220):  '))
                if pick4 != int:
                    print('not a number, try again')
                else:
                    break
        image10 = Image.open('standcat.jpeg')
        image_rotate = image10.rotate(pick1,expand= True, fillcolor = (pick2, pick3, pick4))
        image_rotate.show()
        
show()
png()
size()
rotate()
bnw()
blur()