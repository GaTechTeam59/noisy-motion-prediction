# noisy-motion-prediction

## Human Motion Prediction in Noisy Environments

### Running the code:
To generate overlay-augmented videos, run "python add_overlay.py" in the command line.  This requires that folders containing samples of every video of a certain type exist in the same directory.  Empty folders named "actionname_overlay", "actionname_pics", and "actionname_overlay_pics" must be created as well.  For example, to generate overlays for the "sit" action, folders named "sit_overlay", "sit_pics", and "sit_overlay_pics" must be added.

To generate the csv file that stores the MHIs, run "python experiment.py" in the command line.

To run the CNN, go to https://www.kaggle.com/matthewadamson/activity-classification-with-mhis-and-cnn and run all of the cells.  No uploading of the dataset is necessary.


### References and notes:
The MHI generation function was refactored from a project in the Computer Vision course at Georgia Tech.  This original function was written from scratch by the same author, Matthew Adamson.

The noise overlays were downloaded from the website http://www.forfilmcreation.com/categorias

The Kaggle notebook code used https://www.kaggle.com/kanncaa1/convolutional-neural-network-cnn-tutorial as a guide to Keras CNNs and the MHI CNN model utilized several of the functions such as training loop data augmentation.
