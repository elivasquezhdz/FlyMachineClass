# FlyMachineClass
Python Based Image Classification of 2 Classes: Drones &amp; Airplanes

It was trained using Tensorflow and Google Images.
It needs tensorflow to work: https://www.tensorflow.org/
It also needs the following file to work properly:
https://drive.google.com/file/d/0B9TqKLs79cNgNkdlU1N1MmV0WjQ/view?usp=sharing

Donwload the file and copy it in the same directory for the rest of the files.
To use it type:
python3 FlyClass.py "imageName.jpg"

Where "imageName.jpg" is the name of the file image to classify.
It will print the results as:

Predictions:
drone   airplane
XXXXX       XXXXXX
----------------------
And will save a csv file as imageName.jpg.csv with the predictions.
