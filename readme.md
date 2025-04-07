Scenario 1: If files are added by mistake and the first commit has not been made, how can we unstage them?

Use the command: git rm --cached index.html

Scenario 2: If files are added by mistake after the initial commit (but the file index.html was not committed in the initial commit), how can we unstage it?

Use the command: git restore --staged index.html

Scenario 3: If files have been added and committed, how can we unstage them?

First, check the log with: git log.

To undo the last commit and keep the changes staged, use:
git reset --soft HEAD~1

Now, the files are staged but not committed (one commit back).

You can unstage the files by either:

git rm --cached index.html

or git restore --staged index.html

___________________________________
amend
