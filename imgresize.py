import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
import sys

def loadGrayscale(path) -> np.ndarray:
    img = cv2.imread(path, 0) # cv2.IMREAD_GRAYSCALE

    if not img.any(): # Check for missing file
        raise FileNotFoundError(f"Image at {path} was not read")
     
    return img

def show(*images, titles=None):
    fig, axes = plt.subplots(1, len(images), squeeze=False)
    for ax, img in zip(axes[0], images):
        ax.imshow(img, cmap="gray", vmin=0, vmax=255)
        ax.set_axis_off()
    plt.show()

if __name__ == "__main__":
    p = sys.argv[1]
    arr = loadGrayscale(p)
    print(f"shape: {arr.shape}")
    print(f"dtype: {arr.dtype}")
    print(f"min  : {np.min(arr)}")
    print(f"max  : {np.max(arr)}")
    print(f"mean : {np.mean(arr)}")
    show(arr)