
<img width="1134" alt="OG PUB:SUB" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/354ceed2-e18a-4976-a52e-22f9f6c22f0f">
The above shows two terminal communications hosted on my own laptop computer.  
The topic is the same as the standard for the class, often the subscriber will recieve messages from different publishers.  

<img width="1130" alt="Incrementing a Counter" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/91ad772a-5744-461d-a62a-f3569c6ae318">
The above shows implementation of a counter variable.  Each time a message is published, the subscriber saves the message as an integer and increments the count by 1. 

The image above is a screen shot of communication with a partner.  Partner: Bianca Mittu

The above image is an example of four way communication. 

Four way communication increases complexity and the lag time of the messages being sent and recieved. 
For the project, it seems that MQTT has the ability to update variables and counters between two computers.  This would essentially allow for multiplayer games where score, location, and other variables could be tracked.  It is important to note that lag in MQTT makes the choice of variables important.  Updating score doesn't necessarily need to happen instananeously (so a lag time is ok).  Depending on the game, position tracking could be a critical to happen as fast as possible (therefore MQTT lag could be harmful).  MQTT is great for sending non-vital, simple variables and strings between few networks.  Although, with more networks and complex data, MQTT might struggle sending data with minimal lag.  Depending on what needs to be transmit, a different method of communication may need to be selected.   
