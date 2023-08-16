import splitfolders


input_folder = '/home/nvidia/jetson-inference/python/training/classification/data/Disasters'


# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, (.8, .2).
# Train, val, test
splitfolders.ratio(input_folder, 
                   output="Disasters_data", 
                   seed=42, 
                   ratio=(.7, .2, .1), 
                   group_prefix=None) 