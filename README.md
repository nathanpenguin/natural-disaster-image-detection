# Natural Disaster Image Detection
  A program running on resNet-18 designed to detect whether an image contains a cyclone, flood or wildfire. 

  Based on the image that is provided, after completing the project, the given image is classified into one of these classes.
This project can be used in remote and underpopulated areas to alert special services and the locals in adavnce about the presence of a cyclone, flood, or wildfire. This is extremly vital to first responders; giving them advance warning about events, allowing them to save more lives. It is important for us the recognize and identify natural disasters.

An example of when a cyclone is sent: [Click here](https://imgur.com/a/79i7hYI)

## Algorithm

Model: The way this model uses Resnet-18, which is a pretrained model. ResNet-18 is a convolutional neural network that is 18 layers deep. Resnet-18 is already on downloaded onto the jetson, but it is not made to recognize different natural disasters, which is why it needs to be trained. 

Data and training: The data I used, was found on kaggle, specifically for data classification. I then narrowed the data down to 500 images for each category in order to compromise for the limited amount of sapace on the nano. I had three categories: Cyclone, Flood, and Wildfire. I then made three folders: test, train, and validation. And by using the split.py (More info in "Running the Project") file dived them into three categories in a 8-1-1 ratio: test, train, and validation. I also had a text file with all the labels, for when I trained the Resnet-18 model. The model was then trained using a pre written python file (More info in "Running the Project") from the module, in order to train the network to recognize what these different items are. A lot of training had to be done to get correct values.

Once I trained the model, it was able to recognize the different types of natural disasters it was presented with. I then exported the model in the ONNX format, and saved it to the jetson.

Results: Now that the model was trained, and could classify different natural disaster images. A line could be ran in the terminal to classify the images. The input would the the original image and the output would be a new copy of the original but including a label as well (More info in "Running the Project").

Details in "Running the Project"

## Running the Project

1. Download the jetson-inference folder.
   
   Tutorial [here](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md).
  
2. Download the dataset [here](https://drive.google.com/drive/folders/1gil1saB-UyT2ouvr6iMxMlpPk0Utjh1e). Make sure to download the whole 'data' folder.
   Place it in the jetson-inference/python/training/classification/data.

3. Download the model [here](https://drive.google.com/drive/folders/1OtcPVJD0MdpkANUtxtMmdgYUAS7yiNwh).
   Place it in jetson-inference/python/training/classification/models.

5. Delete the imagenet.py file in jetson-inference/build/aarch64/bin.
   
6. Download the modified imagenet.py file from this GitHub and use it to replace the deleted one.

7. Navagate to the jetson-inference folder.
   Run:
   ```
   $ ./docker/run.sh
   ```
   to run the docker container.
   
9. From inside the Docker container, change directories so you are in jetson-inference/python/training/classification
  
10. Run the training script to train the network where the model-dir argument is what the name of the folder containing the training data.  You should immediately start to see output, but it will take a very long time to finish running. Fill in the square bracket with their respective values.
```
python3 train.py --model-dir=models/[Name of model] data/[Name of the folder containing the data]
```
11. In order to convert the model into ONNX format navigate to jetson-inference/python/training/classification
    Then run:
    ```
    python3 onnx_export.py --model-dir=models/[Name of model]
    ```
    Look in jetson-inference/python/training/classification/models/[Name of model]. There should be a new model called resnet18.onnx there.
    
12. Exit the docker and ensure you are in jetson-inference/python/training/classification.
    
13. Set the NET and DATASET variables.
    ```
    NET=models/[Name of model]
    ```
    ```
    DATASET=data/[Name of the folder containing the data]
    ```

14. The model is trained! Run this script and fill in the appropriate values to classify.
    ```
    python3 /home/nvidia/jetson-inference/python/training/classification/imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/[Disaster Folder (Cyclone, Flood, or Wildfire)]/[Image Name] [New classified image output name]
    ```
15. You are done! Congrats! Find the new classified image output to veiw what it's classified as.
