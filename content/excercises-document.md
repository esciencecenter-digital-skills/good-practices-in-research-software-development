
## Day 1 Version control
### Tracking changes exercise
Exercise in breakout rooms. Write down your (individual) answers to the next 3 questions in the collaborative notebook.
#### 1. Which command(s) below would save the changes of myfile.txt to my local Git repository?

1. git commit -m "my recent changes"
2. git init myfile.txt
   git commit -m "my recent changes"
3. git add myfile.txt
   git commit -m "my recent changes"
4. git commit -m myfile.txt "my recent changes"

#### 2. Committing Multiple Files
The staging area can hold changes from any number of files that you want to commit as a single snapshot.

Add some text to ``mars.txt`` noting your decision to consider Venus as a base
Create a new file ``venus.txt`` with your initial thoughts about Venus as a base for you and your friends
Add changes from both files to the staging area, and commit those changes.

#### 3. (optional) A new repository
Create a new Git repository on your computer called bio.
Write a three-line biography for yourself in a file called me.txt, commit your changes
Modify one line, add a fourth line
Display the differences between its updated state and its original state.

### Exploring history exercise
Exercise in breakout rooms. Write down your (individual) answers to the next 3 questions in the collaborative notebook.
#### 1. Recovering Older Versions of a File
Jennifer has made changes to the Python script that she has been working on for weeks, and the modifications she made this morning “broke” the script and it no longer runs. She has spent ~ 1hr trying to fix it, with no luck…

Luckily, she has been keeping track of her project’s versions using Git! Which commands below will let her recover the last committed version of her Python script called `data_cruncher.py?`

1. `$ git checkout HEAD`
2. `$ git checkout HEAD data_cruncher.py`
3. `$ git checkout HEAD~1 data_cruncher.py`
4.  ` $ git checkout <unique ID of last commit> data_cruncher.py`
5. Both 2 and 4

#### 2. Reverting a Commit

Jennifer is collaborating on her Python script with her colleagues and realizes her last commit to the project’s repository contained an error and she wants to undo it. `git revert [erroneous commit ID]` will create a new commit that reverses Jennifer’s erroneous commit. Therefore `git revert` is different to `git checkout [commit ID]` because `git checkout` returns the files within the local repository to a previous state, whereas `git revert` reverses changes committed to the local and project repositories.
Below are the right steps and explanations for Jennifer to use `git revert`, what is the missing command?

1. `________ # Look at the git history of the project to find the commit ID`
2. `Copy the ID (the first few characters of the ID, e.g. 0b1d055).`
3. `git revert [commit ID]`
4. Type in the new commit message.
5. Save and close

#### 3. Understanding Workflow and History

What is the output of the last command in
```
$ cd planets
$ echo "Venus is beautiful and full of love" > venus.txt
$ git add venus.txt
$ echo "Venus is too hot to be suitable as a base" >> venus.txt
$ git commit -m "Comment on Venus as an unsuitable base"
$ git checkout HEAD venus.txt
$ cat venus.txt #this will print the contents of venus.txt to the screen
```
1. Venus is too hot to be suitable as a base
2. Venus is beautiful and full of love
3. Venus is beautiful and full of love
4. Venus is too hot to be suitable as a base
5. Error because you have changed venus.txt without committing the changes

### Exercises for Ignoring Things
#### Ignoring Nested Files
Given a directory structure that looks like:
```
results/data
results/plots
```
How would you ignore only `results/plots` and not `results/data`?

#### (optional) Including Specific Files

How would you ignore all `.dat` files in your root directory except for `final.dat`? Hint: Find out what `!` (the exclamation point operator) does

### 'The remote' exercises
#### GitHub GUI

Browse to your `planets` repository on GitHub. Under the Code tab, find and click on the text that says “XX commits” (where “XX” is some number). Hover over, and click on, the three buttons to the right of each commit. What information can you gather/explore from these buttons? How would you get that same information in the shell?

#### (optional) Push vs. Commit

In this lesson, we introduced the `“git push”` command. How is `“git push”` different from `“git commit”`?



## Day 2 Collaborative distributed version control



### Exercise: Working as a project collaborator (in breakout rooms)

