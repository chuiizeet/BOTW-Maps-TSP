# BOTW-Maps-TSP
TSP applied to The Legend of Zelda maps: BOTW using opencv.

**Tested in python 3.7**

![tsp](https://i.imgur.com/zAuvoO0.gif)

## Maps
- Fairy Fountains.
- Memories.
- Shrines.

## Requirements
- opencv-python
- numpy
- matplotlib

```
pip install -r requirements.txt
```

## How to use
```
python3 main.py
```
Select a map from the list.

The output will show the route, the distance and the optimal coordinates using the nearest neighbor.

Only the image with the optimal tour will be shown.
