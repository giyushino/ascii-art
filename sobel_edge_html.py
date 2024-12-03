import cv2 
import time
import math 

def sobel_edge_html(img, scale=1, size=600, init_y=0, init_x=0, font_size = 4, gradient_threshold = 20):
    t1 = time.time()

    image = cv2.imread(img)
    image = image[int(init_y * scale):int(init_y * scale) + size, int(init_x * scale):int(init_x * scale) + size] 

    resize = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY) 
    
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3, scale=scale, delta=0, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3, scale=scale, delta=0, borderType=cv2.BORDER_DEFAULT)
    
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    gradient = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    threshold_value = gradient_threshold   # You can adjust this threshold value as needed
    _, strong_edges = cv2.threshold(gradient, threshold_value, 255, cv2.THRESH_BINARY)

    cv2.imshow("Strong", strong_edges)
    key = cv2.waitKey(0)

    if key == 13:
        cv2.destroyAllWindows()
        angle = []
        for i in range(resize.shape[0]): 
            row = []
            for j in range(resize.shape[1]):
                if abs_grad_x[i][j] != 0:
                    atan = math.atan2(grad_y[i][j], grad_x[i][j])
                    degrees = atan * 180 / math.pi
                    row.append(int(degrees)) 
                else:
                    row.append("inf")
            angle.append(row)

        ascii = []
        # Define the characters for different angles
        characters = ["_ ", "| ", """\ """, """/ """, "  "]
        for i in range(resize.shape[0]):
            temp = []
            for j in range(resize.shape[1]):
                if strong_edges[i][j] == 0:
                    temp.append(characters[4])
                else:
                    if angle[i][j] == "inf":
                        temp.append(characters[1])
                    elif angle[i][j] < 10 and angle[i][j] > -10:
                        temp.append(characters[0])
                    elif angle[i][j] > 80:
                        temp.append(characters[1])
                    elif angle[i][j] < -80:
                        temp.append(characters[1])
                    elif angle[i][j] > 10 and angle[i][j] < 80:
                        temp.append(characters[3])
                    else:
                        temp.append(characters[2]) 
            ascii.append(temp)
     
            
        # Write to an index.html file
        with open(r"C:\Users\allan\nvim\Python\ascii-art\index.html", "w") as file:
            file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>ASCII Art</title>\n<style>\n")
            #file.write("body { background-color: black; color: white; }\n")
            file.write("body { background-color: #341539; color: #DAB1DA; }\n")
            file.write(f"pre {{ font-family: monospace; font-size: {font_size}px; line-height: {font_size + 1}px; }}\n")
            file.write("</style>\n</head>\n<body>\n<pre>\n")

            count = 0
            for row in ascii:
                count += 1
                for character in row:
                    file.write(character)
                file.write("\n")
                print(f"Successfully written line {count}")
            
            file.write("</pre>\n</body>\n</html>")
            t2 = time.time()

            print(f"Time taken to complete task: {t2 - t1}")
    else:
        print("lol, what do you have to change")
        cv2.destroyAllWindows()
        

#sobel_edge_html(r"C:\Users\allan\nvim\Python\ascii-art\images\elden.jpg", scale=1, size=2000, init_y=20, init_x=0)