- Log into Github and create a new repository
- Make the repository public
- clone it to your desktop
- add some code
- push the changes to the repository
- Add one person as a collaborator (settings -> Manage Access). Make sure everyone in the group has a collaborator.
- Create an issue in the repo where you are a collaborator
- Clone that repo
- make changes on a new branch
- push the changes
- submit a Pull Request
- wait for approval
- At the same time review a collaborators Pull Request
- (Optionally) Learn about [protecting branches](https://docs.github.com/en/github/administering-a-repository/about-protected-branches) and try it out.

### Exercise: Working as an external contributor (in breakout rooms)
- Remove your group member(s) as collaborators from your repository
- Fork another group members repo (Repository page, top right corner)
- Create an issue on the original repository
- Clone your forked repo to your computer
- Make some changes, use a somewhat real-world example so it makes sense to review it (but don't overdo it).
- Push it to your fork
- Make a change and commit it to the main branch
- push the changes
- make a pull request from your fork to the main repository mentioning the issue
- Consider turning your Pull Request into a draft Pull Request.
- let your code be reviewed by tagging the repo owner using (@Username)
- At the same time review Pull Request using comments on individual lines. Try to act as if it was a real peer review as much as possible.
- Accept or reject the Pull Request
- (Optionally) learn about [merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts) and try it out in your collaboration.


## Day 3: Modular code design

Take a look at the following (terrible) code.

Extract functions from it.

Some things to keep in mind:
- Keep the functions pure (i.e.: no interaction with their environment)
- Good interfaces (input/output) make them testable
- Use good naming practices to describe the functionality

```python=
def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                if temperature % 2 == 0:
                    return "Invalid temperature"
                else:
                    if kelvin % 2 == 0:
                        return "Invalid temperature"
                    else:
                        return celsius, kelvin
            else:
                if celsius % 2 == 0:
                    # Convert Celsius to Fahrenheit
                    fahrenheit = (celsius * (9 / 5)) + 32
                    if fahrenheit < -459.67:
                        # Invalid temperature, below absolute zero
                        return "Invalid temperature"
                    else:
                        if fahrenheit % 2 == 0:
                            return fahrenheit, kelvin
                        else:
                            return fahrenheit, celsius
                else:
                    return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                if temperature % 2 == 0:
                    return "Invalid temperature"
                else:
                    if kelvin % 2 == 0:
                        return "Invalid temperature"
                    else:
                        return fahrenheit, kelvin
            else:
                if temperature % 2 == 0:
                    # Convert Celsius to Fahrenheit
                    fahrenheit = (temperature * (9 / 5)) + 32
                    if fahrenheit < -459.67:
                        # Invalid temperature, below absolute zero
                        return "Invalid temperature"
                    else:
                        if fahrenheit % 2 == 0:
                            return fahrenheit, kelvin
                        else:
                            return fahrenheit, temperature
                else:
                    return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                if celsius % 2 == 0:
                    # Convert Celsius to Fahrenheit
                    fahrenheit = (celsius * (9 / 5)) + 32
                    if fahrenheit < -459.67:
                        # Invalid temperature, below absolute zero
                        return "Invalid temperature"
                    else:
                        if fahrenheit % 2 == 0:
                            return fahrenheit, celsius
                        else:
                            return fahrenheit, kelvin
                else:
                    return celsius, fahrenheit
    else:
        return "Invalid unit"

```

### Points for discussion (do not copy this into the collaborative doc):
- the fact that something works does not make it good code
- extracting modules and naming them makes the code more readable
- there are various bits in the code that do not make sense. Extracting them makes it easier to highlight (i.e. the %2 == 0 clauses) and question these.
- duplicate code does not always look like duplicate code. Thinking in modules will help identify them.


## Day 3: Documentation lesson


### Exercise: Think of good and bad examples
Write down your thoughts in the collaborative documents.
Respond with emojis :+1: :scream_cat: to your colleagues' answers.
- Think of projects of which you like the documentation. What do you like about them?
- Think of projects for which you don’t like the documentation. What don’t you like about them? Are you missing anything?

**NB: You can choose a mature library with lots of users for this exercise, but try to also think of less mature projects you had to collaborate on, or papers you had to reproduce.**

### Exercise: Writing good comments
Let's take a look at two example comments (comments in python start with `#`):
#### Comment A
```python
# Now we check if temperature is larger then -50:
if temperature > -50:
    print('do something')
```

#### Comment B
```python
# We regard temperatures below -50 degrees as measurement errors
if temperature > -50:
    print('do something')
```
 Which of these comments is best? Can you explain why?
 Write your answer in the collaborative document (before looking at others' answers)

### Exercise: Adding in-code documentation

 Update this code snippet so it is well-documented:

 ```python
 import pandas as pd

 def x(a, print_columns=False):
    b = pd.read_excel(a)
    column_headers = list(b.columns.values)
    if print_columns:
        print("\n".join(column_headers))
    return column_headers
 ```
 1. One person screen-shares, discuss and together converge on a final solution. (8 minutes)
 2. Share final solution in collaborative document.


 ### Exercise: Write a README file
 You are going to write a README file for an example project.

 #### The example project
 Here's [the example project](https://github.com/escience-academy/coderefinery-documentation-example-project).
 For this project we transformed the code snippets from the previous episode into a single script [analyse_spreadsheet.py](https://github.com/escience-academy/coderefinery-documentation-example-project/blob/main/analyse_spreadsheet.py)

 Let's take a look at [the script](https://github.com/escience-academy/coderefinery-documentation-example-project/blob/main/analyse_spreadsheet.py).
 You don't need to understand the script completely, all you need to know is:
 * The functions `mean_temperature` and `get_spreadsheet_columns` from previous episode are in there.
 * We added a `main` function that is called when you run the script
 (you could run this python script by calling `python analyse_spreadsheet.py` on the command line).
 It will prompt the user for a file name, print the columns in the spreadsheet, and print the mean
 temperature.

 That's all there is to this project! (You can ignore the other files in the repository, we'll get back to them in episode 4)

 #### The exercise (20 minutes)
 1. One person shares the screen and is the driver. The others are 'navigators' and tell the 'driver' what to do.
 1. Fork [the example project](https://github.com/escience-academy/coderefinery-documentation-example-project) to your own github namespace
 2. Add a file called `README.md` (you can use the github web interface or work locally (i.e. `git clone`, edit the file,  `git add`, `git commit`, `git push`))
 3. Add some content to your README file. Think about what you want the audience to know about your project!
    It does not matter whether the information is correct, it is more important that you have all the components that make up a good README file.
 4. Note that the README file is nicely rendered on the github repository page.

 NB: The `README.md` file is written in 'Markdown' a very popular lightweight markup language, all you need to know for now is this syntax:
 ```
 # A section title
 ## A subsection title
 Normal text

 A list with items
 - item1
 - item2
 ```

 (Optional): Use [https://hemingwayapp.com/](https://hemingwayapp.com/) to analyse your README file and make your writing bold and clear!


### Exercise: Github Pages (15 minutes)

- Deploy own website reusing a template:
    - Follow <https://pages.github.com/>
    - Select "Project site"
    - Select "Choose a theme" (for instance "Minimal")
    - Click "Select theme"
    - Adjust the README.md and commit
    - Browse your page on `http://username.github.io/repository` (adjust "username" and "repository")
- Make a change to the repository after the webpage has been deployed for the first time
- Verify that the change shows up on the website a minute or two later

 The documentation for GitHub Pages is very good so no need for us to duplicate
 screenshots: <https://pages.github.com/>

> #### Real-life examples
>
> - Research Software Hour
>   - Source: <https://raw.githubusercontent.com/ResearchSoftwareHour/researchsoftwarehour.github.io/main/content/about.md>
>   - Result: <https://researchsoftwarehour.github.io/about/>
> - This lesson
>   - Source: <https://raw.githubusercontent.com/coderefinery/documentation/gh-pages/_episodes/06-gh-pages.md>
>   - Result: this page

Paste a link to your github page in the collaborative document.


### Recap modular coding, documentation + collaborative Git + Github
* What questions do you still have?
* Whether there are any incremental improvements that can benefit your projects?
* What’s nice that we learnt but is overkill for your current work?

## Day 4 Introduction to Continuous Integration

### Exercise: Four functions to write tests for
Start by discussing how you would design tests for the following four functions, and then try to write the tests. Below are the Python versions of the code, but you can also work on the C++, R, Julia or Fortran versions of the code. They can be supplied by one the helpers.
# 1
```python=
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
# 2
```python=
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)
```
# 3
```python=
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count
```
# 4
```python=
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1
```

### Exercise: Full-cycle collaborative workflow
This is an expanded version of the automated testing demonstration. The exercise is performed in a collaborative circle within the exercise group (breakout room).

The exercise takes 30-40 minutes.

In this exercise, everybody will:

A. Create a repository on GitHub/GitLab (everybody should use a different repository name for their repository)
B. Commit code to the repository and set up tests with GitHub Actions/ GitLab CI
C. Everybody will find a bug in their repository and open an issue in their repository
D. Then each one will clone the repo of one of their exercise partners, fix the bug, and open a pull request (GitHub)/ merge request (GitLab)
E. Everybody then merges their co-worker’s change

![](https://i.imgur.com/UR6Qaue.png)
Overview of this exercise. Below we detail the steps.

#### Step 1: Create a new repository on GitHub/GitLab

- Select a different repository name than your colleagues (otherwise forking the same name will be strange)
- Before you create the repository, select “Initialize this repository with a README” (otherwise you try to clone an empty repo).
- Share the repository URL with your exercise group via shared document or chat

#### Step 2: Clone your own repository, add code, commit, and push

Clone the repository.

Add a file `example.py` containing:

```python=
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    return a + b  # <--- fix this in step 8


# uncomment the following test in step 5
#def test_subtract():
#    assert subtract(2, 3) == -1

```
Test `example.py` with `pytest`.

Then stage the file (`git add <filename>`), commit (`git commit -m "some commit message"`),
and push the changes (`git push origin main`).


#### Step 3: Enable automated testing

In this step we will enable GitHub Actions.
- Select "Actions" from your GitHub repository page. You get to a page "Get started with GitHub Actions".
- Select the button for "Set up this workflow" under Python Application.

![](https://i.imgur.com/7QOplAg.png)
Select “Python application” as the starter workflow.

GitHub creates the following file for you in the subfolder `.github/workflows`:


   ```yaml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
   ```

Replace `pytest` by `pytest example.py`:
```yaml
   - name: Test with pytest
     run: |
       pytest example.py
```
![](https://i.imgur.com/1TFZPRe.png)


Commit the change by pressing the "Start Commit" button.

#### Step 4: Verify that tests have been automatically run

Observe in the repository how the test succeeds. While the test is executing, the repository has a yellow marker.
This is replaced with a green check mark, once the test succeeds.

![](https://i.imgur.com/b8dI8XH.png)

Green check means passed.

Also browse the "Actions" tab and look at the steps there and their output.

#### Step 5: Add a test which reveals a problem

After you committed the workflow file, your GitHub/GitLab repository will be ahead of your local cloned repository. Update your local cloned repository:

```
$ git pull origin main
```
or
```
$ git pull origin master
```
Next uncomment the code in `example.py` under “step 5”, commit, and push. Verify that the test suite now fails on the “Actions” tab (GitHub) or the “CI/CD->Pipelines” tab (GitLab).


#### Step 6: Open and issue on GitHub/GitLab
Open a new issue in your repository about the broken test (click the “Issues” button on GitHub or GitLab and write a title for the issue). The plan is that your colleague will fix the issue through a pull/merge request

#### Step 7: Fork and clone the repository of your colleague

Fork the repository using the GitHub/GitLab web interface.

Make sure you clone the fork after you have forked it. Do not clone your colleague’s repository directly.

```
$ $ git clone https://gitlab.com/your-username/the-repository.git
```

#### Step 8: Fix the broken test

After you have fixed the code, commit the following commit message `"restore function subtract; fixes #1"` (assuming that you try to fix issue number 1).

Then push to your fork.

#### Step 9: Open a pull request (GitHub)/ merge request (GitLab)

Then before accepting the pull request/ merge request from your colleague, observe how GitHub Actions/ Gitlab CI automatically tested the code.

If you forgot to reference the issue number in the commit message, you can still add it to the pull request/ merge request: `my pull/merge request title, closes #NUMBEROFTHEISSUE`

#### Step 10

Observe how accepting the pull request/ merge request automatically closes the issue (provided the commit message or the pull request/ merge request contained the correct issue number).

Discuss whether this is a useful feature. And if it is, why do you think is it useful?



## Day 4: Testing lesson


### Exercise : Discussion
Why do you write tests/ Why do you not write tests? Write reasons into the collabroative document.

### Excercise: Testing as part of the CI (15min)

Add the following to your github actions workflow file from yesterday.

```
    - name: Test with pytest
      run: |
        pytest example.py
```


Add these functions to your ``example.py``:
```python=
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    return a + b  # <--- fix this


# uncomment the following test
#def test_subtract():
#    assert subtract(2, 3) == -1
```

See what the CI does now and then uncomment the ``test_substract`` test.See what the CI does now, Afterwards fix the ``subtract`` function.


### Exercise : Test design

Pick one function from the following functions/classes. Write tests for it. Also test the error condition:
```python
#1
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)


# 3
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count


# 4
def check_reactor_temperature(temperature_celsius):
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status


# 5
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1

```