- Team name: Project Team 59
- Is this a Facebook project? No.
- Project title: Human Motion Prediction in Noisy Environments

**Project summary.**
- Detecting and identifying human motion arises in a number of applications
including animation (movies and video games), video analysis (security,
sports, etc.), and robotics (self-driving cars). Although movement detection and
identification have roots in classical computer vision (CV) problems, deep
learning provides new avenues to approach these problems, blending classical CV
tools with modern computational and inferential paradigms—for example,
augmenting (parallel) convolutional neural networks with (learnable) optical 
flow neural network layers. As most deep learning approaches have worked
with idealized data sets that are not marred with noise, our project explores 
a recognition network's robustness to image noise.
- To do this, our project aims to evaluate the impact and robustness of human motion
recognition models through the following stages:
    - build an existing architecture used for noise-free datasets;
    - train and optimize the model using noisy data;
    - predict motion in the presence of noise; and
    - compare the performance of models trained with noise versus those 
    trained in the absence of noise.

**Approach.**
- Researchers have used techniques from computer vision as well as deep learning
to detect and identify movements from animated and live-action data sources. Our
approach to investigate the problem of motion prediction in the presence of
noise is to:
    - create/replicate a baseline (*e.g.*, a convolutional sequence-to-sequence
    model with an optical flow layer — followign the model described in
    "Representation Flow for Action Recognition");
    - augment the training dataset by varying the amount of noise in the training dataset (and replicating labels) (*e.g.*, adding noise-energy into the image/sequence 
    — potentially adversarially); 
    - augment the test dataset through similar addition of noise energy; and
    - compare the results and performance of noise-injected models against the
    baseline (noise-free) model.
- We will apply our approach on a subset of live-action movements from the human
motion database (HMDB) dataset (described below) to train and optimize our
models before studying our problem in the context of a larger portion of (or
perhaps the full) HMDB dataset.
- *Stretch goal:* to generate novel human movements (*e.g.*, dancing).

**Resources / related work.**
+ ["HMDB: A Large Video Database for Human Motion Recognition"](https://serre-lab.clps.brown.edu/wp-content/uploads/2012/08/Kuehne_etal_iccv11.pdf) – Kuehne et al.
+ ["Representation Flow for Action Recognition"](https://arxiv.org/pdf/1810.01455v3.pdf) – Piergiovanni and Ryoo
+ ["Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset"](https://arxiv.org/pdf/1705.07750v3.pdf) – Carreira and Zisserman
+ ["Two-Stream Convolutional Networks for Action Recognition in Videos"](https://https://arxiv.org/pdf/1406.2199.pdf) – Simonyan and Zisserman
+ ["Action Bank: A High-Level Representation of Activity in Video"](https://cse.buffalo.edu/~jcorso/pubs/jcorso_CVPR2012_actionbank.pdf) – Sadanand et al.
+ ["Structured Prediction Helps 3D Human Motion Modelling"](https://arxiv.org/pdf/1910.09070.pdf) – Aksan et al.
+ ["Efficient feature extraction, encoding and classification for action recognition"](https://www.di.ens.fr/willow/pdfscurrent/kantorov14cvpr.pdf) – Kantorov and Laptev
+ ["History Repeats Itself: Human Motion Prediction via Motion Attention"](https://paperswithcode.com/paper/history-repeats-itself-human-motion) – Mao et al.
+ ["Convolutional Sequence to Sequence Model for Human Dynamics"](https://arxiv.org/pdf/1805.00655.pdf) – Li et al.

**Datasets (provide a link to the dataset).**
- We plan to use the HMDB-51 dataset, which contains 51 distinct actions
(*e.g.*, smiling, eating, climbing, etc.) categorized into five types (facial
actions, body movements, etc.) with at least 101 examples per action, for our
project.
- The data can be found here:
<https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/>.

**Group members.**
- Matthew Adamson
- Richard Feinleib
- Jake Knigge
- Pavneet Tiwana

Are you looking for more members? No.

**Piazza post link:** <https://piazza.com/class/kni1g8lh43l3ie?cid=223_f127>.
