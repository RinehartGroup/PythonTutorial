# How to Fork this Repository

When you fork a repository, you create a copy of the original repository (upstream repository) but the forked repository (downstream repository) is not linked to the original repository. This means that you can make changes to the forked repository without affecting the original repository.

When this repository (`PythonTutorial`) is updated with additional tutorial notebooks, you can update your forked repository to include the new changes.

While you won't be doing this for `PythonTutorial`, forking is also a useful tool for working on shared projects. You can fork a repository, make changes to the forked repository, and then submit a pull request to the original repository to propose that your changes be merged into the original repository. Forks and branches are similar. [Here's an article discussing when to use which one.](https://www.pluralsight.com/blog/software-development/the-definitive-guide-to-forks-and-branches-in-git)

## Forking this Repository

1. **Click the Fork button at the top right of this page.** This will create a copy of this repository in your GitHub account.

2. **Go to the forked repository on your personal GitHub page.** You can do this by clicking on your profile picture in the top right corner of the page and selecting "Your repositories" from the dropdown menu. You should see a repository called `PythonTutorial` in the list.

3. **Copy the URL of the forked repository.** You can do this by clicking on the green "Code" button and copying the URL that appears in the dropdown menu.

4. Open a new window in VS Code and **clone the forked repository.** You can do this by opening the command palette (Ctrl+Shift+P) and typing "Git: Clone" into the search bar. Then paste the URL of the forked repository into the search bar and press Enter. Select a location on your computer to save the repository.

Remember to make a virtual environment and install dependencies. In this case all you'll need is

```powershell
> pip install ipykernel git+https://github.com/RinehartGroup/MagnetoPy.git@v0.1.0
```

## Working with the Forked Repository

Now that you have a copy of the repository on your computer, you can make changes to the repository without affecting the original repository.

When you make changes that you want to save (e.g. you complete a tutorial notebook), you can **commit** those changes to the forked repository. This means that you are saving the changes to your local copy of the repository. You can commit changes as often as you like.

When you want to share your changes with others, you can **push** those changes to the forked repository. This means that you are saving the changes to the forked repository on GitHub. You can push changes as often as you like. With the work in your `PythonTutorial` notebook, you'll probably be using **commit** and **push** together most of the time.

The GitHub webpage for your forked repository will give information on how many commits your forked repository is ahead or behind the original repository. When the original (upstream) repository is updated with new tutorial notebooks, you'll see that your forked repository is some number of commits behind "RinehartGroup:main". **Click the "Sync fork" menu and select the "Update branch" option to update your forked repository with the new changes.**

## Pull Requests

In this case, it's unlikely that you'll want to submit a pull request to the original repository. However, if you were working on a shared project, you might want to submit a pull request to propose that your changes be merged into the original repository.