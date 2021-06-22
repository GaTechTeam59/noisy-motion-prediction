- Team name: Project Team 59
- Is this a Facebook project?: No.
- Project title: Human Motion Prediction in Noisy Environments
- Project summary (4-5+ sentences). Fill in your problem and 
background/motivation (why do you want to solve it? Why is it interesting?).
This should provide some detail (don’t just say “I’ll be working on object
detection”)
    + Detecting and idenfying human motion arises in a number of applications
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
- What you will do (approach, 4-5+ sentences) - Be specific about what you will
implement and what existing code you will use. Describe what you actually plan
to implement or the experiments you might try, etc. Again, provide sufficient
information describing exactly what you’ll do. One of the key things to note is
that just downloading code and running it on a dataset is not sufficient for a
description or a project! Some thorough implementation, analysis, theory, etc.
has to be done for the project.
    + Researchers have used techniques from computer vision as well as deep
    learning to detect and identify movements. Our approach to investigate 
    the problem of motion prediction in the presence of noise is to:
        - create/replicate a baseline (*e.g.*, a convolutional 
        sequence-to-sequence model);
        - vary the amount of noise in the (training and test) dataset 
        (*e.g.*, adding noise-energy into the image/sequence—potentially 
        adversarially); and
        - compare the results and performance noise-sensitive models against
        the baseline (noise-free) model.
    + *Stretch goal:* to generate novel human movements (*e.g.*, dancing).
- Resources / related work & papers (4-5+ sentences). What is the state of art
for this problem? Note that it is perfectly fine for this project to implement
approaches that already exist. This part should show you’ve done some research
about what approaches exist.
    + ["AMASS: Archive of Motion Capture as Surface Shapes"](https://arxiv.org/pdf/1904.03278.pdf) – Mahmood et al.
    + ["A Spatio-temporal Transformer for 3D HumanMotion Prediction"](https://arxiv.org/pdf/2004.08692.pdf) – Aksan et al.
    + ["Structured Prediction Helps 3D Human Motion Modelling"](https://arxiv.org/pdf/1910.09070.pdf) – Aksan et al.
    + ["Learn to Dance with AIST++: Music Conditioned 3D Dance Generation"](https://paperswithcode.com/paper/learn-to-dance-with-aist-music-conditioned-3d) – Li et al.
    + ["History Repeats Itself: Human Motion Prediction via Motion Attention"](https://paperswithcode.com/paper/history-repeats-itself-human-motion) – Mao et al.
    + ["Convolutional Sequence to Sequence Model for Human Dynamics"](https://arxiv.org/pdf/1805.00655.pdf) – Li et al.
- Datasets (provide a link to the dataset). This is crucial! Deep learning is
data-driven, so what datasets you use is crucial. One of the key things is to
make sure you don’t try to create and especially annotate your own data!
Otherwise the project will be taken over by this.
    + We plan to use the AMASS dataset, which "is a large database of human
    motion unifying different optical marker-based motion capture datasets by
    representing them within a common framework and parameterization." The
    dataset is sufficiently large to support deep learning "having more than 40
    hours of motion data, spanning over 300 subjects, more than 11,000 motions."
    + The data can be found here: <https://amass.is.tue.mpg.de/index.html>.
- List your group members: Matthew Adamson, Richard Feinleib, Jake Knigge, and
Pavneet Tiwana.
- Are you looking for more members? No.
- Piazza post link: **[TBD]**.