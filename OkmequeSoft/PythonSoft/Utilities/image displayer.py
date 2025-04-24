import cv2 as cv
print("Program version 1.0.1")
print("Creator = Okmeque1")
try:
    print("This program will display 3 images.")
    a = input("Please enter a valid photo file.The format must be A:\Directory\Subdirectory\photo.format → ")
    with open(a,"r") as d:
        print("File Loaded.")
    b = input("Please enter a valid photo file.The format must be A:\Directory\Subdirectory\photo.format → ")
    with open(b,"r") as e:
        print("File Loaded.")
    c = input("Please enter a valid photo file.The format must be A:\Directory\Subdirectory\photo.format → ")
    with open(c,"r") as f:
        print("File Loaded.")
    img1 = cv.imread(a)
    cv.imshow('Image 1',img1)
    cv.waitKey(10000)
    img2 = cv.imread(b)
    cv.imshow('Image 2',img2)
    cv.waitKey(1000)
    img3 = cv.imread(c)
    cv.imshow('Image 3',img3)
    cv.waitKey(1000000000)
except FileNotFoundError:
    print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
    input("Press ENTER to exit.")
    exit()
except KeyboardInterrupt or EOFError:
    print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
    exit()
