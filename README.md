# Remove_Shadow

Load the input image as grayscale.  
![Input Image](https://github.com/yashraj02/Remove_Shadow/blob/master/Input_Image/Shadow_Paper1.jpg?raw=true)  
  
Step 1  
Dilate the image, in order to get rid of the text. This step somewhat helps to preserve the bar code.  
![Output Image 1](https://github.com/yashraj02/Remove_Shadow/blob/master/Output_Images/Shadow_Paper2.jpg?raw=true)  
  
Step 2  
Median blur the result with a decent sized kernel to further suppress any text.  
This should get us a fairly good background image that contains all the shadows and/or discoloration.  
![Output Image 2](https://github.com/yashraj02/Remove_Shadow/blob/master/Output_Images/Shadow_Paper3.jpg?raw=true)  
  
Step 3  
Calculate the difference between the original and the background we just obtained. The bits that are identical will be black (close to 0 difference), the text will be white (large difference).  
Since we want black on white, we invert the result.  
![Output Image 3](https://github.com/yashraj02/Remove_Shadow/blob/master/Output_Images/Shadow_Paper4.jpg?raw=true)  
  
Step 4  
Normalize the image, so that we use the full dynamic range.  
![Output Image 4](https://github.com/yashraj02/Remove_Shadow/blob/master/Output_Images/Shadow_Paper5.jpg?raw=true)  
  
Step 5  
At this point we still have the paper somewhat gray. We can truncate that away, and re-normalize the image.  
![Output Image 5](https://github.com/yashraj02/Remove_Shadow/blob/master/Output_Images/Shadow_Paper6.jpg?raw=true)  
  
