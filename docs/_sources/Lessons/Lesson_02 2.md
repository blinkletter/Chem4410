# Lesson 2: Molecular Structure
What holds the world together? **Chemical bonds**. What are they? They are not lines or dots, they are an arrangement of electrons and nuclei that are lower in energy than other options. Let us explore what bonds really are by considering the **electronic structure** of a molecule.

## 2.1 Lesson Plan
The plan below is not necessarily what will happen in class – it is merely what I **hope** will happen in class. We will explore the following subjects and ideas&hellip;
- **Electronic structure** in molecules: Lewis structure and VSEPR theory 
- **Hybrid orbitals**, &pi; and &sigma; bonds and resonance
- Constructing **Molecular orbitals** (the textbook presents a fairly complicated method for building accurate molecular orbitals using hybrid orbitals. I will be presenting a simpler method that produces less accurate but equally useful molecular orbitals for interpreting reactivity). 
- We will **construct molecular orbitals** for alkenes, ketones and enolates and discuss how the shape and size of the orbitals directs reactivity. **See the Molecular Orbital Tutorial** described in the resources section below and available on the Moodle site.
- We will then explore how molecular orbital theory revelas details that Lewis structure cannot and explore this idea using **Hückel Molecular orbital theory (HMOT)**.
    - Interpreting the **reactivity** of an alkene and a carbonyl group to electrophiles and nucleophiles
    - Using Huckel molecular orbital theory (HMOT) to investigate the properties of **conjugated and aromatic** MO systems.
        - The example of the allyl cation and anion
        - The example of the benzyl cation and phenolate anion
        - The example of naphthalene and azulene
- The computational; power of **Python** will be introduced along with the convenience of **Jupyter Notebooks**. 

## 2.2 Learning Goals
After reading the suggested textbook section and practicing the problems you should be able to&hellip;

- Understand how **hydrid orbitals** are constructed from atomic orbitals according to bond angles.
- Calculate the **hydridization** of a carbon atom from bond angles and use this information to **interpret electronic structure**.
- Construct an approximate **molecular orbital diagram** from a basis set of atomic orbitals and be able to **predict reactivity** and relative stability using the diagram.
- Use the results of a **HMOT calculations** to interpret reactivity in a conjugated or aromatic system.
- Use HMOT to estimate the effects of **polar atoms** in that conjugated system on the MO arrangement.
- Be able to use interactive **Python** to solve computational problems.


## 2.3 Assignment \#2

The following assignment is to be submitted via moodle before the Friday meeting.

### The Instructions
This section describes the **activity** that you are to perform for the assignment. Do the following&hellip;

> **Consider** the two arrow-pushing in {numref}`directive-fig` below for the formation of a carbocation from an alkene and from a ketone. **Do you agree** with the arrow pushing? Think about how the arrow-pushing fits with what you know about the **frontier molecular orbitals** involved.

```{figure} ../Lessons/Lesson_02/L02-01.png
---
width: 500px
name: directive-fig
---
*Protonation of alkene and protonation of a carbonyl group*
```

### The Deliverable

> **Create** a document in which you present the approximate  **molecular orbital diagram** for each reactant and **identify** the **frontier molecular orbitals**. **Draw** the **transition state** based on the arrow pushing as presented. If you find the TS unlikely, **draw** the **correct** transition state and correct arrow psuhing reaction scheme. Explain why you **agree or disagree with the arrow pushing**. Be brief in your explanation but be clear. Provide a corrected reaction scheme if needed.

### Grading

**Half** of the grade will be for your **answer** and **half** will evaluate how neat, **clear and professional** your are in communicating your answer. Feel free to use a chemical drawing program. Take pride in your work.


## 2.4 Lesson Schedule

### Monday 

We will begin with a discussion of **Lewis structure** and how it is surprisingly effective in approximating the information available from more sophisticated **local molecular orbital (LMO)** approaches. We will then review molecular orbital theory and construct a **molecular orbital diagram** using the LMO method. How does arrow pushing and Lewis structures relate to the molecular orbital diagrams of reactants and products?

