import cv2 
import time
import math 

def sobel_edge_txt(img, scale=1, size=600, init_y=20, init_x=200):
    image = cv2.imread(img)
    image = image[init_y:init_y + size, init_x:init_x+size] 

    resize = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY) 
    
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3, scale=scale, delta=0, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3, scale=scale, delta=0, borderType=cv2.BORDER_DEFAULT)
    
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    gradient = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    threshold_value = 100  # You can adjust this threshold value as needed
    _, strong_edges = cv2.threshold(gradient, threshold_value, 255, cv2.THRESH_BINARY)

    cv2.imshow("Strong edge", strong_edges)
    #cv2.imshow("magnitude", gradient)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    
    
    angle = []
    for i in range(int(size * scale)): 
        row = []
        for j in range(int(size * scale)):
            if abs_grad_x[i][j] != 0:
                atan = math.atan(grad_y[i][j]/grad_x[i][j])
                degrees = atan * 180/math.pi
                row.append(int(degrees)) 
            else:
                row.append("inf")
        angle.append(row)

    ascii = []
    characters = ["_ ", "| ", "/ ", """/ """]
    
    for row in angle:
        temp = []
        for character in row:
            if character == "inf":
                temp.append(characters[1])
            elif character < 20 and character > -20:
                temp.append("  ")
            elif character > 70:
                temp.append(characters[0])
            elif character < -70:
                temp.append("  ")
            elif character > 20 and character < 70:
                temp.append(characters[3])
            else:
                temp.append(characters[2])
        ascii.append(temp)

    for symbol in ascii[1]:
        print(symbol, end = "")

    
    file = open(r"C:\Users\allan\nvim\Python\ascii-art\art.txt", "w")
    count = 0
    for row in ascii:
        count += 1
        for character in row:
            file.write(character)
        file.write("\n")
        print(f"Successfully written line {count}")

sobel_edge_txt(r"C:\Users\allan\nvim\Python\ascii-art\images\malenia.jpg", scale=1, size=600, init_y=20, init_x=200)

#
