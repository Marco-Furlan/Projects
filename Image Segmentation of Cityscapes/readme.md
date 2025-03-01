# Image Segmentation of Cityscapes


<p align="center">
  <img src="images/frankfurt_pred_denseASPP.gif" alt="[loading gif, please wait]" width="550"/>
</p>

<p align="center">Images of Frankfurt from the Cityscapes Dataset. The coloring is the segmentation of DenseASPP.</p>

In tasks such as autonomous driving and video surveillance, where understanding street scenes is essential, [semantic image segmentation](https://paperswithcode.com/task/semantic-segmentation) serves as the initial step. This process involves classifying each pixel of a high-resolution image into one of the available semantic labels, providing crucial contextual information for subsequent analysis. Given the video-based nature of these tasks, objects and individuals often undergo significant and frequent changes in scale. This poses a challenge for representing high-level features, as models must accurately encode multi-scale information.

Over the years, numerous models have been developed to tackle this demanding task. In this project, we present the results of our experiments with three such models: [DeepLabV3](https://paperswithcode.com/method/deeplabv3), [U-Net](https://arxiv.org/abs/1505.04597), and [DenseASPP](https://openaccess.thecvf.com/content_cvpr_2018/papers/Yang_DenseASPP_for_Semantic_CVPR_2018_paper.pdf). Each model employs distinct strategies and architectural implementations to effectively capture multi-scale contextual information and achieve efficient segmentations of images. For our benchmark testing, we utilized the [Cityscapes dataset](https://www.cityscapes-dataset.com/), specifically designed for street scene segmentation tasks. While all three models exhibit similar performance, DenseASPP demonstrates superior results.

Our contributions were:

- Training from scratch the DeepLabv3 model,

- Training from scratch the UNet model, which was done using [my own UNet PyTorch implementation](https://github.com/MarcoFurlan99/Marco_code_final/tree/master/UNet) 

- Updating the DenseASPP model from [here](https://github.com/DeepMotionAIResearch/DenseASPP) to be compatible with the latest Python and PyTorch versions.

A full breakdown of the model architectures, training and testing methodologies is done in the [report](report.pdf). You can get a fast visual overview of these topics from the [presentation](presentation.pdf). We show here some performance metrics:

![](images/results.jpg)

We will consider the Macro [^1] metric for the comparison. UNet performs terribly despite being trained on less classes [^2], and the best performing model among the three is the DenseASPP.

[^1]: the Macro average should be equivalent to the meanIoU, which would be the standard evaluation metric to compare image segmentation models, but results are off because the exact DenseASPP model we downloaded already trained should return a meanIoU of 0.81 on the Cityscapes dataset, while we get a 0.52. An analysis of this issue is carried in the [report](report.pdf).

[^2]: we reduced the number of classes to test the first training of the UNet. Given the results and the time it takes to train, we deemed it unworthy to redo the training with all 19 classes.

As part of the presentation we included a [video](https://www.youtube.com/watch?v=U-L6mPUYhu0) which compares qualitatively the 3 models on a completely new task.

<table>
  <tr>
    <td style="background-color:#FFFF00">Original</td>
    <td style="background-color:#FF0000">DeepLabv3</td>
  </tr>
  <tr>
    <td style="background-color:#00FF00">UNet</td>
    <td style="background-color:#0000FF">DenseASPP</td>
  </tr>
</table>

Click the link above or the image below to open it.

[![Watch the video](images/youtube_frame.jpg)](https://www.youtube.com/watch?v=U-L6mPUYhu0)
