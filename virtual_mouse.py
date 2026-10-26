import cv2 as cv
import mediapipe as mp
import pyautogui
import math
from pathlib import Path
import time

SCREENSHOT_FOLDER = Path("Screenshots")
SCREENSHOT_FOLDER.mkdir(parents=True, exist_ok=True)

PINCH_THRESHOLD = 0.08
pinch_was_active = False
fist_was_detected = False

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

if not cap.isOpened():
    print("Error: Could not open video stream.")
    hands.close()
    raise SystemExit

while True:
    success, frame = cap.read()

    if not success:
        print("Error: Could not read webcam frame.")
        break

    frame = cv.flip(frame, 1)

    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            index_base = hand_landmarks.landmark[5]
            index_middle_joint = hand_landmarks.landmark[6]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            pinky_tip = hand_landmarks.landmark[20]
            index_pip = hand_landmarks.landmark[6]
            middle_pip = hand_landmarks.landmark[10]
            ring_pip = hand_landmarks.landmark[14]
            pinky_pip = hand_landmarks.landmark[18]

            open_palm = (
                index_tip.y < index_pip.y
                and middle_tip.y < middle_pip.y
                and ring_tip.y < ring_pip.y
                and pinky_tip.y < pinky_pip.y
            )

            closed_fist = (
                index_tip.y > index_pip.y
                and middle_tip.y > middle_pip.y
                and ring_tip.y > ring_pip.y
                and pinky_tip.y > pinky_pip.y
            )

            if closed_fist:
                fist_was_detected = True

            if open_palm and fist_was_detected:
                timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = SCREENSHOT_FOLDER / f"screenshot_{timestamp}.png"

                screenshot = pyautogui.screenshot()
                screenshot.save(screenshot_path)

                print(f"Screenshot saved: {screenshot_path}")
                fist_was_detected = False

            middle_tip_distance = math.hypot(
                thumb_tip.x - middle_tip.x,
                thumb_tip.y - middle_tip.y
            )

            left_click_distance = math.hypot(
                thumb_tip.x - index_tip.x,
                thumb_tip.y - index_tip.y
            )

            right_click_distance = math.hypot(
                middle_tip.x - thumb_tip.x,
                middle_tip.y - thumb_tip.y
            )

            right_to_5 = math.hypot(
                middle_tip.x - index_base.x,
                middle_tip.y - index_base.y
            )

            double_distance_48 = math.hypot(
                thumb_tip.x - index_tip.x,
                thumb_tip.y - index_tip.y
            )

            double_distance_4_12 = math.hypot(
                thumb_tip.x - middle_tip.x,
                thumb_tip.y - middle_tip.y
            )

            DOUBLE_CLICK_THRESHOLD = 0.06

            double_click_active = (
                double_distance_48 < DOUBLE_CLICK_THRESHOLD
                and double_distance_4_12 < DOUBLE_CLICK_THRESHOLD
            )

            RIGHT_CLICK_THRESHOLD_4 = 0.08
            RIGHT_CLICK_THRESHOLD_5 = 0.08

            right_click_active = (
                right_click_distance < RIGHT_CLICK_THRESHOLD_4 
                and right_to_5 < RIGHT_CLICK_THRESHOLD_5
            )

            LEFT_CLICK_THRESHOLD = 0.04

            left_click_active = (
                left_click_distance < LEFT_CLICK_THRESHOLD
            )

            if not closed_fist:
                if double_click_active and not pinch_was_active:
                    pyautogui.doubleClick()

                elif right_click_active and not pinch_was_active:
                    pyautogui.rightClick()

                elif left_click_active and not pinch_was_active:
                    pyautogui.click()

            pinch_was_active = (
                double_click_active
                or right_click_active
                or left_click_active
            )

            distance_to_5 = math.hypot(
                thumb_tip.x - index_base.x,
                thumb_tip.y - index_base.y
            )

            distance_to_6 = math.hypot(
                thumb_tip.x - index_middle_joint.x,
                thumb_tip.y - index_middle_joint.y
            )

            FREEZE_THRESHOLD = 0.09

            freeze_cursor = (
                distance_to_5 < FREEZE_THRESHOLD
                and distance_to_6 < FREEZE_THRESHOLD
            )

            height, width, _ = frame.shape

            x = int(index_tip.x * width)
            y = int(index_tip.y * height)

            screen_x = int(x / width * screen_width)
            screen_y = int(y / height * screen_height)

            if not freeze_cursor:
                pyautogui.moveTo(screen_x, screen_y)

            cv.circle(
                frame,
                (x, y),
                10,
                (0, 255, 0),
                cv.FILLED
            )

    else:
        pinch_was_active = False

    cv.imshow("Webcam", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
hands.close()
cv.destroyAllWindows()
