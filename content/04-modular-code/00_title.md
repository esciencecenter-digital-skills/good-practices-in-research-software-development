<!--
title: Code Modularization
description: Code Modularization
author: Barbara Vreede
version: 4.3.1
plugins: RevealMarkdown, RevealHighlight, RevealMath.KaTeX, RevealMenu, RevealNotes, RevealSearch, RevealZoom
-->

<!-- .slide: data-state="blue_overlay yellow_flag yellow_strip purple_half_circle_bottom purple_blob right_e_top" data-background-video="./files/Mood video Homepage 2.mp4" data-background-video-loop data-background-video-muted="true" -->

# Code Modularization
## Subtitle

[Barbara Vreede](mailto:b.vreede@esciencecenter.nl) |  [Ole Mussmann](mailto:o.mussmann@esciencecenter.nl)


===

<!-- .slide: data-state="standard" -->

# What is modularity?
- It is a way to organize and structure code
- Software is 'built up' from smaller elements
- Each element handles a specific (set of) task(s)
- Elements are self-contained and independent

Eventually, we want to build **complex behavior** from **simple components**

---

<!-- .slide: data-state="standard" -->

## What are blocks?

- functions
- functions
- classes
- modules
- libraries/packages
- programs

---

<!-- .slide: data-state="standard" -->

## Why Modularize Code?

<img width="900" alt="think in building blocks" src="https://user-images.githubusercontent.com/5747405/207459058-59c88b4c-1401-428f-b28a-0ac3e72bd964.png">

===

<!-- .slide: data-state="standard" -->

## Why Modularize Code?

- Maintenance
- Reusability
- Robustness
- Scalability
- Innovation
- Flexibility
- ...

Note:
- Maintenance
  - Modular code is easier to read, understand, and therefore to maintain.
  - An independent module can be debugged, changed, or optimized, without it being necessary to understanding the rest of the codebase.
- Reusability
  - An independent module can live outside the context it was written for.
  - It can be reused by another project, and serve a purpose in a different environment.
- Robustness
  - Modules are prime targets for tests.
  - A well defined module is easier to test, and therefore easier to debug or keep bug-free.
- Scalability
  - Modular code keeps the complexity of a project low by design.
  - This makes it easier to scale up without creating huge issues. 
- Innovation
  - Modules increase the capabilities and power of a project, without increasing the complexity on a maintenance level.
  - Rearranging old modules can lead to powerful new applications.
- Flexibility
  - With code existing of independent modules, with low or absent interdependency, the codebase becomes flexible and amenable to change.
  - Modifications can be made in a targeted way, without unexpected (disastrous) consequences.

---

<!-- .slide: data-state="standard" -->

![](./files/development-speed.svg)

===

<!-- .slide: data-state="standard" -->


## How do we make code more modular?

This process can be done iteratively: modules are built up of smaller modules, which are built up of... etc.

---

<!-- .slide: data-state="standard" -->

### Identify processes and functions
Break the project down into sub-steps and sub-tasks.

---

<!-- .slide: data-state="standard" -->

### Create modules
Create functions, classes, or even full packages for processes and functions identified in step 1. Move existing code into this structure.

---

<!-- .slide: data-state="standard" -->

### Refactor
Refactor the code in each module to make it as self-contained as possible. For example, remove dependencies on external code or data where possible.
Clearly define the task that a module should do, and edit away any other functionality.

---

<!-- .slide: data-state="standard" -->

### Test
Test each module individually to ensure no errors or bugs are creeping in.
Use tests also to again look critically at the function that should be performed by a module.

===

<!-- .slide: data-state="standard" -->

## Do One Thing (and do it well)
- One _function_ for one purpose
- One _class_ for one purpose
- One _package_ for one purpose

===

<!-- .slide: data-state="standard" -->

## Don't Repeat Yourself

- Write routines (i.e. code that gets reused) into functions
- Identify potential functions by _action_: functions perform tasks (e.g. sorting, plotting, saving a file, transform data...)


---

<!-- .slide: data-state="standard" -->

## Functions are...
- Functions are smaller code units reponsible of one task.
- Functions are meant to be reused
- Functions accept arguments (though they may also be empty!)
- Functions generate output

---

<!-- .slide: data-state="standard" -->

## Functions do not...

... necessarily make code shorter (at first)! Compare:

```python=
indexATG = [n for n,i in enumerate(myList) if i == 'ATG']
indexAAG = [n for n,i in enumerate(myList) if i == 'AAG']
```


```python=
def indexString(inputList,z):
    zIndex = [n for n,i in enumerate(li) if i == z]
    return zIndex
    
indexATG = indexString(myList,'ATG')
indexAAG = indexString(myList,'AAG')
```

---

<!-- .slide: data-state="standard" -->


## When to make functions?

Always.

---

<!-- .slide: data-state="standard" -->

## When to make more functions?
- if you have too many levels of indentation
- if a function gets too long
- if a function does more than one thing
- if you find it hard to name a function

---

<!-- .slide: data-state="standard" -->

## Keep your functions pure

- Pure functions have no notion of state: They take input values and return values
- Given the same input, a pure function always returns the same value

Example: pure, no side effects
```python=
def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c
    temp_c = fahrenheit_to_celsius(temp_f=100.0)
    print(temp_c)
```

Example: stateful, side effects
```python=
f_to_c_offset = 32.0
f_to_c_factor = 0.555555555
temp_c = 0.0
def fahrenheit_to_celsius_bad(temp_f):
    global temp_c
    temp_c = (temp_f - f_to_c_offset) * f_to_c_factor
    fahrenheit_to_celsius_bad(temp_f=100.0)
    print(temp_c)
```

---

<!-- .slide: data-state="standard" -->

## Pure functions are easier to

- Test
- Understand
- Reuse
- Parallelize
- Simplify
- Optimize
- Compose

---

<!-- .slide: data-state="standard" -->

## Divide and conquer

- Split the code up
- Construct your program from parts:
  - functions
  - modules
  - packages (Python) or libraries (C or or C++ or Fortran)

---

<!-- .slide: data-state="standard" -->

## Keep it simple

- Avoid using complex data structures or algorithms
- Instead, try to use simple, built-in data types and functions whenever possible.
- Use clear and consistent indentation and naming conventions
- Use descriptive and meaningful names for your variables, functions, and other code elements.
- Avoid using global variables whenever possible
- Instead, use local variables and functions to isolate and manage your data.
- Avoid using complex or nested control flow statements
- Instead, try to break your code down into smaller, simpler pieces that can be handled separately.

===

<!-- .slide: data-state="standard" -->

- building blocks
  - interface
  - naming
  - testing
  - no side effects
  - stateless

- number of blocks not too high
- readability as a code smell

