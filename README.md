DISCUSSION

WHY THE PROBLEM SELECTION ?

We selected these cases which are the Bird Seed and Rice Grains image because the objects are not only numerous but also extremely crowded. In Digital Image Processing, the difficulty increases when the background disappeares. The Rice Grains provided a baseline for simple separation, while the Bird Seeds represented a worst-case scenario for segmentation. 
Counting isolated objects is a trivial task as we could not get the number counting right because the objects is overlappining. However, counting overlapping and touching objects is a significant engineering challenging. Simple thresholding or basic erosion often fail because they keep large clusters as a sing blob. We chose this case to demonstrate the implement of watershed method, which is the  solution for object separation.

WHAT THE RESULT TELL US?

Our results clearly show that Morphology alone is insufficient for dense datasets. As seen in the "After Morphology" output for the bird seeds, many seeds are merged into large white shapes. The Watershed algorithm separated the seeds using the Distance Transform topography to draw boundaries precisely where two seeds meet. We found 71 seeds tells us our Distance Transform was successful in finding the center of every seed even in a dense pile.
