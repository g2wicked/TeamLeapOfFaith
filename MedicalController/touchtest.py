__author__ = 'Zach'

import Tkinter
from Tkinter import Frame, Canvas, YES, BOTH, Tk
from PIL import Image, ImageTk
import sys
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from win32api import GetSystemMetrics
screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)

class TouchPointListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

            # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_frame(self, controller):
        self.paintCanvas.delete("all")
        frame = controller.frame()

        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"

        interactionBox = frame.interaction_box

        for pointable in frame.pointables:
            normalizedPosition = interactionBox.normalize_point(pointable.tip_position)
            if(pointable.touch_distance > 0 and pointable.touch_zone != Leap.Pointable.ZONE_NONE):
                #color = self.rgb_to_hex((0, 255 - 255 * pointable.touch_distance, 0))
                color = "white"

            elif(pointable.touch_distance <= 0):
                #color = self.rgb_to_hex((-255 * pointable.touch_distance, 0, 0))
                #color = self.rgb_to_hex((255,0,0))
                color = "red"

            else:
                #color = self.rgb_to_hex((0,0,200))
                color = ""

            self.draw(normalizedPosition.x * screenWidth, screenHeight - normalizedPosition.y * screenHeight, 40, 40, color)

            # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/4:
                    clockwiseness = "clockwise"
                    color = "orange"
                else:
                    clockwiseness = "counterclockwise"
                    color = "blue"

                # Calculate the angle swept since the last frame
                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                #print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                        #gesture.id, self.state_names[gesture.state],
                        #circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                color = "black"
                #print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                        #gesture.id, self.state_names[gesture.state],
                        #swipe.position, swipe.direction, swipe.speed)

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                color = "green"
                #print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                        #gesture.id, self.state_names[gesture.state],
                        #keytap.position, keytap.direction )

            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = ScreenTapGesture(gesture)
                color = "red"
                #print "  Screen Tap id: %d, %s, position: %s, direction: %s" % (
                        #gesture.id, self.state_names[gesture.state],
                        #screentap.position, screentap.direction )

        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""

        self.draw(normalizedPosition.x * screenWidth, screenHeight - normalizedPosition.y * screenHeight, 40, 40, color)


    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

    def draw(self, x, y, width, height, color):
        self.paintCanvas.create_oval( x, y, x + width, y + height, fill = color, outline = "")

    def set_canvas(self, canvas):
        self.paintCanvas = canvas

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb

class PaintBox(Frame):

    def __init__( self ):
        Frame.__init__( self )
        self.leap = Leap.Controller()
        self.painter = TouchPointListener()
        self.leap.add_listener(self.painter)
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Medical App" )
        self.master.geometry( str(screenWidth) + 'x' + str(screenHeight))

        # create Canvas component
        self.paintCanvas = Canvas( self, width = screenWidth, height = screenHeight )
        self.paintCanvas.pack()
        self.painter.set_canvas(self.paintCanvas)

        # create second Canvas component
        self.backgroundCanvas = Canvas( self, width = screenWidth, height = screenHeight)
        self.paintCanvas.pack()
        self.painter.set_canvas(self.paintCanvas)

root = Tk()
im = Image.open('images/leatherBackground.png')
im = im.resize((screenWidth,screenHeight), Image.BILINEAR)
tkimage = ImageTk.PhotoImage(im)
myvar = Tkinter.Label(root,image = tkimage)
#myvar.place(x=0, y=0, relwidth=1, relheight=1)


def main():
    PaintBox().mainloop()

if __name__ == "__main__":
    main()