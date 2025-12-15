# ECE253_144p
download the VaiL dataset from this link: https://swshah.w3.uvm.edu/vail/datasets.php  
Then run the script in dehaze_part.ipynb to generate you labels in yoloV\v8 style from pascal voc style. You will have to change the names of input and output directory based on how you want to organize your dataset.  

The same file has a script to divide the dataset into training, validation and testing sets. And also script to train your model if you wish to train it. If you do not wish to train your dataset then you can use the best.pt model weights that we have already provided  

Next the same file has a script to add perlin noise fog into the chosen testing images. 
To generate mnono depth estimated fog, followinstructions on this github: https://github.com/tranleanh/haze-synthesis  
Now you have the complete dataset for synthetic generated fog.  

The same file has runs to test on various datasets and also on the dataset that you will generate for low light.  

Follow the script in synthetic_lowlight.ipynb to generate your low_light dataset
