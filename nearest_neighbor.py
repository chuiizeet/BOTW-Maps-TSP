import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import time

best_distance = 0.0
best_tour = []


def display(img,d):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    plt.title('Distance = '+str(d))
    ax.imshow(img)
    plt.show()

def draw_tsp(map,d,tsp,points):
    copy_map = map.copy()
    for line in range (0,len(tsp)-1):
        last = line+1
        # print(points[tsp[line]],points[tsp[last]])
        if last == len(tsp)-1:
            last = 0
            cv2.line(copy_map,
                     pt1=points[tsp[line]],
                     pt2=points[tsp[last]],
                     color=(255,0,0),
                     thickness=4)
        else:
            cv2.line(copy_map,
                     pt1=points[tsp[line]],
                     pt2=points[tsp[last]],
                     color=(255,0,0),
                     thickness=4)

    display(copy_map,d)

def nearest_neightbor(inputMap):

    maps_dots = ['fountains_dots','memories_dots','shrines_dots']
    maps = ['fountains.png','memories.png','shrines.png']

    img = cv2.imread('outputs/'+str(maps_dots[int(inputMap)])+'.png',0)
    dots = np.zeros(img.shape,dtype=np.uint8)
    map = cv2.imread('maps/'+str(maps[int(inputMap)]))
    map_rgb = cv2.cvtColor(map,cv2.COLOR_BGR2RGB)

    #####################################
    ########    GET POINTS    ###########
    #####################################

    image,contours,hierarchy = cv2.findContours(img,
                     cv2.RETR_CCOMP,
                     cv2.CHAIN_APPROX_SIMPLE)
    # Centroids
    mnts  = [cv2.moments(cnt) for cnt in contours]
    centroids = [( int(round(m['m10']/m['m00'])),int(round(m['m01']/m['m00'])) ) for m in mnts]

    points = []
    dots = np.zeros(img.shape)
    for c in centroids:
        cv2.circle(img=map_rgb,center=c,radius=8,color=(0,255,0),thickness=-1)
        points.append(c)

    f = 0
    while f < len(points):

        x = []
        y = []

        for i in points:
            x.append(i[0])
            y.append(i[1])

        eu = []
        tsp = []

        for j in range (0,len(x)):
            last = j+1
            if last == len(x)-1:
                last = 0
                s = (pow(x[f]-x[j],2) + pow (y[f]-y[j],2)) #N
                eu.append(math.sqrt(s))

            else:
                s = (pow(x[f]-x[j],2) + pow (y[f]-y[j],2)) #N
                eu.append(math.sqrt(s))

        # Sort indices
        _indexSort = np.array(np.argsort(eu))

        # Tour TSP
        indexSort = list(_indexSort)

        for x in range (0,len(indexSort)):
            tsp.append(int(indexSort[x]))

        # Insert
        tsp.insert(len(tsp),f)


        # Last distance
        _lTour = points[tsp[len(tsp)-1]]
        _lTour2 = points[tsp[len(tsp)-2]]
        s = (pow(_lTour[0]-_lTour2[0],2) + pow (_lTour[1]-_lTour2[1],2))
        eu.append(math.sqrt(s))

        # Distance
        distance = sum(eu)

        # Draw lines (All routes)
        #draw_tsp(map_rgb,distance,tsp,points)

        # Best distance & tour
        global best_distance, best_tour

        if f == 0:
            best_distance = distance
            best_tour = tsp

        if(distance < best_distance):
            best_distance = distance
            best_tour = tsp

        # Feels
        f += 1

    print('\n')
    print('Distance: ',best_distance)
    print('Best tour: ',best_tour)
    print('\n')
    print('Tour coordinates:')
    print('--------------------')
    for r in best_tour:
        print(points[r])

    # Print optimal tour
    draw_tsp(map_rgb,best_distance,best_tour,points)
