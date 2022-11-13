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

# Functionalities tested (initialTesting, camTesting1)
- Take picture (c, C3)
- Grayscale (d, D4 = on, e, E5 = off)
- Flip 180 deg (f, F6)
- Apply any random filter (sharp filter) (g, G7 = on, h, H8 = off)

# Notes
- Initial testing done using laptop webcam.
- Also works with arducam connected to laptop.
- Next testing will be on raspberrypi with arducam via ssh


