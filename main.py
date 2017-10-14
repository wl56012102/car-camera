import cv2
import time

font = cv2.FONT_HERSHEY_SIMPLEX


def draw_co(co, frame):
    co_x = 300
    cv2.putText(frame, "CO", (10, 340), font, 0.5, (0, 255, 0), 1)
    for i in range(1, co):
        if(i<3):
            cv2.rectangle(frame, (10, co_x), (30, co_x + 20), (0, 255, 0), -1)
        if(i>=3 and i <6):
            cv2.rectangle(frame, (10, co_x), (30, co_x + 20), (0, 255, 255), -1)
        if(i>=6):
            cv2.rectangle(frame, (10, co_x), (30, co_x + 20), (0, 0, 255), -1)
        co_x -= 30


def draw_co2(co2, frame):
    cv2.putText(frame, "CO2", (40, 340), font, 0.5, (0, 255, 0), 1)
    co2_x = 300
    for i in range(1, co2):
        if (i < 3):
            cv2.rectangle(frame, (40, co2_x), (60, co2_x + 20), (0, 255, 0), -1)
        if (i >= 3 and i < 6):
            cv2.rectangle(frame, (40, co2_x), (60, co2_x + 20), (0, 255, 255), -1)
        if (i >= 6):
            cv2.rectangle(frame, (40, co2_x), (60, co2_x + 20), (0, 0, 255), -1)
        co2_x -= 30


def draw_tem(tem, frame):
    cv2.putText(frame, "tem", (610, 340), font, 0.5, (0, 255, 0), 1)
    tem_x = 300
    for i in range(1, tem):
        if (i < 3):
            cv2.rectangle(frame,(610, tem_x),(630, tem_x + 20), (0, 255, 0), -1)
        if (i >= 3 and i < 6):
            cv2.rectangle(frame, (610, tem_x), (630, tem_x + 20), (0, 255, 255), -1)
        if (i >= 6):
            cv2.rectangle(frame, (610, tem_x), (630, tem_x + 20), (0, 0, 255), -1)
        tem_x -= 30


def draw_hum(hum, frame):
    cv2.putText(frame, "hum", (570, 340), font, 0.5, (0, 255, 0), 1)
    hum_x = 300
    for i in range(1, hum):
        if (i < 3):
            cv2.rectangle(frame,(580, hum_x),(600, hum_x + 20), (0, 255, 0), -1)
        if (i >= 3 and i < 6):
            cv2.rectangle(frame, (580, hum_x), (600, hum_x + 20), (0, 255, 255), -1)
        if (i >= 6):
            cv2.rectangle(frame, (580, hum_x), (600, hum_x + 20), (0, 0, 255), -1)
        hum_x -= 30


def draw_dis(frame):
    x1, y1 = 100, 480
    x2, y2 = 540, 480
    cv2.line(frame, (x1, y1), (x1 + 50, y1 - 80), (0, 0, 255), 3)
    cv2.line(frame, (x2, y2), (x2 - 50, y2 - 80), (0, 0, 255), 3)
    cv2.line(frame, (x1 + 50, y1 - 80), (x1 + 100, y1 - 80), (0, 0, 255), 3)
    cv2.line(frame, (x2 - 50, y2 - 80), (x2 - 100, y2 - 80), (0, 0, 255), 3)
    cv2.putText(frame, "STOP", (240, 440), font, 2, (0, 0, 255), 3)
    cv2.line(frame, (x1 + 50, y1 - 80), (x1 + 100, y1 - 160), (0, 255, 255), 3)
    cv2.line(frame, (x2 - 50, y2 - 80), (x2 - 100, y2 - 160), (0, 255, 255), 3)
    cv2.line(frame, (x1 + 100, y1 - 160), (x1 + 140, y1 - 160), (0, 255, 255), 3)
    cv2.line(frame, (x2 - 100, y2 - 160), (x2 - 140, y2 - 160), (0, 255, 255), 3)

    cv2.line(frame, (x1 + 100, y1 - 160), (x1 + 150, y1 - 240), (0, 255, 0), 3)
    cv2.line(frame, (x2 - 100, y2 - 160), (x2 - 150, y2 - 240), (0, 255, 0), 3)
    cv2.line(frame, (x1 + 150, y1 - 240), (x1 + 180, y1 - 240), (0, 255, 0), 3)
    cv2.line(frame, (x2 - 150, y2 - 240), (x2 - 180, y2 - 240), (0, 255, 0), 3)


def switch_mode():
    if key == ord('z'):
        data_mode = 0
    if key == ord('x'):
        data_mode = 1
    if key == ord('c'):
        data_mode = 2
    if key == ord('v'):
        data_mode = 3


def change_data(data, data_mode):
    if key == ord('w'):
        data[data_mode] += 1
    if key == ord('s'):
        data[data_mode] -= 1


def main():
    img_gench = cv2.imread('./gench.jpg')
    img_danger = cv2.imread('./danger.jpg')

    img_gench_gray = cv2.cvtColor(img_gench, cv2.COLOR_BGR2GRAY)
    img_danger_gray = cv2.cvtColor(img_danger, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img_gench_gray, 175, 255, cv2.THRESH_BINARY)
    ret, mask1 = cv2.threshold(img_danger_gray, 175, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    mask1_inv = cv2.bitwise_not(mask1)

    rows, cols, chanels = img_gench.shape
    rows1, cols1, chanels1 = img_danger.shape
    co_data = 5
    co2_data = 5
    hum_data = 5
    tem_data = 5
    data_mode = 0
    data = [co_data, co2_data, hum_data, tem_data]
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        roi = frame[0:rows, 0:cols]
        roi1 = frame[30:30 + rows1, 220:220 + cols1]
        frame_bg = cv2.bitwise_and(roi, roi, mask=mask)
        frame_fg = cv2.bitwise_and(img_gench, img_gench, mask=mask_inv)
        frame_bg1 = cv2.bitwise_and(roi1, roi1, mask=mask1)
        frame_fg1 = cv2.bitwise_and(img_danger, img_danger, mask=mask1_inv)
        dst = cv2.add(frame_bg, frame_fg)
        dst1 = cv2.add(frame_bg1, frame_fg1)
        if (data[0] > 6 or data[1] > 6 or data[2] > 6 or data[3] > 6):
            frame[30:30 + rows1, 220:220 + cols1] = dst1
        frame[0:rows, 0:cols] = dst

        draw_co(data[0], frame)
        draw_co2(data[1], frame)
        draw_hum(data[2], frame)
        draw_tem(data[3], frame)
        draw_dis(frame)
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, str(now), (10, 450), font, 0.5, (255, 255, 255), 1)

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow("frame", frame)

        key = cv2.waitKey(5) & 0xff
        if key == ord("q"):
            break
        if key == ord('z'):
            data_mode = 0
        if key == ord('x'):
            data_mode = 1
        if key == ord('c'):
            data_mode = 2
        if key == ord('v'):
            data_mode = 3
        if key == ord('w'):
            data[data_mode] += 1
        if key == ord('s'):
            data[data_mode] -= 1

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
