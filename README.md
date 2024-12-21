Welcome to our innovative project: a Virtual Hand-Gesture Based Calculator powered by OpenCV and cvzone. This cutting-edge application leverages computer vision technology to create an intuitive, touchless interface for performing mathematical calculations. By combining the power of OpenCV for image processing and cvzone for hand tracking, we've developed a system that translates hand gestures into calculator inputs, revolutionizing the way we interact with digital tools.
This code implements a virtual hand gesture-based calculator using OpenCV and the `cvzone` library for hand tracking. Here's a breakdown of the components:

1. Button Class: This class defines each button on the calculator. Each button has a position, size, and a label (value). The `draw` method draws the button on the screen, and the `checkClick` method checks if the button is clicked by the user's hand.

2. **Button Grid**: The `buttonListValues` array defines the labels of the buttons in a grid format. The `buttonList` stores the instances of the `Button` class, with each button placed on the screen based on the grid positions.

3. **Hand Detection**: The `HandDetector` from `cvzone` is used to detect the user's hand and track the positions of the index and middle fingers. The distance between these two fingers is calculated to determine whether a "click" is made.

4. **Input Handling**: When a click is detected (distance between the fingers is less than a threshold), the code checks which button was clicked and updates the equation displayed on the screen. Special operations like clear (`C`), backspace (`AC`), negation (`+/-`), and evaluation (`=`) are implemented.

5. **Display**: The equation is continuously updated and displayed on the screen. The buttons are also drawn at predefined positions. The OpenCV window is set to fullscreen, and the program continuously captures frames from the webcam to detect hand gestures and interact with the calculator.

6. **Controls**: The user can press 'C' to clear the screen or 'q' to quit the application.

In summary, the code creates a virtual calculator that can be controlled using hand gestures, making it an interactive and hands-free way to perform calculations.
