---
layout: publication
long_title: Multi-task Learning of a Deep K-Nearest Neighbour Network for Histopathological Image Classification and Retrieval
title: Multi-task Learning of a Deep K-NN Network
authors: Tingying Peng, Melanie Boxberg, Wilko Weichert, Nassir Navab, Carsten Marr
publication: Medical Image Computing and Computer Assisted Intervention – MICCAI 2019
year: 2019
doi: https://doi.org/10.1007/978-3-030-32239-7_75
cover-photo: /images/multi-task-knn_small.png
icon: xxx
---

Deep neural networks have achieved tremendous success in image recognition, classification and object detection. However, deep learning is often criticised for its lack of transparency and general inability to rationalise its predictions. The issue of poor model interpretability becomes critical in medical applications: a model that is not understood and trusted by physicians is unlikely to be used in daily clinical practice. In this work, we develop a novel multi-task deep learning framework for simultaneous histopathology image classification and retrieval, leveraging on the classic concept of k-nearest neighbours to improve model interpretability. For a test image, we retrieve the most similar images from our training databases. These retrieved nearest neighbours can be used to classify the test image with a confidence score, and provide a human-interpretable explanation of our classification. Our original framework can be built on top of any existing classification network (and therefore benefit from pretrained models), by (i) combining a triplet loss function with a novel triplet sampling strategy to compare distances between samples and (ii) adding a Cauchy hashing loss function to accelerate neighbour searching. We evaluate our method on colorectal cancer histology slides and show that the confidence estimates are strongly correlated with model performance. Nearest neighbours are intuitive and useful for expert evaluation. They give insights into understanding possible model failures, and can support clinical decision making by comparing archived images and patient records with the actual case.