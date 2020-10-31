# Update Paradox Files

### Motivation
The modding restrictions force us to edit some game files.
These game files are edited by Paradox Development Studio.
Then our modifications of these files need to be updated to each Paradox file.

The *paradox* branch's goal is to help to update the edited Paradox files.
This file will show how to do.

### Add edited Paradox files to the paradox branch
When Paradox release a patch of CK3, DO NOT UPDATE YOUR GAME YET !

Check the edited files by the mod by going to [this link](https://github.com/ArkoG/MyMo/compare/paradox...main) and seeing the files list by cliking on area with red rectangle in the following image.
![List of edited files by the mod](images/edited_files.jpg)

Pay attention to added files (green + before their names).

If you recognize Vanilla files, commit and push them in the *paradox* branch. 

Go to the *main* branch and merge the *paradox* branch You will have conflicts, keep always the HEAD version (you can always solve brutally conflicts by overriding files with their version on the *main* branch).

*Example on GitHub Desktop*

The following images show you how to do it with [GitHub Desktop](https://desktop.github.com/).

Check you are on the *main* branch.
![Main branch on GitHub Desktop](images/main_branch.jpg)

Select *Merge into current branch...*
![Merge branch menu on GitHub Desktop](images/merge_branch.jpg)

Select *paradox* branch.
![Merge with branch branch on GitHub Desktop](images/merge_paradox_branch.jpg)

You will see conflict. To solve one by one, click on the editor at the right for a file.
![Merge with branch branch on GitHub Desktop](images/merge_conflict.jpg)

Search "==========" in the editor.
Remove the lines with "<<<<<< HEAD" and all lines between "==========" and ">>>>> paradox" included.
![Solve conflict in editor](images/solve_conflict.jpg)

Repeat the operation for each file. Commit the merge when there is no more conflicts.
![Commit merge on GitHub Desktop](images/commit_merge.jpg)

### Update the paradox files
When you have finished adding all edited paradox files (see previous section), you should now update your game.

To update the paradox files you can use a homemade Python script.
You need to install Python 3. You can do it by installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

When done, you can create a script file (.bat on Windows, .sh on Linux) with the following command to run the Python script.
```
"<path_to_python>\python" update_source.py "<path_to_steam>\Steam\steamapps\common\Crusader Kings III\game" "<path_to_github>\GitHub\MyMo\MyMo"
```

Example of a more complete .bat file:
```
@echo off
C:\Users\Nicolas\Miniconda2\python update_source.py "D:\Programmes\Steam\steamapps\common\Crusader Kings III\game" D:\Documents\GitHub\MyMo\MyMo
pause
```

The double quotes are used to manage arguments with spaces.

After running the script, if there is no error you will see the changes in your git application.

Commit and push the changes.

Go to the *main* branch and merge the *paradox* branch.
It is possible you have conflict. This time you cannot solve them by overriding them, you should fix them one by one with your text editor (or your git merge tool).
