import cv2
 
if __name__ == "__main__":
    img = cv2.imread('yuner.jpg', 1)
    
    print('Original Dimensions : ',img.shape)
    
    scale_percent = 30       # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized_1 = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    resized_2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    fx = 1.5
    fy = 1.5

    resized1_1 = cv2.resize(resized_1, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_NEAREST)
    
    resized2_1 = cv2.resize(resized_1, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LINEAR)
    
    resized3_1 = cv2.resize(resized_1, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_CUBIC)

    resized1_2 = cv2.resize(resized_2, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_NEAREST)

    resized2_2 = cv2.resize(resized_2, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LINEAR)
    
    resized3_2 = cv2.resize(resized_2, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_CUBIC)

    print('Resized Dimensions : ',resized_1.shape)
    
    cv2.imshow("Resized image1", resized_1)
    cv2.imshow("INTER_NEAREST image1", resized1_1)
    cv2.imshow("INTER_LINEAR image1", resized2_1)
    cv2.imshow("INTER_CUBIC image1", resized3_1)

    print('Resized Dimensions : ',resized_2.shape)  
    
    cv2.imshow("Resized image2", resized_2)
    cv2.imshow("INTER_NEAREST image2", resized1_2)
    cv2.imshow("INTER_LINEAR image2", resized2_2)
    cv2.imshow("INTER_CUBIC image2", resized3_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()