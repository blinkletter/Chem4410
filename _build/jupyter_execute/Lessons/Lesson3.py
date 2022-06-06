#!/usr/bin/env python
# coding: utf-8

# # Lesson 3: Computational Chemistry
# We can do **much more** than estimate the electronic structure of $\pi$ molecular orbital systems. Using computers we can **optimize structure and energies** to visualize accurate (at least more accurate than HMOT) electronic structure. In this lesson we will be introduced to the free **GAMESS computational chemistry package**. We will be able to perform semi-empirical and ab-initio calculation. We will not dwell on the theory, we will just use the system like a black box. There is a whole other course on theoretical chemistry that you can experience if you are inspired to do so.
# 
# Along the way we will gain a **better understanding** of molecular orbitals, transition state theory and confromational analysis. 
# 
# -----
# ## 3.1 Lesson Plan
# The plan below is not necessarily what will happen in class – it is merely what I **hope** will happen in class. We will explore the following subjects and ideas$\ldots$
# - **Installing** GAMESS and related software
# - The Z-matrix and constructing GAMESS **input files**
# - Interpreting GAMESS **output files**
# - Using GAMESS to interpret the structure of **small molecules and transition states**
# - Using GAMESS to construct r0tational **energy profiles and reaction coordinates**
# - Using GAMESS and related software to **visualize molecular orbitals**.
# 
# -----
# ## 3.2 Learning Goals
# After reading the suggested textbook section and practicing the problems you should reached the following goals$\ldots$
# 
# - To have a **beginners** experience with computational tools.
# - To have learned **problem solving** and zen-like patience in dealing with scientific software.
# - To have a better understanding of how local **molecular orbitals** relate to "real" molecular orbitals and how both can explain **reactivity**.
# - Be able to use GAMESS in **future exercises** in this course and in your **research** projects.
# 
# -----
# ## 3.3 Assignment \#3
# 
# The following assignment is to be submitted via moodle before the Friday meeting.
# 
# ### Instructions
# This section describes the **activity** that you are to perform for the assignment. Do the following$\ldots$
# 
# > **Install** GAMESS and related programs on your computer. Perform calculations as demonstrated in the Monday and Wednesday meetings on your own. try molecules of your own choice as you repeat the methods demonstrated in class.
# 
# ### The Report
# > **write** a report in which you present the local bonding orbitals and the molecular orbitals of the ethyene cation ($C_2H_5^+$). Report all the bond lengths and **comment** of the assymmetry of the methyl bond lengths. Propose an **explanation**. Your report should include relevant diagrams and images (especially graphical representations of the orbitals)
# 
# 
# ### Grading
# **Half** of the grade will be for your **answer** and **half** will evaluate how neat, **clear and professional** your are in communicating your answer. Feel free to use a chemical drawing program. Take pride in your work.
# 
# 
# 
# -----
# ## 3.4 Lesson Schedule
# 
# ### Monday 
# 
# Bring your **laptop computer** if you have one and are able to do so. On Monday we will introduce the very basics of computational chemistry and demonstrate the use of GAMESS at for determinig the structure of water, ammonia and methane. We will learn how to **construct input files** with the **Z-matrix** and will then **visualize** the molecular orbitals. We will explore how our own graphical approach from lesson \#2 **compares** to more sophisticated methods.
# 
# #### Reading
# 
# > **Read** Chapter 14.1 and 14.2. Be gentle on yourself, we will not be emphasizing the theory here but you should be exposed to it to help understand the results of our GAMESS calculations.  <br>
# > **Read** the instructions for installing and using GAMESS.  
# 
# #### Suggested Problems
# 
# > **Install GAMESS** and related software. Be patient, this will be frustrating. <br>
# > **Attempt** to complete the calculation described in the instructions above. We will be discussing all your frustrations on Monday so be sure to try this before class. Give yourself **lots of time**.
# 
# ### Wednesday
# 
# Bring your **laptop computer** if you have one and are able to do so. We will discuss using GAMESS to optimize and visualize local and molecular orbitals in $\pi$ systems and to construct a **rotational energy profile** for ethane and butane.
# 
# #### Reading
# 
# > **Read** the instructions for constructing an **energy profile** using GAMESS.    
# 
# #### Suggested Problems
# 
# > **Attempt** to make an energy profile for bond rotation in ethane and butane. Plot the results using a Jupyter notebook that documents your efforts.
# 
# ### Friday
# 
# There will be **no quiz**. This has been planned to be more of a practical lesson. Bring your **laptop computer** if you have one and are able to do so. We will explore transition states and reactions using GAMESS. Finally the topics for the **next lesson** will be introduced. **Look ahead** to Lesson 4 to see what you should prepare for Monday. 
# 
# 
# #### Reading
# 
# > **Read** the instructions for performing a **transition state optimization** and calculatingan **intrinsic reaction coordinate** using GAMESS   
# 
# #### Suggested Problems
# 
# > **Attempt** to determine the structure of the transition state for an $\text{S}_N2$ reaction.
# 
# ------
# ## 3.5 Resources
# ### For This Lesson
# 1.  [Instructions for Installing **GAMESS**](MOODLE-LINK_TO_REPLACE)
# 2.  [Instructions for Installing **Avogadro**](MOODLE-LINK_TO_REPLACE)
# 3.  [Instructions for Installing **MacMolPlt**](MOODLE-LINK_TO_REPLACE)
# 4.  [Instructions for using GAMESS (**Monday**)](MOODLE-LINK_TO_REPLACE)
# 5.  [Instructions for energy profiles in GAMESS (**Wednesday**)](MOODLE-LINK_TO_REPLACE)
# 6.  [Instructions for energy profiles in GAMESS (**Friday**)](MOODLE-LINK_TO_REPLACE)
# 
# ### Extra Resources
# 
# 

# In[ ]:




