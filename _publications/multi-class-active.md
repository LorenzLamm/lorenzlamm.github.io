---
layout: publication
long_title: Multiclass Deep Active Learning for Detecting Red Blood Cell Subtypes in Brightfield Microscopy
title: Multiclass Active Learning
authors: Ario Sadafi, Niklas Koehler, Asya Makhro, Anna Bogdanova, Nassir Navab, Carsten Marr, Tingying Peng
publication: Medical Image Computing and Computer Assisted Intervention – MICCAI 2019
year: 2019
doi: https://doi.org/10.1007/978-3-030-32239-7_76
cover-photo: /images/multi-class-active.png
icon: xxx
---

The recent success of deep learning approaches relies partly on large amounts of well annotated training data. For natural images object annotation is easy and cheap. For biomedical images however, annotation crucially depends on the availability of a trained expert whose time is typically expensive and scarce. To ensure efficient annotation, only the most relevant objects should be presented to the expert. Currently, no approach exists that allows to select those for a multiclass detection problem. Here, we present an active learning framework that identifies the most relevant samples from a large set of not annotated data for further expert annotation. Applied to brightfield images of red blood cells with seven subtypes, we train a faster R-CNN for single cell identification and classification, calculate a novel confidence score using dropout variational inference and select relevant images for annotation based on (i) the confidence of the single cell detection and (ii) the rareness of the classes contained in the image. We show that our approach leads to a drastic increase of prediction accuracy with already few annotated images. Our original approach improves classification of red blood cell subtypes and speeds up the annotation. This important step in diagnosing blood diseases will profit from our framework as well as many other clinical challenges that suffer from the lack of annotated training data.