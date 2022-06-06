#!/usr/bin/env python
# coding: utf-8

# # Lesson 2: Molecular Structure
# What holds the world together? **Chemical bonds**. What are they? They are not lines or dots, they are an arrangement of electrons and nuclei that are lower in energy than other options. Let us explore what bonds really are by considering the **electronic structure** of a molecule.
# 
# -----
# ## 2.1 Lesson Plan
# The plan below is not necessarily what will happen in class – it is merely what I **hope** will happen in class. We will explore the following subjects and ideas$\ldots$
# - **Electronic structure**in molecules: Lewis structure and VSEPR theory 
# - **Hybrid orbitals**, $\pi$ and $\sigma$ bonds and resonance
# - Constructing **Molecular orbitals** (the textbook presents a fairly complicated method for building accurate molecular orbitals using hybrid orbitals. I will be presenting a simpler method that produces less accurate but equally useful molecular orbitals for interpreting reactivity). 
# - We will **construct molecular orbitals** for alkenes, ketones and enolates and discuss how the shape and size of the orbitals directs reactivity. **See the Molecular Orbital Tutorial** described in the resources section below and available on the Moodle site.
# - We will then explore how molecular orbital theory revelas details that Lewis structure cannot and explore this idea using **Hückel Molecular orbital theory (HMOT)**.
#     - Interpreting the **reactivity** of an alkene and a carbonyl group to electrophiles and nucleophiles
#     - Using Huckel molecular orbital theory (HMOT) to investigate the properties of **conjugated and aromatic** MO systems.
#         - The example of the allyl cation and anion
#         - The example of the benzyl cation and phenolate anion
#         - The example of naphthalene and azulene
# - The computational; power of **Python** will be introduced along with the convenience of **Jupyter** Notebooks. 
# 
# -----
# ## 2.2 Learning Goals
# After reading the suggested textbook section and practicing the problems you should be able to$\ldots$
# 
# - Understand how **hydrid orbitals** are constructed from atomic orbitals according to bond angles.
# - Calculate the **hydridization** of a carbon atom from bond angles and use this information to **interpret electronic structure**.
# - Construct an approximate **molecular orbital diagram** from a basis set of atomic orbitals and be able to **predict reactivity** and relative stability using the diagram.
# - Use the results of a **HMOT calculations** to interpret reactivity in a conjugated or aromatic system.
# - Estimate the effects of **polar atoms** in that conjugated system on the MO arrangement.
# - Be able to use interactive **Python** to solve computational problems.
# 
# 
# -----
# ## 2.3 Assignment \#2
# 
# The following assignment is to be submitted via moodle before the Friday meeting.
# 
# ### Instructions
# This section describes the **activity** that you are to perform for the assignment. Do the following$\ldots$
# 
# > **Consider** the two arrow-pushing in {numref}`directive-fig` below for the formation of a carbocation from an alkene and from a ketone. **Do you agree** with the arrow pushing? Think about how the arrow-pushing fits with what you know about the **frontier molecular orbitals** involved.
# 
# ```{figure} ../Lessons/Lesson_02/L02-01.png
# ---
# width: 500px
# name: directive-fig
# ---
# *Protonation of alkene and protonation of a carbonyl group*
# ```
# 
# 
# ### The Report
# > **Create** a document in which you present the approximate  **molecular orbital diagram** for each reactant and **identify** the **frontier molecular orbitals**. Using this information either **confirm or criticize the arrow pushing**. Be brief in your explanation but be clear. Provide a corrected reactionreaction scheme if needed.
# 
# 
# ### Grading
# **Half** of the grade will be for your **answer** and **half** will evaluate how neat, **clear and professional** your are in communicating your answer. Feel free to use a chemical drawing program. Take pride in your work.
# 
# 
# 
# -----
# ## 2.4 Lesson Schedule
# 
# ### Monday 
# 
# We will begin with a discussion of Lewis structure and how it is surprisingly effective in approximating the information available from more sophisticated local molecular orbital (LMO) approaches (LMO). We will then review molecular orbital theory and construct a molecular orbital diagram using the LMO method. How does arrow pushing and Lewis structures relate to the molecular orbital diagrams of reactants and products?
# 
# #### Reading
# 
# > **Read** Chapter 1.1 to 1.4 (feel free to skim section 1.2 and 1.3) <br>
# > **Read** the **Molecular orbital Tutorial** described in the resources described below and available on the moodle page.
# > Read the instructions and **install** the **Anaconda** package. This will give you the tools to use Jupyter notebooks and Python.
# 
# #### Suggested Problems
# 
# > **Attempt** the following problems at the end of Chapter 1: 1, 2, 3, 4, 5, 6, 7, 8, 15 & 32
# 
# ### Wednesday
# 
# We will discuss **simplified Hückel molecular orbital theory (SHMOT)** and use the math of this approach to calculate the molecular orbitals of butadiene and acrolein and discuss what is revealed about their reactivity.
# 
# #### Reading
# 
# > **Read** Chapter 14.3<br>
# > **Examine** the Jupyter notebooks introducing Python described below and available on the moodle page
# 
# #### Suggested Problems
# 
# > **Attempt** the following problems at the end of Chapter 14: 9, 11, 26, 41 & 43
# 
# ### Friday
# 
# In our third meeting for this lesson there will be a **short quiz** featuring problems adapted from the suggested textbook problems above. We will explore using Python tools to perform **SHMOT calculations** and introduce the seemingly endless tools made available by other chemists for your use. 
# 
# We will **easily and quickly calculate** the molecular orbitals for a handful of molecules. Furan, pyrole and the Cp anion? **Naphthalene and azulene** are aromatic compounds with the same number of carbons and electrons, yet they have very different properties. Can SHMOT reveal why? You will see how computers can be your friends. 
# 
# Finally the topics for the **next lesson** will be introduced. **Look ahead** to Lesson 3 to see what you should prepare for Monday. 
# 
# #### Reading
# 
# > **Read** Chapter 14.3 & 14.5  <br>
# > **Read and Use** the Jupyter notebooks for HMOT described below and available on the moodle page
# 
# #### Suggested Problems
# 
# > **Explore** the Jupyter notebooks and change them to calculate the $\pi$-MOs of a molecule of your choice. Please **practice** with them before the Friday meeting.
# 
# ------
# ## 2.5 Resources
# 
# ### Jupyter Notebooks
# 
# The following notebooks have been made in advance and are available on the moodle site.
# 
# #### Notebooks for Introducing Python
# 
# 
# 
# #### Notebooks for HMO theory
# 1. HMOT calculations using Eigenvectors
# 2. HMOT calculations using module
# 
# 
# ### For This Lesson
# #### Molecular Orbital Theory
# 1.  [Molecular Orbital Tutorial](MOODLE-LINK_TO_REPLACE)
#     - I wrote this review to present a simpler method for constructing a molecular orbital system than that given in the text- book. The textbook method is better and more generally applicable. My method is lesser in every category but works well most of the time. A PDF file on the moodle site
# 
# 
# 
# ### Extra Resources
# 
# #### Molecular Orbital Theory
# 3. [Hybrid Orbitals and Bonding](http://www.cpp.edu/~psbeauchamp/pdf/314_lect_02.pdf) 
#       - This is an overview of hybrid orbitals and bonding from Cal Poly Pomona. 
# 4. [Molecular Orbitals and Organic Chemical Reactions](https://onlinelibrary-wiley-com.proxy.library.upei.ca/doi/book/10.1002/9780470684306)
#       - A textbook that examines organic chemistry through the lens of molecular orbital theory. there is a more research oriented "reference version" that contains links to original literature available [here](https://onlinelibrary-wiley-com.proxy.library.upei.ca/doi/book/10.1002/9780470689493).
# 
# #### Python for Chemists
# 8. [Scientific Computing for Chemists with Python](https://weisscharlesj.github.io/SciCompforChemists/intro.html)
#      - An online textbook introducing Python and data science tools to chemists who have not used it before.
# 9. [An Introduction to Python for Chemists](https://pythoninchemistry.org/intro_python_chemists/intro.html)
#      - An online textbook with a short overview of important topics in python.
# 7. [Python For Chemistry in 21 Minutes](http://felix.unife.it/Didattica/Articoli/17518-OBoyle.pdf)
#      - A slide deck justifying and introducing the use of Python for chemists.
# 9. [Python in Chemistry blog](https://pythoninchemistry.org/)
#      - This is a collection of articles on using Python in chemistry research and eduaction.
# 10. [The Good Research Code Handbook](https://goodresearch.dev/index.html)
#      - this is an online textbook in wfitkng good code for research. It's mostly about good habits.
# 11. [ChemPy](https://pypi.org/project/chempy/)
#      - A python module with chemistry tools. 
# 12. [Teaching Programming across the Chemistry Curriculum](https://pubs.acs.org/doi/book/10.1021/bk-2021-1387)
#      _ An ACS symposium series arguing for more computing in chemistry

# 
