import sys
sys.path.append("/home/jasonraiti/Documents/GitHub/USC_REU/Project_Files/Jasons_Functions/")

from erosion_dilation import * 



# path to image
path = r'./MAPS/Map_originals/Ibrahim_Test/ibrahim_test_bw.png'
option = 1 # 1 = erode first 2 = dialate first 
num_erosions = 1
num_dilations = 0

# inputs = path to image, erode first (1) or dialate first (2) .desired number of erosions, desired number of dialations 
# outputs = eroded then dialated image
e_d_image , name = erosion_dilation(path,option,num_erosions,num_dilations)
print(name )