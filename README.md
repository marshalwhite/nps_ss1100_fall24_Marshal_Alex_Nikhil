# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

### White Beyrooty Taniparti

### Assignment
- **Instructions**: Work in groups of four to complete the steps outlined in the project instructions.
- **Submission**: All of your submission will go here in this repository, to include this README file to hold your writeup.

### Procedure
#### Preparation
- Employ programming skills to solve problems related to spacecraft subsystems.
- Develop code and responses to tasks in various sections.
- Experience working with code and collaborating on a coding project.

#### Requirements
1. Complete all tasks listed in each section, paying attention to the Evaluation subsections.
2. Use MatLab to complete at least one of the tasks.
3. Submit the project using GitHub, replacing the content of this README file with your writeup and presentation of the work.

#### Subsystems and Tasks
Reaction Control Subsystem (RCS): Malfunction detection and velocity change calculation.\
Thermal Control Subsystem (TCS): Temperature control function.\
Attitude Control Subsystem (ACS): Attitude determination and rotation calculations.\
Command and Data Handling (C&DH): Command parsing and routing.\
Electrical Power Subsystem (EPS): Power budget analysis and battery charging calculations.\
Remote Sensing Payload: Data ingestion, radiance to reflectance conversion, and image rescaling.

#### Questions
1. What was your experience in collaborating? Talk about what steps you used to ensure the
inputs from group members worked - code testing, GitHub branch management, etc. - and
how you divided up the workload for the project.

  Our group divided the project into three separate sections giving each team member two total sections each to code. We completed our sections without much collaboration aside from occasional troubleshooting conducted in person in between classes. Once we had each compiled our own code, we uploaded our segments to a Test Branch created on our Github. We had at least one other person make sure that the code would run correctly before pushing our code to the Main Branch. ### White

2. What was the most challenging section, and why? Feel free to provide more than one response
if there is a difference of opinion in the group.

  We encountered the most issues when collaborating across PC and MAC users in our group. I suspect some degree of user error, but we encountered issues getting the code from the MAC to github. Our workaround was to the just send raw lines of code via email, but since there were formatting issues, the code had to be edited again to run without errors before being pushed to Github. ### White

3. If you employed Generative AI tools, how did you do so? Discuss which tools you used, the
prompts you utilized, how you ensured the results were valid, and how you integrated the code
into your tasks.

  ChatGPT made quick work of most of this assignment. It was very easy to upload the PDF instructions to the ChatGPT and then prompt it to write code for Python and Matlab for specific sections. Since the instructions were already very clear in the PDF, it didn’t require much additional prompting to get satisfactory results. ChatGPT was also very useful for troubleshooting and correcting any errors we encountered when double-checking another team member’s code. ### White

4. What other resources did you use to find solutions? Online sites, books, references, etc.

  ChatGPT was the only resource consulted to complete this assignment.

5. In what way could this project be improved for future quarters?

  Introducing the class to Github earlier in the course would be beneficial. Unfamiliarity with the website created some delay. Team members were confused on how to upload their code to the Github, how to differentiate between the Test and Main branches, and occasionally were unsuccessful in using Github altogether. Being able to become familiar with the website interface while still in class would have allowed ample time to avoid these issues. ### White


# Instructor Comments

### ADC
In your import statement of the ADC_py.py, you specified all of the function names from the rotate_me.py file. This allows you to call them without using the rotate_me.XXXX syntax, but one way to make it easier would be to use the "*" operator to get all of the functions by name:

from rotate_me import *

### C&DH
Great use of modular code with separate functions to split up the script into segments. Main comment I have is that you repeat certain objects (subsystems, commands, etc.) in multiple functions; if you instead wrote those in the main script, their scope would still be available in read-only form inside of the functions. That's actually desirable in some ways, since it would prevent your functions from accidentally overwriting those data.

When working with error handling, it is often useful to have a "catch-all" exception, in this case just to be sure it can catch errors other than ValueErrors (which is the only type of error that your code can handle as written). 

### EPS
Good use of default parameters and a dictionary as the output in your solar_power_and_energy() function. 

### TCS
In your dynamic_temperature_control, you use the same variable name (current_temp) as a variable declared in the main body of the script. This may result in unexpected behavior, although you do overwrite it with a new value. Recommend you use unique names inside functions that don't match ones on the outside of that scope, *unless* you actually intend to use that same variable's value (or modify it with *global*). I also think your *break* in the dynamic_temperature_control() function isn't correctly exiting the loop - it seems to run for 15 cycles no matter if it reaches the 0.1 threshold or not. I think the issue is with the abs(current_temp - target_temp) not correctly determining the adjustment difference. 

### Github
Good use of the test branch; it seems like you pushed everything to the main, so hopefully that worked well for you. Great responses and feedback on the main page.