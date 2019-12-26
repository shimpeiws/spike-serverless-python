try:
    import unzip_requirements
except ImportError:
    pass

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
import cv2
import urllib.request

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    with urllib.request.urlopen(url) as resp:
        s = resp.read()
        image = np.asarray(bytearray(s), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # return the image
        return image

def main(event, context):
    # numpy
    print("THIS IS FROM numpy!!!")
    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)

    # sklearn
    print("THIS IS FROM sklearn!!!")
    lr = LogisticRegression(penalty='l1')
    print('Default representation:')
    print(lr)
    # LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
    #                    intercept_scaling=1, l1_ratio=None, max_iter=100,
    #                    multi_class='auto', n_jobs=None, penalty='l1',
    #                    random_state=None, solver='warn', tol=0.0001, verbose=0,
    #                    warm_start=False)

    set_config(print_changed_only=True)
    print('\nWith changed_only option:')
    print(lr)
    # LogisticRegression(penalty='l1')

    #opencv
    print("THIS IS FROM opencv!!!")
    image = url_to_image("https://stickershop.line-scdn.net/stickershop/v1/product/3242305/LINEStorePC/main.png")
    height, width, channels = image.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': '{"message": "Hello from AWS Lambda"}'
    }

if __name__ == "__main__":
    main('', '')