#!/usr/bin/env python
# coding: utf-8

# # Lesson 5: Acids and Bases
# Acids and bases are **core concepts** in chemistry. And it is about much more than mere $pH$. What is the acidity of 1% sulphuric acid mixture in water? How would you calculate or **measure** it? Now, what is the acidity of a 99% mixture? Does $pH$ have any meaning here? We need a way to measure the acidity of **very strong acid mixtures** so that we can use them in **experiments**. You are now ready at last to learn the truth.
# 
# I didn't truly understand **acid-base equilibria** until I started graduate school. I hope to save you a year and get the concept across in this course.
# 
# -----
# ## 5.1 Lesson Plan
# The plan below is not necessarily what will happen in class – it is merely what I **hope** will happen in class. We will explore the following subjects and ideas$\ldots$
# 
# - We will explore how to **calculate** the fraction of protonated/deprotonated species in a solution of a given acidity. We will make it super easy with a **Jupyter notebook and Python**.
# - What does $pK_a$ mean and how is it useful? Even when the value seems ridiculous? (Ch.5.1)
# - What is ”acidity”? What is $pH$? I mean, **what is it really**? What if I told you that $pH$ is not really $−\log[H^+]$. Can you handle the truth? (Ch. 5.1)
# - Introducing the **Hammett acidity function**, $H_0$. (Ch. 5.2)
# - Predicting **relative acid strengths** by comparing molecular structure (Ch. 5.4)
# - **Solvent effects** on acid/base equilibrium (Ch. 5.3) 
# 
# 
# -----
# ## 5.2 Learning Goals
# After reading the suggested textbook section and practicing the problems you should be able to$\ldots$
# 
# - Understand $pH$ as an **acidity function**.
# - Understand **how** the Hammett acidity function **is determined** for various acid mixtures.
# - Determine the **extent of protonation** of a reactant in various $pH$ or $H_0$ values.
# - **Calculate** the $pK_a$ of a reactant from equilibrium data.
# - Understand the **effect of resonance, induction, steric strain and electrostatic effects** on the $K_a$ value of an acidic functional group.
# - Be able to **predict** which of two related acids is stronger and explain why.
# - Understand the role of **solvent** in determining the $K_a$ value of an acidic functional group.
# 
# 
# -----
# ## 5.3 Assignment \#5
# 
# The following assignment is to be submitted via moodle before the Friday meeting.
# 
# ### Instructions
# This section describes the **activity** that you are to perform for the assignment. Do the following$\ldots$
# 
# > Create a **plot** of one set of $pK_a$ values against a set of related $pK_a$ values. Perhaps plot $pK_a$ values in water vs. $pK_a$ values in DMSO. Or plot $pK_a$ values in water vs. gas phase. Or plot $pK_a$ values of **substituted benzoic acids** agains $pK_a$ values of substituted phenols or substituted pyridines or substituted something else. An example will be presented in class so you will know exactly what to do.
# 
# ### The Report
# > We are now exploring **data analysis** and so your report should be an **executable Jupyter notebook** that documents your activity while providing the code and results of the code. Feel free to start with the example notebook presented during the lesson week and alter it to suit you. <br>
# > **Write** your notebook in a neat and well organized form. Include comments on your observations and attempt to **explain** them. Is the result obvious to you, or is it a surprise? **Submit a .zip file** that contains the notebook and the data file that you created. Data analysis projects are presented with code and raw data in modern journals, often as Jupyter notebooks. Keeping the code and data together **helps others** to follow your work.
# 
# 
# ### Grading
# **Half** of the grade will be for your **answer** and **half** will evaluate how neat, **clear and professional** your are in communicating your answer. Feel free to use a chemical drawing program. Take pride in your work.
# 
# -----
# ## 5.4 Lesson Schedule
# 
# ### Monday 
# 
# We will explore the **math** of acid/base equilibria using Jupyter notebooks as our calculator. We will introduce the idea of the **acidity function**. $pH$ is just one of many options for expressing acid strength.
# 
# #### Reading
# 
# > **Read** Chapter 5.1 \& 5.2  <br>
# > **Read and Use** the Jupyter notebooks for acid equilibria described below and available on the moodle page
# 
# 
# #### Suggested Problems
# 
# > **Attempt** the following problems at the end of Ch. 5: 1, 3, 5, 6, 12 \& 20  <br>
# > **Explore** the Jupyter notebooks and change them to suit you
# 
# ### Wednesday
# 
# We will consider how structure affects acidity. The most obvious example is substituted benzoic acids. 
# 
# #### Reading
# 
# > **Read** Chapter 5.3 \& 5.4  <br>
# > **Read and Use** the Jupyter notebooks for plotting $pK_a$ values agains each other described below and available on the moodle page
# 
# 
# #### Suggested Problems
# 
# > **Attempt** the following problems at the end of Ch. 5: 2, 4, 9, 11, 13, 17, 19 \& 21 <br>
# > **Explore** the Jupyter notebooks and change them to suit you
# 
# ### Friday
# 
# In our third meeting for this lesson there will be a **short quiz** featuring problems adapted from the suggested textbook problems above. We will then discuss how the plots in our assignment revealed **correlation** (or not) between series of acid strengths. Could this **correlation** be used as a score for how structure affects electron density in a molecule?
# 
# Finally the topics for the **next lesson** will be introduced. **Look ahead** to Lesson 3 to see what you should prepare for Monday. 
# 
# 
# ------
# ## 5.5 Resources
# 
# ### Jupyter Notebooks
# 
# The following notebooks have been made in advance and are available on the moodle site.
# 
# 1. Classic Chem101 Acid Equilibrium
# 2. Hammett Acidity Function Example
# 3. Example Assignment Notebook
# 
# 
# ### For This Lesson
# 
# 1. Tables and Charts of Hammett acidity function values 
#     - How acidic is 50% sulfuric acid? You can look up the Ho value of that and other acid mixtures in these charts.
# 
# 2. Acid-Base Tutorial 
#     - I wrote this review for my biochemistry class several years ago. It may be useful in reviewing the basics of acid-base equi- libria.
# 
# 3. Acidity, Basicity & pKa”
#     - I found this short review out on the internet. I have collected it here for your convenience. It is basic (see what I did there?) but it may be useful for reviewing your earlier work in this subject area.
# 
# 4. Williams’ Compilation of pKa Tables
#     - This is a famous compilation of pKa data assembled by R. Williams based on an earlier compilation by Westheimer & Jencks.
# 5. Evans’ pKa Table 
#     - This is a shorter version of Reich’s compilation of DMSO pKa data (see below) combined with corresponding water pKa data from Williams’ table (see above). I found it at http://evans.rc. fas.harvard.edu/pdf/evans_pKa_table.pdf
# 6. Reich’s pKa Table
#     - This is a compilation of pKa data curated by Hans Re- ich. These values are mostly from the famous Bordwell table of pKa values in DMSO. I found it at https://www.chem.wisc.edu/areas/reich/pkatable/index.htm
# 7. A Short pKa Table
#     - This is a compilation of pKa data curated by Sarah Black. This table focuses on general cases of functional groups and will give a quick survey of pKa values. I found it at http://cactus. dixie.edu/smblack/chem2310/
# 8. Another Short pKa Table
#     - This is a compilation of pKa data curated by Brian Myers. This table focuses on general trends in functional groups. I found it at https://www2.onu.edu/~b-myers/organic/ or https://myersorganic.netlify.app/
# 
# 9. the Jupyter notebooks 
#     - For you to use and abuse
# 
# ### Extra Resources
# 
# 

# 11.5 Learning Goals
# After reading the suggested textbook section and practicing the problems you should be able to. . .
#   Barry Linkletter Page 26 of 67
# 
# 12 STRUCTURE AND ACID STRENGTH
# 12 Structure and Acid Strength 12.1 Textbook Reading
# Chapter 5.3 & 5.4
# 12.2 Resources
# The Moodle site contains links to helpful documents. They will be found in the moodle section that corresponds to this class meeting. They in- clude. . .
#   
# 12 STRUCTURE AND ACID STRENGTH
# 12.3 Lesson Plan
#  
