# TA_tracker

This is a program that helps TA decide which confused student to help when the TA is ready to help.<br />
There are two TAs, Oliver and Colleen and there are students who are approaching the students to solve their doubts <br />
Colleen solves student doubts on priority basis whereas Oliver does it in First-Come-First-Serve basis. <br />
Each line of this code has a O(log n) complexity.<br />
<br />
Input:
A line of the input may contain either of the following: <br />
  a. "Oliver ready" indicating Oliver is ready to solve the doubts <br />
  b. "Colleen ready" indicating Colleen is ready to solve the doubts <br />
  c. " Student_name confusion_level"  for example: Bob 3 indicating Bob is confused at level 3.<br />
<br /> 
Output:
Each line of output either tells if a student is looking for help or Oliver/Colleen helping the student <br />
At the end of the program, the list of unhelped students is displayed <br />
