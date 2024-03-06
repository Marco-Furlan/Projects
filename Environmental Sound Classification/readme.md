# Environmental Sound Classification

![](images/image.png)

In this group project me and a dear friend of mine cooperated to implement and train from scratch different algorithms for the Environmental Sound Classification task. We used the [ESC50](https://github.com/karolpiczak/ESC-50) dataset and its subset, the ESC10, and got performances up to 91% and 100% respectively.

More specifically, we implemented:

- classic ML mdels with manual feature extraction,

- [Pickzac's model](https://www.karolpiczak.com/papers/Piczak2015-ESC-ConvNet.pdf) re-implemented from scratch in Tensorflow,

- a sequential CNN,

- a parallel CNN,

- a vision transformer, which applies self-attention on fixed-size patches.

Here I leave the [report](report.pdf) and the [presentation code](presentation.ipynb), the full codes are shared [here](https://github.com/ivankrstev7/Environmental_Sound_Classification).