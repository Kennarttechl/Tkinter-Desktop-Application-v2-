# python_project
This is beginners projects that teach how to use git and github 


# ----------console commands-----------#
1. cd = change directory
2. ls = list
3. clear = clear terminal
4. pwd = print working directory
5. mkdir = make new directory
6. touch = use to create new file
7. cd .. = navigating back
8. cd ~ = navigating back home
9. mv = use to rename and move a file
10. rm = use to remove file or directory
11. cp = use to copy file into another dir


# ----------git commands--------------#
git config --global user.email "you@example.com"
git config --global user.name "Your Name"


# ------------git conflict-----------###
git pull

1. git config pull.rebase false = To merge the changes from the remote branch into your local branch, 

2. git config pull.rebase true = To rebase your local changes onto the remote branch,


# ------------------------------------------------------------- #
3. git pull --no-rebase = If you want to merge the changes from the remote branch into your local branch, run the following command::

4. git pull --rebase = If you want to rebase your local changes onto the remote branch, run the following command:

5. git pull --ff-only = If you want to only allow fast-forward merges, which will only merge the remote branch if it is a direct ancestor of your local branch


# -----------------------git branching or moving to new branch------------------------ #
1. git checkout -b tech = This create new branch
2. git checkout main = to switch back to the main branch
2. git push origin tech = after creating new branch push it to the gihub
3. git add e.g README.md
4. git commit -m "Moving to new branch"
5. git push origin tech
6. git merge tech = this merge the two branch (*main branch)
7. git commit -am "Fix merge conflicts"
8. Bonus, on your github (there will be pull to merge request) this merge the two branch
9. git fetch origin = this upadate your local repo with the latest changes from the remote repo
10. git checkout tech2
11. git checkout --force tech3



# -----------------------changes made long time branch------------------------ #
error: failed to push some refers to "https://github.com/"
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. integrate the remote changes
1. git stash = this command saves your local changes to a temporary area so that yu can apply them later, after you've pulled the changes from remote branch and merge them into your local branch
2. git pull origin tech
3. git stash apply = This command retrieve your changes from the stash and re-apply them to your working directory
4. git pull origin tech
5. git push origin --delete tech2 =this delete the new branch you create from remote
6. git push --set-upstream origin tech2 =this help interms of push and pull not necessary targeting or specifying the branch name before pushing
