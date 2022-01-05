"""
import cv2

img_file = 'Car Image4.jpg'
video = cv2.VideoCapture('video2.mp4')

classifier_file = 'car_detector3.xml'

img = cv2.imread(img_file)


car_tracker = cv2.CascadeClassifier(classifier_file)


black_n_white = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


# detect cars
cars = car_tracker.detectMultiScale(black_n_white)

print(cars)

# draw rect around the car

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


cv2.imshow('Robin Car Detector', img)


cv2.waitKey()


print("Code Completed")
"""

import cv2


# Just add your video file here
#vid_file = cv2.VideoCapture('car.mp4')
vid_file = cv2.VideoCapture('vid.mp4')


# Pre-Trained classifier
car_tracker = cv2.CascadeClassifier('car_detector3.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')


while True:
    # Read Video
    (read_successful, frame) = vid_file.read()
    if read_successful:
        # Convert to greyscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect Cars & Pedestrian
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    print("CARS:", cars)
    print("Pedestrain:", pedestrians)

    # Finding rectangle Area

    # def MyFn(a):

    #   return a[2]*a[3]

    def getSortedAreaOfEachFrame(items):

        sortedItems = sorted(items, key=lambda tup: tup[2], reverse=True)

        return sortedItems

    cars = getSortedAreaOfEachFrame(cars)

    print("Sorted Cars:", cars)

    frontCars = cars[: int(len(cars)/3)]

    backCars = cars[int(len(cars)/3):]

    pedestrians = getSortedAreaOfEachFrame(pedestrians)

    frontPedestrains = pedestrians[: int(len(pedestrians)/3)]

    backPedestrains = pedestrians[int(len(pedestrians)/3):]

    print("Fornt", frontCars)
    print("Back", backCars)

    # Draw square around the front cars
    for i in range(len(frontCars)):

        x = frontCars[i][0]

        y = frontCars[i][1]

        w = frontCars[i][2]

        h = frontCars[i][3]

        cv2.rectangle(frame, (x+1, y+1), (x+w, y+h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Draw square around the back cars
    for i in range(len(backCars)):

        x = backCars[i][0]

        y = backCars[i][1]

        w = backCars[i][2]

        h = backCars[i][3]

        cv2.rectangle(frame, (x+1, y+1), (x+w, y+h), (7, 164, 12), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (7, 164, 12), 2)

    # Draw square around the front cars
    for i in range(len(frontPedestrains)):

        x = frontPedestrains[i][0]

        y = frontPedestrains[i][1]

        w = frontPedestrains[i][2]

        h = frontPedestrains[i][3]

        cv2.rectangle(frame, (x+1, y+1), (x+w, y+h), (255, 165, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 165, 0), 2)

    # Draw square around the back cars
    for i in range(len(backPedestrains)):

        x = backPedestrains[i][0]

        y = backPedestrains[i][1]

        w = backPedestrains[i][2]

        h = backPedestrains[i][3]

        cv2.rectangle(frame, (x+1, y+1), (x+w, y+h), (75, 0, 130), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (75, 0, 130), 2)

    # Display the image
    cv2.imshow('Car & Pedestrian Detector', frame)

    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

    # Hold it so it won't autoclose


# Release the videoCapture object
vid_file.release()

print('Code Completed')