#### Reading

> **Read** Chapter 1.1 to 1.4 (feel free to skim section 1.2 and 1.3) <br>
> **Read** the [Molecular orbital Tutorial](Resource_Moodle_Link.md) described in the resources described below and available on the moodle page. <br>
> Read the instructions and **install** the **Anaconda** package. This will give you the tools to use Jupyter notebooks and Python.

#### Suggested Problems

> **Attempt** the following problems at the end of Chapter 1: 1, 2, 3, 4, 5, 6, & 8

### Wednesday

We will discuss **simplified Hückel molecular orbital theory (SHMOT)** and use the math of this approach to calculate the molecular orbitals of butadiene and acrolein and discuss what is revealed about their reactivity.

We will use a *Python* tool to **easily and quickly calculate** the molecular orbitals for a handful of molecules: furan, pyrole and the C<sub>p</sub> anion. **Naphthalene and azulene** are aromatic compounds with the same number of carbons and electrons, yet they have very different properties. Can SHMOT reveal why? You will see how computers can be your friends. 


#### Reading

> **Read** Chapter 14.3 & 14.5 <br>
> **Examine** the Jupyter-book [Python and Chemistry](https://blinkletter.github.io/MathWithPython/) described in the resources section below and available on the moodle page <br>
> **Examine** the Jupyter-book for [HMOT calculations](Resource_Moodle_Link.md) described in the resources section below and available on the moodle page.

#### Suggested Problems

> **Attempt** the following problems at the end of Chapter 1: 7, 15 & 32
 <br>
> **Attempt** the following problems at the end of Chapter 14: 9, 11, 26 

### Friday

In our third meeting for this lesson there will be a **short quiz** featuring problems adapted from the suggested textbook problems above. We will review using *Python* tools to perform **SHMOT calculations** and introduce the seemingly endless tools made available by other chemists for your use. Finally the topics for the **next lesson** will be introduced. **Look ahead** to Lesson 3 to see what you should prepare for Monday. 

#### Presentations

> Two of you will have been selected on Monday to present the results of the assignment. You will each be give one of the two molecules to present.

#### Reading

> **Review** Chapter 1,1, 1,4, 14.3 & 14.5  <br>

#### Suggested Problems

> **Explore** the Jupyter notebooks and change them to calculate the &pi;-MOs of a molecule of your choice. Please **practice** with them before the Friday meeting.

````{admonition} A Suggested Personal Schedule

As we **get started**, here is a suggested schedule for getting it all done. The purpose of this schedule is to make the case for **starting early** on your weekly efforts to make **best use** of your time. 

```{admonition} Friday and the Weekend

**Last week** on Friday you will have looked ahead to this chapter and read this text so you will know to start on Friday. 

1. Read the **assigned** readings for Monday and attampt the **suggested** problems.

2. For the **assignment**, use what you learned in the reading to **start** sketching out the molecular orbitals.
```
```{admonition} Monday and Tuesday

On Monday you can ask questions. You will have **questions** if you have begun the work. You will participate in a discussion of how Lewis structure relates to molecular orbitals and practice using graphical methods to combine atomic orbitals. Now you can proceed by doing the following:

1. **Complete** the molecular orbital **diagram** for both systems in the assignment. Then **begin** making a neat and tidy version for you report. Try to see how the frontier orbitals **match up** (or not) with the **arrow-pushing** in the proposed reaction mechanisms.

2. **Read** the assigned readings for Wednesday and **attempt** the suggested problems.
```
```{admonition} Wednesday and Thursday

Oh you will hopefully have more **questions**. On Wednesday you can ask them. You will be introduced to using *Python* notebooks to make Hückel molecular orbital theory calculations.

1. Now, after seeing **further examples** of molecular orbitals and mechanism, complete the assignment report. You will be better able to construct MOs in conjugated systems after gaining an introduction to HMOT.

2. Don't study for the quiz. **Doing** the problems is all you need.

3. **Hack** the Jupyter notebooks demonstrated in class. Try **different** molecules. We've demonstrated naphthalene and azulene, so try the **molecules** in problem 14.10 that you would have noticed while trying the suggested problems.

4. For the two **chosen ones** who are asked to present their assignments, make **two slides** explaining your work and presenting your MO digram and conclusions.
```
```{admonition} Friday

You will submit your **assignments** before class. In class there will be the **quiz** followed by the two short **presentations**. Discussion may follow. You will get a heads up on the **next topic** and will **look ahead** to the next chapter to see what you need to do this weekend.

That's it. Rinse and repeat. **Apply** this schedule to every lesson for best results. Always **start early** on problems and assignments. You can't ask questions at midnight.

```
````

## 2.5 Resources

### For This Lesson

#### Jupyter Books

The following notebooks have been made in advance and are available in Jupyter-book format. The individual Jupyter notebooks can be downloaded via a link at the top of each chapter in the Jupyter-book.

1. [Python and Chemistry](Resource_Moodle_Link.md)
     - A Jupyter-book introducing some basic skills in using *Python* to perform calculations and make plots for chemistry. Feel free to cut and paste all the code for your own projects.

2. [HMOT calculations using Python](Resource_Moodle_Link.md)
    - A Jupyter-book that will take you through some ways to use *Python* to perform simplified Hückel molecular orbital 


#### Molecular Orbital Theory

1.  [Molecular Orbital Tutorial](Resource_Moodle_Link.md)
    - I wrote this review to present a simpler method for constructing a molecular orbital system than that given in the text- book. The textbook method is better and more generally applicable. My method is lesser in every category but works well most of the time. A PDF file on the moodle site

### Extra Resources

#### Molecular Orbital Theory

3. [Hybrid Orbitals and Bonding](http://www.cpp.edu/~psbeauchamp/pdf/314_lect_02.pdf) 
      - This is an overview of hybrid orbitals and bonding from Cal Poly Pomona. 
4. [Molecular Orbitals and Organic Chemical Reactions](https://onlinelibrary-wiley-com.proxy.library.upei.ca/doi/book/10.1002/9780470684306)
      - A textbook that examines organic chemistry through the lens of molecular orbital theory. there is a more research oriented "reference version" that contains links to original literature available [here](https://onlinelibrary-wiley-com.proxy.library.upei.ca/doi/book/10.1002/9780470689493).

#### Python for Chemists

8. [Scientific Computing for Chemists with Python](https://weisscharlesj.github.io/SciCompforChemists/intro.html)
     - An online textbook introducing Python and data science tools to chemists who have not used it before.
9. [An Introduction to Python for Chemists](https://pythoninchemistry.org/intro_python_chemists/intro.html)
     - An online textbook with a short overview of important topics in python.
7. [Python For Chemistry in 21 Minutes](http://felix.unife.it/Didattica/Articoli/17518-OBoyle.pdf)
     - A slide deck justifying and introducing the use of Python for chemists.
9. [Python in Chemistry blog](https://pythoninchemistry.org/)
     - This is a collection of articles on using Python in chemistry research and eduaction.
10. [The Good Research Code Handbook](https://goodresearch.dev/index.html)
     - this is an online textbook in wfitkng good code for research. It's mostly about good habits.
11. [ChemPy](https://pypi.org/project/chempy/)
     - A python module with chemistry tools. 
12. [Teaching Programming across the Chemistry Curriculum](https://pubs.acs.org/doi/book/10.1021/bk-2021-1387)
     - An ACS symposium series arguing for more computing in chemistry
13. [Awesome Python Chemistry](https://github.com/lmmentel/awesome-python-chemistry)
     - A collection of resources for the Python-friendly chemist.
14. [Python For Engineers And Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html)
     - "Python Programming And Numerical Methods: A Guide For Engineers And Scientists" is a full exploration of python as a tool for scientists. Highly recommended when you are ready for the next level.