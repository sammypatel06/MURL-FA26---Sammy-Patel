import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
import sys

def loadGrayscale(path) -> np.ndarray:
    img = cv2.imread(path, 0) # cv2.IMREAD_GRAYSCALE
    if not img: raise FileNotFoundError(f"Image not found at {path}") # Missng file 
    return img

def show(*images, titles=None):
    fig, axes = plt.subplots(1, len(images), squeeze=False)
    for ax, img in zip(axes[0], images):
        ax.imshow(img, cmap="gray", vmin=0, vmax=255)
        ax.axis("off") # removes ticks on axes
    if titles:
        for ax, t in zip(axes[0], titles):
            ax.set_title(t)
    plt.tight_layout()
    plt.show()

def isDarkOnLight(gray) -> bool:
    # Take border strip (outer 5% of rows and cols)
    # Compute median 
    # Compare to 127
    pass

def binarize(img):
    blur = cv2.GaussianBlur(img, (5,5), 0)
    ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

if __name__ == "__main__":
    p = sys.argv[1]
    arr = loadGrayscale(p)
    print(f"shape: {arr.shape}")
    print(f"dtype: {arr.dtype}")
    print(f"min  : {arr.min()}")
    print(f"max  : {arr.max()}")
    print(f"mean : {arr.mean()}")
    show(arr)