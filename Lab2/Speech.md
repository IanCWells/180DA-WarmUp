Speech Program:

First I made sure the guess the word game was functioning properly.
Next I altered some of the word detections to be words like dog and cat.  This performed as expected (the computer was able to detect these two different words).

Limit Testing:
1) Two similar sounding words: sound, round
Results - Has more difficulty distinguishing between the two words in a loud setting.  It is best if the speech detection is in a quiet area and the user is particular with their enunciation.  

2) Letters (A,B,C,D,E,F)
Results - Each letter was distinguished, although the speech processing still took a long time.
It seems as though shorter letters might be hard to distinguish as the computer wants a few syllables in order to properly distinguish words.

<img width="400" alt="Screen Shot 2024-01-24 at 12 51 22 PM" src="https://github.com/IanCWells/180DA-WarmUp/assets/97809757/0fb24f52-8515-43be-9c59-cac8dcc6cfb2">

4) Phrases
Results - Brief phrases work with more accuracy than longer sentences.  As complexity increases, the speech processing seems to miss a few words when speaking into the mic.  Shorter syllable count also helps to minimize complexity.  

5) Music in Background
Results - Loud settings create a huge boundary for word and phrase detection.  The detection software started to struggle when noise was present in the system.

(a) What can you do with your given speech program in the project?
Use words like "start", "stop", or "pause" to begin playing stop playing, or pause the game.  Since these words are short and distinguishable, implementation seems relatively straight forward. Speech recognition should be used primarily in cases where lag time is not critical.  

(b) How complex do you want your speech recognition to be? How complex can you reasonably expect
your speech recognition to be?
Speech recognition can be used in several parts of the project, although each time it is used, the responses should not be time dependent, and further should be short and distinguishable. 

(c) What level of speech accuracy do you need? In other words, how quickly do you need an accurate
recognition? Does a missed recognition hurt the progress of the game?
Because speech recognition isn't perfect, it should be noted to use the recognition software in instances where word usage isn't critical.  Accurate recognition could

(d) Do you need specific hardware, specific conditions, etc. to have a reasonable confidence that it
works well enough?
Depending on how critical speech recognition is in our project, a microphone could be purchased to get a more localized sound detection.  A polar microphone would help to limit noise in a loud room.  
