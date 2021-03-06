import cv2
import numpy as np
from matplotlib import pyplot as plt

def color_space_demo(image1):
    img_BGR = cv2.cvtColor(image1, cv2.COLOR_RGB2BGR) # BGR
    plt.subplot(3,3,1); plt.imshow(img_BGR);plt.axis('off');plt.title('BGR')
    
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)#RGB
    plt.subplot(3,3,2); plt.imshow(img_RGB);plt.axis('off');plt.title('RGB')
    
    img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)#GRAY
    plt.subplot(3,3,3); plt.imshow(img_GRAY, cmap=plt.cm.gray);plt.axis('off');plt.title('GRAY')
    
    img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)#HSV
    plt.subplot(3,3,4); plt.imshow(img_HSV);plt.axis('off');plt.title('HSV')
    
    img_YcrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)#YCrCb
    plt.subplot(3,3,5); plt.imshow(img_YcrCb);plt.axis('off');plt.title('YcrCb')
    
    img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)#HLS
    plt.subplot(3,3,6); plt.imshow(img_HLS);plt.axis('off');plt.title('HLS')
    
    img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)#XYZ
    plt.subplot(3,3,7); plt.imshow(img_XYZ);plt.axis('off');plt.title('XYZ')
    
    img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)#LAB
    plt.subplot(3,3,8); plt.imshow(img_LAB);plt.axis('off');plt.title('LAB')
    
    img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)#YUV
    plt.subplot(3,3,9); plt.imshow(img_YUV);plt.axis('off');plt.title('YUV')
    plt.show()

def channels_splib_merge(image2):
    b, g, r = cv2.split(image2)#提取RGB通道
    
    zeros = np.zeros(image2.shape[:2],dtype="uint8") #创建于image相同大小的零矩阵

    cv2.imshow("BLUE",cv2.merge([b, zeros, zeros]))
    cv2.imshow("GREEN",cv2.merge([zeros, g, zeros]))
    cv2.imshow("RED",cv2.merge([zeros, zeros, r]))

    merge_image = cv2.merge([b,g,r])

    cv2.imshow("merge_image",merge_image)

if __name__ == '__main__':

    img = cv2.imread('yuner.jpg',1)
    cv2.imshow("yuner",img)

    color_space_demo(img)
    channels_splib_merge(img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()