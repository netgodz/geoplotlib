import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox


#data = read_csv('somedata.csv')
#data = read_csv('data/loc-andrea-prod-resampled.csv')
data = read_csv('data/auser.csv')

geoplotlib.kde(data, bw=[10,10], cmap='hot', method='hist', scaling='lin', cut_below=92, clip_above=99, binsize=1)
#geoplotlib.kde(data, bw=[5,5], method='hist', scaling='log', cut_below=92, clip_above=99)

#geoplotlib.kde(data, bw=[15,15], cmap='hot', method='kde', scaling='lin', cut_below=92, clip_above=99, binsize=8)
#geoplotlib.kde(data, bw=[15,15], cmap='hot', method='kde', scaling='log', cut_below=92, clip_above=99, binsize=8)

#geoplotlib.scatter(data, color=[0,0,255], point_size=1)

geoplotlib.set_bbox(BoundingBox.DTU)
geoplotlib.show()