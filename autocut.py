import cv2
from os import listdir

# Loading cat-face detector
cat_path = 'haarcascade_frontalcatface.xml'
face_cascade = cv2.CascadeClassifier(cat_path)


def read_img(img_name):
    '''Read the pictures, grayscale'''
    img = cv2.imread(img_name)
    return img


def get_face(img):
    '''Cat face recognition'''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.02,
        minNeighbors=3,
        minSize=(150, 150),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces


def face_rect(faces, img):
    '''Face rectangle'''
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, 'Cat', (x, y - 7), 3, 1.2,
                    (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Cat?', img)
    cv2.waitKey(0)


def cut_img(img_in: str, img_out: str) -> bool:
    '''Cut cat face'''
    img = read_img(img_in)
    if img is not None:
        faces = get_face(img)
    else:
        raise FileNotFoundError
    cut_img = None
    # print(faces)
    if not len(faces):
        print(f'No faces found for "{img_in}".')
        return False
    for (x, y, w, h) in faces:
        cut_img = img[y: y + h, x: x + w]
    cv2.imwrite(img_out, cut_img)
    return True


def cut_imgs(path_in: str, path_out: str) -> tuple[int]:
    '''Cut cat faces in a directory'''
    succ = 0
    cnt = 0
    path_in += '/'
    path_out += '/'
    for f in listdir(path_in):
        if f.endswith('.jpg'):
            cnt += 1
            succ += cut_img(path_in + f, path_out + f)
    return succ, cnt
    

if __name__ == '__main__':
    # fname = 'IMG_001.jpg'
    # cut_img('testcut/original/' + fname, 'testcut/cutted/' + fname)
    succ, cnt = cut_imgs('testcut/original', 'testcut/cutted')
    print(f"{succ}/{cnt} ({succ/cnt*100}%)")

