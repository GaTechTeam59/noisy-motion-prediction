- Team name: Project Team 59
- Is this a Facebook project? No.
- Project title: Human Motion Prediction in Noisy Environments

**Project summary.**
- Detecting and idenfying human motion arises in a number of applications
including animation (movies and video games), video analysis (security,
sports, etc.), and robotics (self-driving cars). Although movement detection
and indentifcation has its roots in classical computer vision (CV) problems,
deep learning provides new avenues to approach these problems blending 
classical CV tools with modern computational and inferential paradigms. That
said, deep learning approaches have worked with idealized data sets that are
not marred with noise. Our project seeks to:
    - train and optimize models using noisy data (based on existing 
    architectures used for noise-free datasets);
    - predict motion in the presence of noise; and
    - compare the performance of models trained with noise versus those 
    trained in the absence of noise.

**Approach.**
- Researchers have used techniques from computer vision as well as deep
learning to detect and identify movements from animated and live-action data
sources.
Our approach to investigate the problem of motion prediction in the presence of
noise is to:
    - create/replicate a baseline (*e.g.*, a convolutional 
    sequence-to-sequence model);
    - vary the amount of noise in the (training and test) dataset 
    (*e.g.*, adding noise-energy into the image/sequence—potentially 
    adversarially); and
    - compare the results and performance noise-sensitive models against
    the baseline (noise-free) model.
- We will apply our approach on a subset of live-action movements from the human
motion database (HMDB) dataset (described below) to train and optimize our
models before studying our problem in the context of a larger portion of (or
perhaps the full) HMDB dataset.
- *Stretch goal:* to generate novel human movements (*e.g.*, dancing).

**Resources / related work.**
+ ["HMDB: A Large Video Database for Human Motion Recognition"](https://serre-lab.clps.brown.edu/wp-content/uploads/2012/08/Kuehne_etal_iccv11.pdf) – Kuehne et al.
+ ["AMASS: Archive of Motion Capture as Surface Shapes"](https://arxiv.org/pdf/1904.03278.pdf) – Mahmood et al.
+ ["A Spatio-temporal Transformer for 3D HumanMotion Prediction"](https://arxiv.org/pdf/2004.08692.pdf) – Aksan et al.
+ ["Structured Prediction Helps 3D Human Motion Modelling"](https://arxiv.org/pdf/1910.09070.pdf) – Aksan et al.
+ ["Learn to Dance with AIST++: Music Conditioned 3D Dance Generation"](https://paperswithcode.com/paper/learn-to-dance-with-aist-music-conditioned-3d) – Li et al.
+ ["History Repeats Itself: Human Motion Prediction via Motion Attention"](https://paperswithcode.com/paper/history-repeats-itself-human-motion) – Mao et al.
+ ["Convolutional Sequence to Sequence Model for Human Dynamics"](https://arxiv.org/pdf/1805.00655.pdf) – Li et al.

**Datasets (provide a link to the dataset).**
- We plan to use the HMDB dataset, which contains 51
distinct actions (*e.g.*, smiling, eating, climbing, etc.) categorized into five
types (facial actions, body movements, etc.) with at least 101 examples per
action, for our project.
- The data can be found here:
<https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/>.

**Group members.**
- Matthew Adamson
- Richard Feinleib
- Jake Knigge
- Pavneet Tiwana

Are you looking for more members? No.

**Piazza post link:** **[TBD]**.