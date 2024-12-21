import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 0), 5)
            return True
        else:
            return False

# Buttons
buttonListValues = [['C', '+/-', '%', '/'],
                    ['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '.', '=', 'AC']]

buttonList = []
buttonWidth = 100  # Further reduced width for better fit
buttonHeight = 100  # Further reduced height for better fit
for y in range(5):
    for x in range(4):
        xpos = x * buttonWidth + 850  # Adjusted starting x position
        ypos = y * buttonHeight + 150  # Adjusted starting y position
        if buttonListValues[y][x] != '':
            buttonList.append(Button((xpos, ypos), buttonWidth, buttonHeight, buttonListValues[y][x]))

# Variables
myEquation = ''
delayCounter = 0

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # Set width for full HD
cap.set(4, 1080)  # Set height for full HD
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Set OpenCV window to full-screen
cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Draw All
    cv2.rectangle(img, (850, 50), (850 + 400, 50 + 100),  # Adjusted display position and size
                  (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (850, 50), (850 + 400, 50 + 100),
                  (50, 50, 50), 3)

    for button in buttonList:
        button.draw(img)

    # Check for Hand
    if hands:
        # Find distance between index and middle fingers
        lmList = hands[0]['lmList']
        p1 = lmList[8][:2]  # Extract the (x, y) coordinates of the index finger tip
        p2 = lmList[12][:2]  # Extract the (x, y) coordinates of the middle finger tip
        length, _, img = detector.findDistance(p1, p2, img)
        print(length)
        x, y = lmList[8][:2]  # Use the index finger tip coordinates

        # If clicked, check which button and perform action
        if length < 50 and delayCounter == 0:
            for button in buttonList:
                if button.checkClick(x, y):
                    myValue = button.value  # get correct number
                    if myValue == '=':
                        try:
                            myEquation = str(eval(myEquation))
                        except:
                            myEquation = "Error"
                    elif myValue == 'C':  # Clear the equation
                        myEquation = ''
                    elif myValue == 'AC':  # Clear the last digit
                        myEquation = myEquation[:-1]
                    elif myValue == '+/-':  # Negate the current number
                        if myEquation and myEquation[-1].isdigit():
                            myEquation = str(-1 * int(myEquation))
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # to avoid multiple clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Write the Final answer
    cv2.putText(img, myEquation, (860, 120), cv2.FONT_HERSHEY_PLAIN,
                4, (0, 0, 0), 4)  # Adjusted for full-screen

    # Display
    key = cv2.waitKey(1)
    cv2.imshow("Image", img)
    if key == ord('c'):
        myEquation = ''
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
