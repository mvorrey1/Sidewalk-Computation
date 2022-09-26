import pptk
import numpy as np
import pandas as pd

ptc = pd.read_csv("HD_Run1(0).csv")
ptcDf = pd.DataFrame(ptc)
xyz = ptcDf.filter(['X', 'Y', 'Z'])
intensity = ptcDf.filter(['Retro'])
intensity = np.array(intensity.Retro).transpose()

v = pptk.viewer(xyz)
v.attributes(intensity)
