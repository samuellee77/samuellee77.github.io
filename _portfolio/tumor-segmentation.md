---
title: "Liver Tumor Detection Model"
excerpt: "In this project, we developed a liver tumor detection model using the U-Net architecture to accurately identify and segment tumors in liver images. The model achieved a 68% accuracy on the evaluation dataset, demonstrating a moderate ability to detect liver tumors. Although the model's performance is not yet optimal, it lays the foundation for future advancements.<br/><img src='/images/tumor_summary.png'>"
collection: portfolio
---
## Liver Tumor Detection Model

**Authors:** Ali, Nathaphat, Samuel Lee

## Introduction

Tumor detection is a critical task in medical diagnostics, as it plays a vital role in early intervention and treatment planning. With the large amounts of CT scans that radiologists must go through, we propose a program that helps detect liver tumors. The dataset we will be using is “Medical Image Segmentation: Evaluation” from Kaggle.

## Aim

The aim of this project is to build a U-Net Model that will be able to predict tumors in the liver with a high accuracy. As well as create a GUI which allows anyone to input a CT scan as an image into a user interface to predict whether there is a tumor or not.

## Data Collection and Preprocessing

We first gathered a dataset of medical images containing tumors from the liver from Kaggle ([Medical Image Segmentation: Evaluation](https://www.kaggle.com/datasets/modaresimr/medical-image-segmentation)). In the dataset, the images are separated into ground truth (GT) and raw CT scans as `.nii` files. The ground truth files are scans that radiologists have circled a tumor around.

**Steps we took for preprocessing:**

1. **Conversion:** Convert medical image files (`.nii`) into slices of the CT scan as PNG files.
2. **Verification:** Ensure that the images have corresponding ground truth files.
3. **Resizing:** Resize images to ensure consistency between raw and GT files.

To achieve these steps, we converted the 3D CT scan into 2D image slices by utilizing Python libraries such as NumPy for converting 3D arrays into 2D. Then, we looped through the sizes of the files to ensure they were consistent; if not, we resized them to 512 by 512 pixels.

## Model Selection

We had to explore different models to use for representation learning for medical images, and the one that worked the best for this that we found was the U-Net Model. From Olaf Ronneberger, Philipp Fischer, and Thomas Brox’s paper, **“U-Net: Convolutional Networks for Biomedical Image Segmentation”**, we found that this model has been proven to be effective and reliable, utilizing the advantages of CNN. U-shaped skip connections also make it a good choice for medical image segmentation. The model has been used before to identify the boundaries of tumors in other body parts and can perform well with limited training data.

## Model Training and Validation

For data collection, we split our dataset into training and validation sets. We stored images in folders as pairs containing the raw CT scan and the corresponding GT file for that scan. Then we trained our U-Net model using the training set and validated its performance on the validation set. We applied an appropriate loss function (Mean Squared Error) and used optimization techniques to fine-tune the model's parameters and improve liver tumor detection accuracy.

## Results

The liver tumor detection model achieved an overall accuracy of 68% on the evaluation dataset. While the accuracy indicates that the model performs better than random guessing, it falls short of meeting the desired level of performance for clinical deployment. Several factors might contribute to the lower accuracy of the model. The limited size of the training dataset may not have provided sufficient diversity and representation of different tumor types and imaging conditions. In addition, the short of computing power during our model training process also limit the performance of our model. Additionally, the complexity and heterogeneity of liver tumors pose significant challenges for accurate detection and segmentation.

## Conclusion

In this project, we developed a liver tumor detection model using the U-Net architecture to accurately identify and segment tumors in liver images. The model achieved a 68% accuracy on the evaluation dataset, demonstrating a moderate ability to detect liver tumors. Although the model's performance is not yet optimal, it lays the foundation for future advancements. Addressing limitations, such as the limited training dataset and complex liver tumors, is crucial for enhancing accuracy and robustness. Our next steps involve expanding the dataset, incorporating advanced deep learning techniques, refining the model architecture, and improving preprocessing and augmentation methods. Despite limitations, the model can serve as a valuable supporting tool when used alongside expert radiologists' assessments, potentially reducing workload and providing additional insights. Future work aims to extend the study to other anatomical regions, such as the brain and pancreas, using the U-Net model, to improve results and achieve higher accuracy in tumor detection, ultimately contributing to enhanced clinical decisionmaking and patient care.

## Acknowledgements

We would like to thank everyone who has supported us in this project. Firstly, thank you to DS3 student organization for providing us with this project and thank you to the dataset owners. And to our mentor Advaith for providing his help throughout the time span of this project. Also, we’d like to thank ITS UCSD for providing us with tools like the Jupyter Notebook server for running our tumor detection program.
