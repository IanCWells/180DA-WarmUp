Task 1:

<img width="400" alt="blink" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/d0092ca4-f91f-4276-99ea-f6172b49e411">

The above image shows the microcontroller's response to the blink example code. 

<img width="400" alt="IMU lab4" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/e69f5386-161b-47b0-a678-d1757531d199">

Above are the IMU printouts for the second pazrt of task 1. 

Baseline script is referenced in the header comments of the IMU code labeled "ex.ino"

Task 2:

<img width="200" alt="Screen Shot 2024-02-19 at 2 52 10 PM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/45073cc6-55da-4557-b1c1-8255a2d61924">

<img width="200" alt="Screen Shot 2024-02-19 at 2 52 16 PM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/d5ec1c07-625b-4662-acb8-2250e6b98ff3">

Above is the wifi connection used in task 2.  The IP address and wifi are not shared in the screenshots. 

Task 3:

<img width="400" alt="Lab4IMU" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/48863919-d3e1-464d-a7df-d9e07df7be7c">

Above is the screenshot of the terminal printout of the MQTT connection.  
Ways to reduce lag include reducing the amount of readings taken, increasing delay in between readings, sending smaller messages accross the MQTT protocal. 
Some ways to get around lag will include incorperation of a turn based system and making our IMU take acceleration values less frequently.  

Task 4:

a)

To determine whether something is idle, it is best to use some form of decision tree 
Yes gravity is shown when idle.  Looking at the printouts from part 1 of this lab, we can verify that gravity in the z-direction is captured as roughly 9.62 m/s. Pitch roll and yaw are confirmed when the IMU is laying flat on a table.  

b)

<img width="400" alt="LAb4Forwards" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/04bcac6a-17d0-4c66-8516-9b73e7bf9c95">

Above is the terminal output of the implementation of a basic directional monitor.  
It outputs forwards or backwards based on what direction the IMU is moving. 
The logic for this code is a simply decision tree using if statements.  It tracks the acceleration and prints out a driection based on a posiitve or negative signed interger.   

c)

Tme implementation of the circular acceleration is the same as the code in part (c) of this lab.  A decision tree is used.  Idle was difficult to implement, and the combination of a decision tree and thresholding, an idle printout can be achieved.  

d) 

<img width="400" alt="LAb4Forwards" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/04bcac6a-17d0-4c66-8516-9b73e7bf9c95">

Above is the terminal output of the implementation of a basic directional monitor.  
It outputs forwards or backwards based on what direction the IMU is moving. 


