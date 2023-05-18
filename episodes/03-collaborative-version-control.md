# Collaborative version control with git and Github
#### Timing
3:00 hours

### Questions
* How can we collaborate with others within one repository?
* How can we collaborate with people who we might not know yet?
* What is a fork?
* What is a pull request or merge request?
* What is code review?

### Instructor notes
The instructor can use [these slides](../content/03-collaborative-version-control-coderefinery.pptx) as a guidance.

Teaching is done as a pair of instructors.
Instructor A acts as the owner of the repository, instructor B as a collaborator (internal or external).

### Centralized workflow
First we show the centralized workflow all in the browser using Github:

* instructor A creates an issue (for example create ‘sum’ function)
* instructor B picks up the issue
* Instructor B creates a new branch (good to do this explicitly)
* Instructor B does some reviewable changes (a simple ‘sum’ function)
* Instructor B opens a new pull request.
* Instructor A reviews and approves the PR.
* Instructor B merges the pull request.
* Use Github repo’s insights -> network to visualize what just happened

#### Exercise: Working as a project collaborator (in groups):
- Log into Github and create a new repository
- Make the repository public
- clone it to your desktop
- add some code
- push the changes to the repository
- Add one person as a collaborator (settings -> Manage Access). Make sure everyone in the group has a collaborator.
- Clone that repo
- make changes on a new branch
- push the changes
- submit a Pull Request
- wait for approval
- At the same time review a collaborators Pull Request
- (Optionally) Learn about [protecting branches](https://docs.github.com/en/github/administering-a-repository/about-protected-branches) and try it out.

### Distributed workflow
Second we show distributed workflow. All in the browser using Github:
* Instructor A removes instructor B (Sven & Jens will love it if you play out a funny reason why instructor B needs to be kicked out)
* Instructor B now submits an issue
* Instructor A responds to issue asking instructor B to pick it up
* Instructor B forks repo, does some changes, and submits PR
* Instructor A reviews the changes
* Instructor B implements the changes
* Instructor A merges the pull request
* Use Github repo’s insights -> network to visualize what just happened

#### Exercise: Working as an external contributor (in breakout rooms):
- Remove your group member(s) as collaborators from your repository
- Fork another group members repo (Repository page, top right corner)
- Create an issue on the original repository
- Clone your forked repo to your computer
- Make some changes, use a somewhat real-world example so it makes sense to review it (but don't overdo it).
- Push it to your fork
- make a pull request from your fork to the main repository mentioning the issue
- Consider turning your Pull Request into a draft Pull Request.
- let your code be reviewed by tagging the repo owner using (@Username)
- At the same time review Pull Request using comments on individual lines. Try to act as if it was a real peer review as much as possible.
- Accept or reject the Pull Request
- (Optionally) learn about [merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts) and try it out in your collaboration.

### Key Points
* Git and Github are superpowerful, not just for version control, but as tools for collaborative development
* Do code reviews and be constructive in them!
* Use centralized flow for internal collaborations
* Use distributed flow for external collaborations
