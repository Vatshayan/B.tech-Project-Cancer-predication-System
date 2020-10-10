"""
Thus the data frame is made of 97 observations on 9 variables:
lcavol: log cancer volume
lweight: log prostate weight
age: patient age in years
lbph: log amount of benign prostatic hyperplasia
svi: seminal vesicle invasion
lcp: log of capsular penetration
gleason: Gleason score
pgg45: percent of Gleason score 4 or 5
lpsa: log prostate specific antigen
The goal is to find models predicting the response lpsa.
"""

import numpy as np
import pandas as pd
from sklearn import linear_model, metrics, model_selection
from sklearn.linear_model import ElasticNet
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

# For full Project Code. Please Mail me now( vatshayan007@gmail.com )
# I reply mails very soon!
# Happy to help you.