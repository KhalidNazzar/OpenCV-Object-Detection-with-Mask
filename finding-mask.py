import cv2


def none(x):
    pass

cv2.namedWindow('Track Bars', cv2.WINDOW_NORMAL)

cv2.createTrackbar('min_blue', 'Track Bars', 0, 255, none)
cv2.createTrackbar('min_green', 'Track Bars', 0, 255, none)
cv2.createTrackbar('min_red', 'Track Bars', 0, 255, none)

cv2.createTrackbar('max_blue', 'Track Bars', 0, 255, none)
cv2.createTrackbar('max_green', 'Track Bars', 0, 255, none)
cv2.createTrackbar('max_red', 'Track Bars', 0, 255, none)

# while True:
#     if cv2.waitKey(0):
#         break


image_BGR = cv2.imread('objects-to-detect.jpg')

image_BGR = cv2.resize(image_BGR, (600, 426))

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image_BGR)

image_HSV = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2HSV)

cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)
cv2.imshow('HSV Image', image_HSV)

while True:

    min_blue = cv2.getTrackbarPos('min_blue', 'Track Bars')
    min_green = cv2.getTrackbarPos('min_green', 'Track Bars')
    min_red = cv2.getTrackbarPos('min_red', 'Track Bars')

    max_blue = cv2.getTrackbarPos('max_blue', 'Track Bars')
    max_green = cv2.getTrackbarPos('max_green', 'Track Bars')
    max_red = cv2.getTrackbarPos('max_red', 'Track Bars')

    mask = cv2.inRange(image_HSV,
                       (min_blue, min_green, min_red),
                       (max_blue, max_green, max_red))

    cv2.namedWindow('Binary Image with Mask', cv2.WINDOW_NORMAL)
    cv2.imshow('Binary Image with Mask', mask)

    # Breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


# Printing final chosen Mask numbers
print('min_blue, min_green, min_red = {0}, {1}, {2}'.format(min_blue, min_green,
                                                            min_red))
print('max_blue, max_green, max_red = {0}, {1}, {2}'.format(max_blue, max_green,
                                                            max_red))

