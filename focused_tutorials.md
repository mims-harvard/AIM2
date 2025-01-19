---
layout: page
title: Focused Tutorials
nav_order: 2.2
description: Artificial Intelligence in Medicine II 
---

# Focused Tutorials
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The practical tutorials are designed to give you hands-on experience applying AI techniques to real-world healthcare problems. Using open-source datasets, you’ll have the opportunity to work with proven AI applications, from building models to validating their performance and visualizing results. 

Each tutorial is structured to be straightforward and accessible, ensuring that you can dive right in and start experimenting with the code and models. These tutorials cover a range of core AI applications, such as natural language processing, medical image analysis, graph neural networks, generative models, LLMs, biological foundation models, clincial foundation models, providing a practical complement to the theoretical concepts discussed in class. You’ll have the chance to see how the models you’ve learned about work in practice, gaining valuable insight into their behavior, strengths, and limitations.

By working directly with real-world data, you’ll not only strengthen your technical skills but also build a deeper understanding of how to integrate AI into healthcare research. The practical tutorials are designed to prepare you for future projects, whether in academia or industry, by developing essential skills in coding, data analysis, and model evaluation.

This hands-on experience will serve as a foundational toolset for your future research as well as additional support for your work in the course project. 

## Tutorial 1: NLP in Medicine

### Speaker
{:.no_toc}

[Dr. Grey Kuling](../staff)

### Datasets
{:.no_toc}

* Clinical notes dataset (e.g., MIMIC-III or de-identified open-source clinical datasets).

### Tasks
{:.no_toc}

* Preprocessing Medical Text Data
	- Tokenize text into sentences and words using NLP libraries like spaCy or NLTK.
	- Normalize text by handling abbreviations, medical jargon, and common typos.
	- Annotate datasets with relevant medical entities using Named Entity Recognition (NER).

* Fine-Tuning Pre-trained Transformers
	- Use Hugging Face Transformers to fine-tune ClinicalBERT or similar models.
	- Train the model on specific clinical tasks like disease classification or drug identification.

* Parameter-Efficient Fine-Tuning with LoRA
	- Apply Low-Rank Adaptation (LoRA) to reduce computational requirements.
	- Compare model performance between full fine-tuning and LoRA.

* Text Generation with LLMs
	- Use GPT-based models to summarize medical notes or generate clinical trial matches.
	- Experiment with controlling output length and quality using temperature and sampling parameters.

* Advanced NLP Applications (Stretch Task)
	- Implement a pipeline for de-identifying clinical notes using trained NER models.
	- Use a GPT model to answer medical questions based on clinical scenarios.

### Skills Developed
{:.no_toc}

* Mastery of medical text preprocessing techniques.
* Practical experience fine-tuning transformers for clinical NLP tasks.
* Hands-on introduction to efficient NLP model training.

## Tutorial 2: Generative AI in Medicine

### Speaker
{:.no_toc}

[Dr. Grey Kuling](../staff)

### Datasets
{:.no_toc}

* Medical imaging datasets (e.g., CheXpert or the Medical Segmentation Decathlon).

### Tasks
{:.no_toc}

* Building Variational Autoencoders (VAEs)
	- Implement a VAE using PyTorch for generating synthetic medical images.
	- Visualize the learned latent space to understand its representation of data variability.
* Building Generative Adversarial Networks (GANs)
	- Train a GAN to generate synthetic medical images (e.g., X-rays or MRI scans).
	- Evaluate the quality of generated images using Fréchet Inception Distance (FID).
* Exploring Generative Models for Text
	- Use a GPT model to generate synthetic clinical records.
	- Compare synthetic records to real notes and evaluate semantic coherence.
* Understanding Data Privacy in Generative AI
	- Experiment with techniques to assess privacy risks, such as membership inference attacks.
	- Discuss how synthetic data can mitigate privacy concerns in healthcare.
* Model Comparison (Stretch Task)
	- Compare VAEs and GANs for their ability to generate realistic medical data.
	- Explore how generated data can be used to augment training datasets for downstream tasks.

### Skills Developed
{:.no_toc}

* Building and evaluating generative models for healthcare applications.
* Understanding privacy implications and synthetic data generation.

## Tutorial 3: Medical Image Analysis

### Speaker
{:.no_toc}

[Dr. Grey Kuling](../staff)

### Datasets
{:.no_toc}

* Datasets from the Medical Segmentation Decathlon (e.g., liver or brain scans).

### Tasks
{:.no_toc}

* Image Preprocessing
	- Load, resize, and normalize medical images using Python libraries like Pillow or OpenCV.
	- Visualize medical images and perform basic exploratory analysis.
* Image Classification and Regression
	- Train a CNN to classify medical images into diagnostic categories (e.g., tumor or non-tumor).
	- Perform regression analysis to predict risk scores based on image features.
* Image Segmentation with U-Net
	- Build and train a U-Net model for segmenting anatomical regions in medical images.
	- Evaluate segmentation performance using the Dice coefficient and Jaccard index.
* Experimentation and Model Tracking
	- Use Weights & Biases to log model performance and compare experiments.
	- Optimize model performance through hyperparameter tuning.
* Advanced Segmentation Tasks (Stretch Task)
	- Perform multi-class segmentation for complex medical images (e.g., segmenting organs and tumors).
	- Explore using pre-trained models for transfer learning in segmentation tasks.

### Skills Developed
{:.no_toc}

* Mastery of medical image preprocessing, classification, and segmentation.
* Hands-on experience with CNNs and U-Net architectures.

## Tutorial 4: AI in Genomics

### Speaker
{:.no_toc}

[Dr. Joshua Pan, Senior Research Scientist - Google DeepMind](https://scholar.google.com/citations?user=BbJE7xgAAAAJ&hl=en)

### Datasets
{:.no_toc}

TBA

### Tasks
{:.no_toc}

TBA

### Skills Developed
{:.no_toc}

TBA

## Tutorial 5: TBA

### Speaker
{:.no_toc}

[Yasha Ektefaie](../staff)

### Datasets
{:.no_toc}

TBA

### Tasks
{:.no_toc}

TBA

### Skills Developed
{:.no_toc}

TBA

## Tutorial 6: TBA

### Speaker
{:.no_toc}

[Courtney A Shearer](../staff)

### Datasets
{:.no_toc}

TBA

### Tasks
{:.no_toc}

TBA

### Skills Developed
{:.no_toc}

TBA

## Tutorial 7: TBA

### Speaker
{:.no_toc}

[Yepeng Huang](../staff)

### Datasets
{:.no_toc}

TBA

### Tasks
{:.no_toc}

TBA

### Skills Developed
{:.no_toc}

TBA