1) HSV vs RGB:
HSV allows computers to be less sensitive to the hue of a color, 
thus making image tracking slightly easier when dealing with shadows and differences in lighting.
Therefore, we typically want to use HSV over RGB when tracking based off of color.  

Threshold Range:
  
    # lower boundary RED color range values; Hue (0 - 10)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([10, 255, 255])
 
    # upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160,100,20])
    upper2 = np.array([179,255,255])

These are the color ranges and thresholds I used to create a mask for red coloration.  
They do a good job tracking reds and I can spot a waterbottle moving accross the screen.  

<img width="1269" alt="Screen Shot 2024-01-17 at 7 00 27 PM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/160221b4-2e65-4778-8932-5aa537224b87">

2) Lighting Condition
When my red waterbottle is being tracked in good lighting, lamp directly lighting the bottle, 
with a background that is dark or contrasting the red color, the image tracking is easier to handle.

3) Color Picker

<img width="766" alt="Screen Shot 2024-01-17 at 7 06 34 PM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/34f6a0be-4eaf-4eba-b1db-b804064733bc">

Changing the brightness of the screen can dramatically affect the way the computer senses the color on the screen.  
Making a small range can be quite difficult as the actual color emmitted by the phone is different than the color HSV value that the camera detects. 

4) Dominant Color Code
<img width="1269" alt="Screen Shot 2024-01-18 at 2 00 56 AM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/be9efda3-5a96-40fd-a877-d93cad4d5ecc">

<img width="1269" alt="Screen Shot 2024-01-18 at 2 02 36 AM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/e1ee3bc4-399e-495d-af1e-6e94ebb533c3">

   Placing the red object in the center changes the dominant color of whatever is inside the rectangle.
   Depending on where the object is in proximity to the center of the rectangle will determine much the dominant color changes.

   Using the phone and adjusting the brightness had a similar affect on the dominant color, though it was found that the color       displayed on the screen varied more dramatically than the color on screen after the object-test.  Perhaps this is suggesting      that simple, non contoured objects with defined color are easier to track that objects with shadows etc.  
   
