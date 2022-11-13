# opencvCamLibTesting
Test program to explore functionality of OpenCV library for possible future usage when integrating camera for NASA student launch payload mission. 

# Usage
## initialTesting.py
- To use the camera, either press "i" to input sequences of instructions or "esc" to exit. 
- You will have to toggle between screens to select input or exit in your camera screen, and to type input.
- Make sure you update your path to be your current active directory where you are running the program (see comments in code).
## camTesting1 - camMain.py
- Run the program from the command line using 
  ```py camMain.py <yourdirectory>\opencvCamLibTesting\camTesting1```
- Example: ```py camMain.py C:\Users\bob\programs\opencvCamLibTesting\camTesting1```
## camTesting - camMain2.py
- This testing was done through ssh on a RaspberryPi Compute Module 4
- Adjust your paths for current directory in the file
- Use ```scp <filename> <username>@raspberrypi2:<directory>``` for all files
- Run the program from command line using 
```python3 camMain2.py```


# Functionalities tested (initialTesting, camTesting1)
- Take picture (c, C3)
- Grayscale (d, D4 = on, e, E5 = off)
- Flip 180 deg (f, F6)
- Apply any random filter (sharp filter) (g, G7 = on, h, H8 = off)

# Notes
- Initial testing done using laptop webcam.
- Also works with arducam connected to laptop.
- Next testing will be on raspberrypi with arducam via ssh
  - Update: taking photos/filtering was a success with some adjustments
  - Was missing certain downloads (numpy, opencv-python, libcblas) and had to work around with various versions of Python/Pip
  - Unable to pass path as a recognizable string as an argument in main method, adjusted program to use a set variable for path

