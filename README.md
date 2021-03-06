# MaskCoco
MaskCoco is a simple script that parse masked images to coco format for object segmentation. 

## Install
Simply run the following in terminal
```
git clone https://github.com/georgezywang/MaskCoco.git
```
Additionally, this script expects the following libraries:
```
pathlib #pip install pathlib
PIL
numpy
skimage
shapely
```
as well as some built in ones. Use conda or pip to install missing dependencies

## Play with the Demo
The demo parses a mask of a wave image[1] and displays an annotated image.
Wave Image   |  mask
:-------------------------:|:-------------------------:
![Alt text](images/001_rgb.png "Wave Image")  |  ![Alt text](images/001_gt.png "Mask")

The wave image is the original image to be segmented, and the mask captures the wave. These images can both be found in the images folder.

To play with this demo, run the following:
```
cd MaskCoco
python3 driver.py
```
Open `demo.ipynb` and run the cell. An annotated wave image should appear. A bounding box and a mask should be present in the image.

<p align="center">
  <img src="resources/display.jpg">
</p>
<p align = "center">
Annotated Wave Image
</p>

The visualizer was taken from kaggle [2]. To change the mask's color, or display more information, please visit the link in the references section. To visualize more complicated images, i.e. those with a lot of polygons, consider using the alternative detectron2 visualization tool in `demo.ipynb`. 

This script was also inspired by this post [3]. A more optimized version is later adapted from [4].

## Using Custom Dataset
To use a custom dataset, make changes in the `driver.py` file. MaskCoco.MaskParser has two required arguments, being the category dictionary and a list of images. The list of images should be initialized using the ImageLabel class from `MaskCoco.py`. If no image id is provided when initializing, MaskCoco will incrementally generate an id for each image.

The CLI provides a straightforward implementation, but to custom image name, path, or set is_crowded, it is recommended to adjust `driver.py`.

```
optional arguments:
  -h, --help            show this help message and exit
  -i INPATH, --inpath INPATH
                        directory of input images
  -o OUTPATH, --outpath OUTPATH
                        coco json output file path
  -c CATPATH, --catpath CATPATH
                        path of category dictionary json file
  -d, --imageid         specify if use image id
```
One can run the program by `python3 driver.py -i images -o images/dat.json -c categories.json -d`

Initialize the image list and category dictionary, then initialize MaskParser from MaskCoco. The default input path is the current directory. If no output path is specified, the json file `data.json` will be saved in the current directory. The data can then be used for object segmentation architectures like Mask RCNN.

*This script was originally used for wildfire detection*

## References
```
[1] http://groups.csail.mit.edu/vision/datasets/ADE20K/browse.php/?dirname=/training/w/wave/
[2] https://www.kaggle.com/stargarden/coco-image-viewer
[3] https://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch
[4] https://github.com/waspinator/pycococreator/blob/master/pycococreatortools/pycococreatortools.py
```