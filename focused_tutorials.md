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

* ClinVar: A database of genomic variations and their associations with diseases.
* gnomAD: Population-wide genomic variant data with allele frequency annotations.
* UniProt: A comprehensive database of protein sequences and functional annotations.

### Tasks
{:.no_toc}

1. Introduction of [AlphaMissense](https://www.science.org/doi/10.1126/science.adg7492)
   - Overview of AlphaMissense and its novel transformer-based approach for pathogenicity prediction.  
   - Discuss the strengths of AlphaMissense in capturing proteome-wide context for missense variant prediction.  
   - Analyze specific case studies where AlphaMissense has advanced our understanding of pathogenic variants.  

2. Practical Applications of Missense Variant Effect Prediction
   - Use AlphaMissense to classify missense variants (e.g., benign vs. likely pathogenic) across datasets.  
   - Validate predictions by comparing with known annotations (e.g., ClinVar).  
   - Explore how predictions can inform clinical decision-making and functional studies.  

3. Transformers in Genomics
   - Broader discussion on the use of transformer architectures in genomics beyond AlphaMissense.  
   - Build a simple transformer-based model for sequence classification using genomic or proteomic data.  
   - Explore variant effect prediction tasks using custom transformer models.  

4. Advanced Applications and Fine-tuning (Stretch Task)  
   - Fine-tune AlphaMissense or another pre-trained transformer model with specific datasets (e.g., domain-specific mutations or rare disease variants).  
   - Evaluate the generalizability of these models across unseen data and rare variant types.  
   - Discuss transfer learning and zero-shot predictions in genomics.  

### Skills Developed
{:.no_toc}

* Understanding the challenges for proteome-wide variant effect prediction.
* Hands-on experience with AlphaMissense for missense variant classification and analysis.
* Broader knowledge of transformer models applied to genomics.

## Tutorial 5: Biomolecular Structure Modeling with AlphaFold3, Boltz-1, and Chai-1 Foundation Models

### Speaker
{:.no_toc}

[Yasha Ektefaie](../staff)

### Datasets
{:.no_toc}

* Structural data from the Protein Data Bank (PDB), including proteins, ligands, RNA, and DNA, to serve as inputs for the models.

### Tasks
{:.no_toc}

1. Setting Up and Running Foundation Models
	* Learn how to install and run AlphaFold3, Boltz-1, and Chai-1.
	* Set up and configure input data for each model.
	* Run the models using Google Colab for practical, hands-on experience.
	* Visualize the outputs in PyMOL to analyze the predicted structures.
	* Compare the model outputs to reference structures in the literature to quickly benchmark model performance.
2. Understanding Model Performance with [SPECTRA](https://github.com/mims-harvard/SPECTRA)
	* Download and interpret precomputed spectral performance data for Boltz-1.
	* Calculate the cross-split overlap between an example input and Boltz-1's training data.
	* Plot the overlap on the spectral performance curve to predict Boltz-1's performance, and validate predictions by running the model.
3. Fine-Tuning for Specialized Applications by Improving Boltz-1's performance on a specific dataset:
	* Fine-tune the model using an antibody dataset.
	* Assess the improvement in predictions post-fine-tuning.

## Tutorial 6: Protein Language Models for Clinical Variant Effect Prediction

### Speaker
{:.no_toc}

[Courtney A Shearer](../staff)

### Datasets
{:.no_toc}

* MSA.
* Variant effect prediction (VEP) scores from multiple models.
* ClinVar: A database of genomic variations and their associations with diseases.
* gnomAD: Population-wide genomic variant data with allele frequency annotations.
* Deep Mutational Scan (DMS) datasets.

### Tasks
{:.no_toc}

* Download and visualize pLM representations.
* Correlate pLM predictions with DMS data.
* Correlate pLM predictions with Clinvar data.
* Download various pLM VEP and determine differences.
* Analyze how different pLM VEP tools are used for different genetics questions based on training data.

### Skills Developed
{:.no_toc}

* Protein sequence analysis.
* Clinical variant interpretation.
* Model selection for different genomic scenarios.
* Performance evaluation methods.

## Tutorial 7: Modeling Single-Cell Perturbations with Foundation Models

### Speaker
{:.no_toc}

[Yepeng Huang](../staff)

### Datasets
{:.no_toc}

* Single-cell genetic perturbation datasets, scPerturb (in particular, Normal et al. (2019), Replogle et al. (2022)).
* Single-cell drug perturbation datasets, Sci-plex 3.

### Models
{:.no_toc}

* Foundation models: scGPT, scBERT, scFoundation.

### Tasks
{:.no_toc}

* Setting up and running the model
	* Set up environment.
	* Download models and their pretrained weights.
	* Run inference of models to get cell embeddings.
* Benchmarking the model
	* Implement simple evaluation metrics.
	* Finetune linear probes for each model with those cell embeddings.
	* Compare performance with simple baselines.
* Adapting scGPT for generalization to unseen perturbations
	* Download a variant of scGPT designed for predicting new perturbations
	* Run inference to obtain results.
	* Compare performance with simple baselines.