<h1 align="center"> Invisible Cloak For Achieving Invisibility </h1>


<hr>

### What is invisible cloak? ###
<i> Based on [Wikipedia,](https://en.wikipedia.org/wiki/Cloak_of_invisibility) </i>
A cloak of invisibility is a fictional theme. In folklore, mythology and fairy tales, a cloak of invisibility appears either as a magical item used by duplicitous characters or an item worn by a hero to fulfill a quest.
<br>


* You have seen invisible cloak type of cloth in ["Harry Potter"](https://en.wikipedia.org/wiki/Harry_Potter) movies a lot!
![Sample](img/sample.gif)
 Remember that now?

### Now the next question is, how can we make that fantasy true in a simple python programming script? ### 

Well, after going through the simple algorithm I'm providing here, you would say to yourself that it is so easy actually!
<br> 

1. After enabling the camera, capture the present frame and keep that as background frame. I'll provide very short amount of time for that.
2. Now the program would detect red colored object through the camera using our provided color detection algorithm. 
3. Through the previously generated mask, apply the previous mask on the new ongoing video by segmenting out the red colored cloth.
4. Now, it's the time for that magical effect, for what we've been waiting for! Generate the final output as directed in the python script.

<br>

### Special Modules ###
- OpenCV
- NumPy
- Time