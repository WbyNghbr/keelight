import cv2

fps = 25.
frame_width = 256
frame_height = 144

gst_pipeline = (
    "v4l2src ! video/x-raw, format=UYVY, interlace-mode=progressive, colorimetry=bt601, width=1920, height=1080, framerate=25/1 "
    "! videorate ! videoscale "
    "! video/x-raw, width=256, height=144, framerate=25/1 "
    "! videoconvert ! appsink"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
cap.set(cv2.CAP_PROP_FPS, fps)

if not cap.isOpened():
    print("Could not open video device")
    exit()

print("video capture pipeline initialized")



cap.release()
cv2.destroyAllWindows()
