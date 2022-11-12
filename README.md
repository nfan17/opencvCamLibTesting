# opencvCamLibTesting
Test program to explore functionality of OpenCV library for possible future usage when integrating camera for NASA student launch payload mission. 

# Usage
## initialTesting.py
- To use the camera, either press "i" to input sequences of instructions or "esc" to exit. 
- You will have to toggle between screens to select input or exit in your camera screen, and to type input.
- Make sure you update your path to be your current active directory where you are running the program (see comments in code).
## camTesting1.py
- Run the program from the command line using 
  ```py camMain.py <yourdirectory>\opencvCamLibTesting\camTesting1```
- Example: ```py camMain.py C:\Users\bob\programs\opencvCamLibTesting\camTesting1```

# Functionalities tested
- Take picture (c)
- Grayscale (d = on, e = off)
- Flip 180 deg (f)
- Apply any random filter (sharp filter) (g = on, h = off)

# Notes
- Initial testing done using laptop webcam.
- Also works with arducam connected to laptop.
- Next testing will be on raspberrypi with arducam via ssh


