from PIL import Image




def rotate_90_clockwise(file):

    img = Image.open(file)
        
    #- is required because by default turns image anticlockwise.
    #expand = True makes the new canvas fit the rotated image.
    img = img.rotate(-90, expand = True)

    img.save("rotated_90_clockwise_{}".format(str(file)))
    img.show()



def rotate_90_anticlockwise(file):
    img = Image.open(file)
    #- is required because by default turns image anticlockwise.
    #expand = True makes the new canvas fit the rotated image.
    img = img.rotate(-270, expand = True)

    img.save("rotated_90_anti-clockwise_{}".format(str(file)))
    img.show()



def custom_rotation(file):
    img = Image.open(file)

    #checks a valid int was entered.
    correct = False
    while correct == False:
        try:
            rotation = int(input("Please enter a rotation angle: "))
            correct = True
                           
        except:
            print("Error\n")
            
    img = img.rotate(-rotation, expand = True)

    img.save("custom_rotated_{}_{}".format(str(rotation), str(file)))
    img.show()


def histogram(file):
    img = Image.open(file)
    print(img.histogram())
