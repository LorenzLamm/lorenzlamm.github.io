---
layout: publication
long_title: Background and Illumination Correction for Time-Lapse Microscopy Data with Correlated Foreground
title: BaSiC++
authors: Tingying Peng, Lorenz Lamm, Dirk Loeffler, Nouraiz Ahmed, Nassir Navab, Timm Schroeder, Carsten Marr
publication: Medical Image Computing and Computer Assisted Intervention – MICCAI 2020
year: 2020
doi: https://doi.org/10.1007/978-3-030-59722-1_17
cover-photo: /images/multi-class-active.png
icon: xxx
code: https://github.com/peng-lab
---

Due to the inherent imperfections in the optical path, microscopy images, particularly fluorescence microscopy images, are often skewed by uneven illumination and hence have spurious intensity variation, also known as shading or vignetting effect. Besides spatial intensity inhomogeneity, time-lapse microscopy imaging further suffers from background variation in time, mostly due to photo-bleaching of the background medium. Moreover, the temporal background variation is often experiment-specific and hence cannot be easily corrected, in contrast to shading, where a prospective calibration method can be used. Existing retrospective illumination correction methods, ranging from simple multi-image averaging to sophisticated optimisation based methods such as CIDRE and BaSiC, all assume that the foreground of all images is uncorrelated between each other. However, this assumption is violated in e.g. long-term time-lapse microscopy imaging of adherent stem cells, in which a strong foreground correlation is observed from frame to frame. In this paper, we propose a new illumination and background correction method for time-lapse imaging, based on low-rank and sparse decomposition. We incorporate binary segmentation masks that inform the weighting scheme of our reweighted   𝐿1  norm minimisation about foreground vs background pixels in the image. This yields a better separation of the low-rank and sparse component, hence improving the estimation of illumination profiles. Experiments on both simulated and real time-lapse data demonstrate that our approach is superior to existing illumination correction methods and improves single cell quantification.