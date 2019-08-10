
import numpy as np
import cv2
import time

#loads the video 
vidcap = cv2.VideoCapture('C:/Users/nigel/Desktop/ufc videos/ready to process/Top 20 Knockouts in UFC History.mp4')

#two copies of vidcap
success,image = vidcap.read()

#count hold the frame number, start holds the time. 
count = 0
start = time.time()

while success:
  #another time place holder, not sure why i need two.
  end = time.time()
  #im using start var and end var to round two decimal places in the video naming scheme.
  #I should do the math to convert this decimal into seconds. *60/100 ratio
  result = round((end-start),2)

  cv2.imwrite("D:/picture demo/20 knockouts/frame%d,%s.jpg" % (count,result), image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success,count)
  print(result)
  count += 1

'''
  #im combining count and result into one so i can control work flow with if statement.
  combine = float(count+result)
  if combine < 23.59:
    count+=1
    continue
  else:'''
