# Lesson 6: Reaction Kinetics

From the first year of your journey in chemistry umtil now, you have been studying reaction kinetics. Rate **laws**, integrated rate **equations**, transition state **theory**, the **Arrhenius** and **Eyring** equations and more are in your toolbox and ready to be deployed as we dive deeper into the nature of this important subject. We will create rate laws for **complex reactions** and plot the integrated rate laws using *Python* tools. We will consider how chemical kinetics experiments are **designed**. We will return to the idea of the **reaction coordinate** and explore how we can interpret the structure of the transition state using **Hammond's postulate**.  

## 6.1 Lesson Plan
The plan below is not necessarily what will happen in class – it is merely what I **hope** will happen in class. We will explore the following subjects and ideas&hellip;

- Review (Ch. 7.1, 7.2, 7.4)
    - Rate laws 
        - The pre-equilibrium approach
        - The steady-state assumption (Ch. 7.5)
    - Reaction coordinates
    - The transition state and transition state theory
    - Using the Arrhenius and Eyring equations
    - Reaction Kinetics Experiments 
        - 1<sup>st</sup> and 2<sup>nd</sup> order reactions
        - Pseudo first order conditions and initial rate methods
- Core statements in physical organic chemistry (Ch. 7.3) 
    - The Hammond Postulate
    - The Curtin-Hammett principle
    - Microscopic reversibility
    - The reactivity-selectivity principle
    - Kinetic vs. thermodynamic control
- What is a reaction coordinate, really? I mean really? No really, what is a reaction coordinate? Are you ready for the truth? (Ch. 7.1, 7.8)
- Multiple axes in reaction coordinates (Ch. 7.8) 
    - Changes in TS structure caused by changes in reactant structure (Ch. 7.8)
- Review of experimental design (Ch. 7.6) 

## 6.2 Learning Goals
After reading the suggested textbook section and practicing the problems you should be able to&hellip;

- Identify the likely **rate determining step** in a reaction and construct a **rate law** from a reaction scheme.
- Draw a reaction **mechanism** using curved arrows that describes a **transition state** for that reaction.
- Understand that the **curved arrows** are really just way to **describe** the transition state.
- **Define and apply** the Hammond postulate, the reactivity-selectivity principle, microscopic reversibility and the Curtin-Hammett principle.
- Describe how to use the idea of **kinetic vs. thermodynamic control** to provide a strategy for maximizing the yield of desired reaction products.
- Understand that changes in bonds as we pass through a transition state can be **concurrent** but **asynchronous** and how this reflects in the structure of the T.S. and the **path** of the **reaction coordinate**.
- **Predict** changes in T.S. structure as we **change** the structure of the reactants.
- **Design an experiment** to investigate reaction kinetics in a given reaction
- **Construct** a rate law from a **complex reaction scheme** using the pre-equilibrium
assumption of steady-state assumption.
- Be able to **interpret data** from reaction kinetics **experiments**.

## 6.3 Assignment \#6

The following assignment is to be submitted via moodle before the Friday meeting.

### The Instructions
This section describes the **activity** that you are to perform for the assignment. Do the following&hellip;

> Draw a **reaction coordinate diagram** to demonstrate the core statements of physical organic chemistry in the list below. Then **write** a justification of how each diagram demonstrates the idea that you presenting. **Math** can be useful in backing up your explanation. Do **all five** activities.
- The Hammond Postulate
- The reactivity-selectivity principle 
- The Curtin-Hammett principle
- Microscopic reversibility
- Kinetic vs. thermodynamic control

### The Deliverable

> Make a clear and professional report of **one** of these core concepts. **Choose** a subject using the table below. You will have **randomly** been assigned a topic by drawing cards. **Draw** the reaction coordinate and **explain** how it is consistent with the idea that you are presenting. Can math help you prove your point?

Make a concise one-page **document** with the diagram appropriately sized and the explanatory text below. Don’t forget a title, you name, a figure legend, etc. You may hand-draw the diagram but, when you photograph it, please **adjust** contrast and brightness so that the lines are dark and the paper is white. I cannot interpret shades of grey. I am a graphical extremist. My world is black or white.

**I dare you** to draw your coordinate diagram by using a vector graphics editor (*Inkscape* is a free example). Presentation programs like Microspft *Powerpoint* also have drawing tools. Hand-drawn is very "kindergarten" and the *Shark Tank*&trade; investors agree with me.

| Card     |    Topic                              |
| :------- | :-------                              |
| 1 or 6   |  The reactivity-selectivity principle |
| 2 or 7   |  The Curtin-Hammett principle         |
| 3 or 8   |  Microscopic reversibility            |
| 4 or 9   |  Kinetic vs. thermodynamic control    |
| 5 or 10  |  The Hammond Postulate                |

### Grading

**Half** of the grade will be for your **answer** and **half** will evaluate how neat, **clear and professional** your are in communicating your answer. Feel free to use a chemical drawing program. Take pride in your work.

## 6.4 Lesson Schedule

### Monday 

You will **review** the basics of chemical kinetics **on your own**. (Ch. 7.1, 7.2 and 7.4. We will **start** the meeting reviewing the basic assumptions of physical chemistry (Ch. 7.3) and then **demonstrate** the math of some complex rate laws (Ch. 7.5). We will briefly remind ourselves about **integrating** simple rate laws. The integration of complex rate equations will be demonstrated using *Python* numerical method tools. We can integrate anything without actually integrating. 

#### Reading

> **Read** Chapter 7.1 to 7.5

#### Suggested Problems

> **Attempt** the following problems from Ch. 7: 3-7, 9, 11, 13 & 14

### Wednesday

The idea of **transition state structure** and how it can be influenced by changes in the reactants or environment will be discussed. The More-O'Farrel-jencks plot will be introduced as a tool for **visualizing** this concept.  

#### Reading

> **Read** Chapter 7.6 to 7.8

#### Suggested Problems

> **Attempt** the following problems from Ch. 7: 8, 10, 12, 15–17 & 23–25

### Friday

There will be a **short quiz** featuring problems adapted from the suggested textbook problems above. After the **presentations** we will then discuss how the plots in our assignment demonstrated the core ideas of reaction kinetics. Finally the **topics** for the next lesson will be introduced. Look ahead to Lesson 7 to see what you should prepare for Monday.

#### Presentations

Two of you will have been **selected** on Monday to present the results of the assignment. Imagine you are the professor trying to **explain** your idea to the class.

## 6.5 Resources

### Jupyter Notebooks

The following notebooks have been made in advance and are available on the moodle site.
1. [Graphing Integrated Rate Laws](Resource_Moodle_Link.md)  TBA
2. [3D Energy Surface](Resource_Moodle_Link.md)  TBA 

### For This Lesson

1. [Integrating Rate Equations](Resource_Moodle_Link.md)  
    - I wrote this document several years ago for my physical organic class as a review of previous topics in reaction kinetics. It presents the basics of creating a rate law and integrating it to obtain an equation that relates the concentration of reactants (or products) to time. Such equations will enable you to obtain rate constants from conc. vs. time data.

 ### Extra Resources

[Numerical Methods using Python (scipy)](https://www.southampton.ac.uk/~fangohr/teaching/python/book/html/16-scipy.html)

https://scicomp.stackexchange.com/questions/24066/solve-rate-equations-with-different-reaction-orders-using-scipy-ode

https://personal.math.ubc.ca/~pwalls/math-python/

