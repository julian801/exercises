
from scipy.misc import imread, imshow
import numpy as np

logo = imread('python_logo.png', mode='RGB')

black = np.zeros((20, 20))
white = np.ones((20, 20))

bw = np.hstack([black, white])
wb = np.hstack([white, black])
bwwb = np.vstack([bw, wb])

checker = np.tile(bwwb, (5, 5))

logo[:,:,0] = logo[:,:,0] * checker
imshow(logo)

# source: www.academis.eu