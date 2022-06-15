from pytube import YouTube
import cv2

def down(url):
    st = YouTube(url).streams.first()
    print(st.title, st._filesize, 'downloading...')
    st.download()
    # YouTube(url).streams.first().download()

def cap(path):
    vc = cv2.VideoCapture(path)
    fps = int(vc.get(cv2.CAP_PROP_FPS))
    print(f'fps = {fps}')
    count = 0
    while True:
        for i in range(fps):
            success, image = vc.read()
        if not success:
            break
        cv2.imwrite("frame%d.jpg" % count, image)
        print(f'\rFrame {count}', end='')
        count += 1


cap('yellow.mp4')

'''
url_list = open('test.txt', 'r').read().split('\n')
print(url_list)
for url in url_list: do(url)
'''
