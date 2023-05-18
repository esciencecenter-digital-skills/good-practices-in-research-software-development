<!--
title: Code Modularization
description: Code Modularization
author: Barbara Vreede, Ole Mussmann
version: 4.3.1
plugins: RevealMarkdown, RevealHighlight, RevealMath.KaTeX, RevealMenu, RevealNotes, RevealSearch, RevealZoom
-->

<!-- .slide: data-state="blue_overlay yellow_flag yellow_strip purple_half_circle_bottom purple_blob right_e_top" data-background-video="./files/Mood video Homepage 2.mp4" data-background-video-loop data-background-video-muted="true" -->

# Developing Modular Code

[Barbara Vreede](mailto:b.vreede@esciencecenter.nl) |  [Ole Mussmann](mailto:o.mussmann@esciencecenter.nl)

===

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## What is modularity?

- Software is 'built up' from smaller elements
<!-- .element: class="fragment" data-fragment-index="3" -->
- Elements are self-contained and independent
<!-- .element: class="fragment" data-fragment-index="4" -->
- Each element handles a specific (set of) task(s)
<!-- .element: class="fragment" data-fragment-index="5" -->


**Simple components** build **complex behavior**.
<!-- .element: class="fragment" data-fragment-index="6" -->

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png" -->

## Modular code

<img width="900" alt="think in building blocks" src="https://user-images.githubusercontent.com/5747405/207459058-59c88b4c-1401-428f-b28a-0ac3e72bd964.png">

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png" -->

## What are these blocks/elements?

- functions
- functions
- classes
- modules
- libraries/packages
- programs


===

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Why write modular code?

To increase robustness:

<img width="200" alt="testing a single module" src="./files/testing_module.png">

- A well-designed module can be tested.
- This helps keep the codebase well-functioning and bug-free.

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Why write modular code?

To make maintenance easier:

<img width="300" alt="testing a module taken from a larger project" src="./files/testing_module_maintenance.png">

- Modular code is more readable and understandable.
- Modules can be debugged separately.

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Why write modular code?

To allow reusability:

<img width="400" alt="reuse a module in another project" src="./files/reuse_module.png">

- A module can live independent of its original context
- It can be reused by another project

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Why write modular code?

To facilitate scalability:

<img height="300" alt="scalability" src="./files/scalability.png">


<div>

- Complexity remains low by design
- This creates space for scaling up

</div>

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Why write modular code?

To create opportunities for innovation:

<img height="300" alt="tetris shows innovation" src="./files/tetris_innovation.png">

- Modules increase the capabilities and power of a project
- Rearrange old modules for new applications

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->


<img height="500" alt="modularity meme" src="./files/modularity_meme.png">

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

<img width="800" alt="development speed" src="./files/development-speed.svg">

===

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## A good module...

- has a clear interface

---


<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

<img height="500" alt="Modules with bad interaction" src="./files/modules-bad-connection.png">
<!-- .element: class="fragment" data-fragment-index="2" -->
<img width="100" src="./files/whitebg.png">

<img height="500" alt="Modules with clear connecting interfaces" src="./files/modules-good-connection.png">
<!-- .element: class="fragment" data-fragment-index="3" -->

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## A good module...

- has a clear interface
- performs limited and clearly defined tasks
- has a good name
<!-- .element: class="fragment" data-fragment-index="2" -->
- is readable
<!-- .element: class="fragment" data-fragment-index="3" -->

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Readability =/= shorter code

Shorter:
```python=
indexATG = [n for n,i in enumerate(myList) if i == 'ATG']
indexAAG = [n for n,i in enumerate(myList) if i == 'AAG']
```

More modular:
```python=
def getIndex(inputList,z):
    zIndex = [n for n,i in enumerate(li) if i == z]
    return zIndex

indexATG = getIndex(myList,'ATG')
indexAAG = getIndex(myList,'AAG')
```

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## A good module...

- has a clear interface
- performs limited and clearly defined tasks
- has a good name
- is readable
- is pure/does not have a 'state'

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## A pure function

has no side-effects:

```python=
def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c

>>> temp_c = fahrenheit_to_celsius(temp_f=77.0)
>>> print(temp_c)
25.0
```

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## A stateful function

changes its environment:

```python=
def fahrenheit_to_celsius(temp_f):
    global temp_c
    temp_c = (temp_f - f_to_c_offset) * f_to_c_factor

>>> f_to_c_offset = 32.0
>>> f_to_c_factor = (5.0/9.0)
>>> temp_c = 0.0
>>> print(temp_c)
0.0
>>> fahrenheit_to_celsius(temp_f=77.0)
>>> print(temp_c)
25.0
```

===

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Focus on readability

- Modular code becomes more readable
- Code is read more than it is written
- Does a reader understand what the code does?
- Bad readability can be a "code smell"

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Identify future functions

- Don't Repeat Yourself (DRY): place reused code into a function
- Identify potential functions by their _action_
    (e.g. "plotting", "transforming", "extracting", "saving")

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Target nested code

Nested code is a prime target for modularization:

```python=
def checkTemperature(degrees):
    if degrees < 0:
        if degrees < -273:
            if degrees < -459:
                print("This temperature is impossible.")
            else:
                print("This temperature is likely Fahrenheit.")
        else:
            print("This temperature is either Celsius or Fahrenheit.")
    else:
        print("This temperature is in Kelvin, Celsius, or Fahrhenheit.")
```

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Reduce nestedness

by extracting modules:

```python=
def validTemp(degrees):
    if degrees < -459:
        return FALSE
    return TRUE

def checkTemperature(degrees):
    if not validTemp(degrees):
        return "invalid temperature"
    if degrees < 0:
        if degrees < -273:
            print("This temperature is likely Fahrenheit.")
        else:
            print("This temperature is either Celsius or Fahrenheit.")
    else:
        print("This temperature is in Kelvin, Celsius, or Fahrhenheit.")
```

---

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

## Let tests help you

- Write tests for each individual module
- Use the test-writing procedure to look critically at the module's function:
    - Is the input/output clear?
    - What can you not yet test? Extract it into a new module.


===

<!-- .slide: data-state="standard" data-background="./files/whitebg.png"  -->

![](https://imgs.xkcd.com/comics/code_lifespan_2x.png)