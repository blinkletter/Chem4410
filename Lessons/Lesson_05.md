# Lesson 5: Acids and Bases
Acids and bases are **core concepts** in chemistry. And it is about much more than *pH*. What is the acidity of 1% sulphuric acid mixture in water? How would you calculate or **measure** it? Now, what is the acidity of a 99% mixture? Does *pH* have any meaning here? We need a way to measure the acidity of **very strong acid mixtures** so that we can use them in **experiments**. You are now ready at last to learn the truth.

I didn't truly understand **acid-base equilibria** until I started graduate school. I hope to save you a year and get the concept across in this course.

## 5.1 Lesson Plan
The plan below is not necessarily what will happen in class – it is merely what I **hope** will happen in class. We will explore the following subjects and ideas&hellip;

- How to **calculate** the fraction of protonated/deprotonated species in a solution of a given acidity. We will make it super easy with a **Jupyter notebook and Python**.
- What does *pK<sub>a</sub>* mean and how is it useful (even when the value seems ridiculous)? (Ch.5.1)
- What is ”acidity”? What is *pH*? I mean, **what is it really**? What if I told you that *pH* is not really −log[H<sup>+</sup>]. Can you handle the truth? (Ch. 5.1)
- Introducing the **Hammett acidity function**, *H<sub>0</sub>*. (Ch. 5.2)
- Predicting **relative acid strengths** by comparing molecular structure (Ch. 5.4)
- **Solvent effects** on acid/base equilibrium (Ch. 5.3) 


## 5.2 Learning Goals
After reading the suggested textbook section and practicing the problems you should be able to&hellip;

- Understand *pH* as an **acidity function**.
- Understand **how** the Hammett acidity function **is determined** for various acid mixtures.
- Determine the **extent of protonation** of a reactant at various *pH* or *H<sub>0</sub>* values.
- **Calculate** the *pK<sub>a</sub>* of a reactant from equilibrium data.
- Understand the **effect of resonance, induction, steric strain and electrostatic effects** on the *K<sub>a</sub>* value of an acidic functional group.
- Be able to **predict** which of two related acids is stronger and explain why.
- Understand the role of **solvent** in determining the *K<sub>a</sub>* value of an acidic functional group.


## 5.3 Assignment \#5

The following assignment is to be submitted via moodle before the Friday meeting.

### The Instructions
This section describes the **activity** that you are to perform for the assignment. Do the following&hellip;

> Create a **plot** of one set of *pK<sub>a</sub>* values against a set of related *pK<sub>a</sub>* values. Perhaps plot *pK<sub>a</sub>* values in water vs. *pK<sub>a</sub>* values in DMSO. Or plot *pK<sub>a</sub>* values in water vs. gas phase. Or plot *pK<sub>a</sub>* values of **substituted benzoic acids** agains *pK<sub>a</sub>* values of substituted phenols or substituted pyridines or substituted something else. An example will be presented in class so you will know exactly what to do.

### The Deliverable

> You will have tried a few different correlations. Pick your favourite and write a **report** using an executable Jupyter notebook as the medium. The notebook will **document** your activity while providing the **code** and **results** of the code. Feel free to start with the example notebook presented during the lesson week and alter it to suit you. You must perform an analysis that is **different** than the one in the sample notebook.

Write your notebook in a **neat** and well organized form. Include **comments** on your observations and attempt to **explain** them. Is the result obvious to you, or is it a surprise? **Submit a .zip file** that contains the notebook and the data file that you created. Data analysis projects are presented with code and raw data in modern journals, often as Jupyter notebooks. Keeping the code and data together **helps others** to follow your work.


### Grading
**Half** of the grade will be for your **answer** and **half** will evaluate how neat, **clear and professional** your are in communicating your answer. Feel free to use a chemical drawing program. Take pride in your work.

## 5.4 Lesson Schedule

### Monday 

We will explore the **math** of acid/base equilibria using Jupyter notebooks as our calculator. We will introduce the idea of the **acidity function**. *pH* is just one of many options for expressing acid strength.

#### Reading

> **Read** Chapter 5.1 \& 5.2  <br>
> **Read and Use** the Jupyter notebooks for acid equilibria described below and available on the moodle page
> **Read and Use** the Jupyter notebooks for aciditry functions described below and available on the moodle page


#### Suggested Problems

> **Attempt** the following problems at the end of Ch. 5: 1, 3, 5, 6, 12 \& 20  <br>
> **Explore** the Jupyter notebooks and change them to suit you

### Wednesday

We will consider how structure affects acidity. The most obvious example is substituted benzoic acids. We will explore examples involving resonance stabilization, aromaticity and hybridization.

#### Reading

> **Read** Chapter 5.3 \& 5.4  <br>
> **Read and Use** the Example Assignment Jupyter notebooks for plotting *pK<sub>a</sub>* values agains each other described below and available on the moodle page

#### Suggested Problems

> **Attempt** the following problems at the end of Ch. 5: 2, 4, 9, 11, 13, 17, 19 \& 21 <br>
> **Explore** the Jupyter notebooks and change them to suit you

### Friday

In our third meeting for this lesson there will be a **short quiz** featuring problems adapted from the suggested textbook problems above. We will then discuss how the plots in our assignment revealed **correlation** (or not) between series of acid strengths. Could this **correlation** be used as a score for how structure affects electron density in a molecule? Finally the topics for the **next lesson** will be introduced. **Look ahead** to Lesson 6 to see what you should prepare for Monday. 

#### Presentations

> Two of you will have been selected on Monday to present the results of the assignment. You will want to **ask** your presentation partner what they are doing so you can be sure that you are both making **different** correlations.


## 5.5 Resources

### Jupyter Notebooks

The following notebooks have been made in advance and are available on the moodle site.

1. [Classic Chem 1110 Acid Equilibrium](Resource_Moodle_Link.md)
2. [Hammett Acidity Function Example](Resource_Moodle_Link.md)
3. [Example Assignment Notebook](Resource_Moodle_Link.md)


### For This Lesson

1. [Tables and Charts of Hammett acidity function values](Resource_Moodle_Link.md) 
    - How acidic is 50% sulfuric acid? You can look up the Ho value of that and other acid mixtures in these charts.

2. [Acid-Base Tutorial](Resource_Moodle_Link.md) 
    - I wrote this review for my biochemistry class several years ago. It may be useful in reviewing the basics of acid-base equi- libria.

3. [Williams’ Compilation of pKa Tables](https://organicchemistrydata.org/hansreich/resources/pka/)
    - This is a famous compilation of pKa data assembled by R. Williams based on an earlier compilation by Westheimer & Jencks.
    
4. [Evans’ pKa Table](https://organicchemistrydata.org/hansreich/resources/pka/) 
    - This is a shorter version of Reich’s compilation of DMSO *pK<sub>a</sub> data (see below) combined with corresponding water pKa data from Williams’ table (see above). 
    
5. [Reich’s pKa Table](https://organicchemistrydata.org/hansreich/resources/pka/)
    - This is a compilation of pKa data curated by Hans Reich. These values are mostly from the famous Bordwell table of pKa values in DMSO. 
    
6. [A Short pKa Table](http://cactus.dixie.edu/smblack/chem2310/)
    - This is a compilation of pKa data curated by Sarah Black. This table focuses on general cases of functional groups and will give a quick survey of pKa values. 
    
7. [Another Short pKa Table](https://organicchemistrydata.org/myers)
    - This is a compilation of pKa data curated by Brian Myers. This table focuses on general trends in functional groups. 

### Extra Resources

