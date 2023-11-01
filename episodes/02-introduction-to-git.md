# Introduction to git
#### Timing
3:12 hours (this is according to the carpentries, but it is not accurate, see below)

### Instructor Notes
Lesson material: https://swcarpentry.github.io/git-novice/
Slides (optional, but nice and helpful to show): https://nlesc-slides.github.io/2023-06-19-ds-cr/git/. This is our suggestion for when to use the slides:
- Slides 0 - 4: accompanying episode 1 (Automated Version Control)
- Slides 5 - 9: right after episode 4 (Tracking Changes)

NB: Optional day before the course starts for participants who don’t know the git basics yet.

Teach what you think is most useful. See how far you get, usually we get to episode 7 in one morning.
To give participants a good understanding of the git basics, we suggest to:
* Ignore the temptation to answer advanced questions. (You can of course do this individually during exercises).
* Explain what a command line is, why it is useful, and why we use it in this workshop. Participants are often new to the command line and don't get why we not use a git gui.
* Only focus on the bare essentials for setting up git ([episode 2](https://swcarpentry.github.io/git-novice/02-setup/index.html)
* Do episode 5 (exploring history) as a demo and do not go into the details. The aim is to demonstrate to participants the **possiblity** to go back and forth through the git log, which is enough for an introduction to git. In practice you only use this occasionally.
* Focus on the main concept of ignoring files with a `.gitignore` file, instead of fully learning the syntax. ([episode 6](https://swcarpentry.github.io/git-novice/06-ignore/index.html)
* Take a dedicated moment right before [episode 7](https://swcarpentry.github.io/git-novice/07-github/index.html) to check succesful completion of particpants' SSH setup and help out people who did not succeed yet. You will need 15-30 minutes for this.
* Make use of `git switch` and `git restore` instead of the confusing `git checkout`. This is probably much clearer for participants. We haven't tried this yet and it is not in the training material, so you have to do some pioneering.

You can use [these slides to introduce git](../files/02-introduction-to-git-slides.pptx)
You can skip [the lesson on collaborating](https://swcarpentry.github.io/git-novice/08-collab/index.html),
since we cover that extensively in the rest of the course. 
