import cv2

def main():

 img_rgb = cv2.imread("4.jpeg")  #读取图片
 img_color = img_rgb
 img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
 img_blur = cv2.medianBlur(img_gray, 7)
 #检测到边缘并且增强其效果
 img_edge = cv2.adaptiveThreshold(img_blur,255,
          cv2.ADAPTIVE_THRESH_MEAN_C,
          cv2.THRESH_BINARY,
          blockSize=9,
          C=2)
 #转换回彩色图像
 img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
 img_cartoon = cv2.bitwise_and(img_color, img_edge)
 # 保存转换后的图片
 cv2.imshow("out", img_cartoon)
 cv2.waitKey(0)


if __name__ == '__main__':
     main()
