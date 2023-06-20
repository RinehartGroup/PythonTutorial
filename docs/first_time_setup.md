# The Rinehart Group Development Environment

This document will walk you through setting up your development environment and creating a repository for your scratch work.

The tutorial notebooks in `PythonTutorial` can be copied into your scratch repository or forked into your own repository (recommended). If you are here to use the tutorial notebooks, use this document to set up your development environment first and then follow the instructions in the [How to Fork this Repository](how_to_fork_this_repository.md) document.

## Git and GitHub

Git is a [version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) system that allows you to track changes to your code over time. GitHub is a website that hosts Git repositories. We will be using Git and GitHub to manage our code and collaborate with each other.

1. **Make a GitHub account** at [github.com](https://github.com/).

2. **Download and install [Git](https://git-scm.com/downloads).**

    a. When installing Git, select all of the default options.

    b. Check these user settings from the command line:

    ```commandline
    git config --global user.name
    git config --global user.email
    ```

    If these are not set, set them with the following commands:

    ```commandline
    git config --global user.name "Your Name"
    git config --global user.email "your_email@xzy.com"
    ```

    Where the name and email should be the ones associated with your GitHub account.

3. **Make sure you're a part of the [RinehartGroup organization](https://github.com/RinehartGroup) on GitHub.** If you're not, ask someone to add you.

<br>

## Python

You can check to see if you already have Python installed with the following command line or terminal command:

```commandline
python --version
```

Without the `--version` flag, this command will open the Python interpreter. You can exit the interpreter by typing `exit()`.

Even if you already have a version of Python installed, when working on a group project you may need to download a specific version of Python. Newer versions of Python (within the same major version number) _should_ be compatible with older versions, but this is not always the case. It's best to be safe on collaborative projects and use a specific version of Python.

>A note on versioning: Python uses semantic versioning ("SemVer"). The version number is broken up into three parts: `major.minor.patch`. The `major` version number is incremented when there are breaking changes to the language (i.e. version 3 is not compatible with version 2). The `minor` version number is incremented when new features are added. The `patch` version number is incremented when there are bug fixes.

<br>


4. **Download and install [Python 3.10](https://www.python.org/downloads/release/python-31010/)**

    a. Windows: use the "Windows installer (64-bit)" link.

    b. MacOS: use the "macOS 64-bit universal2 installer" link or use [Homebrew](https://brew.sh/) to install Python 3.10.

    c. Recommend installing at the user level, not system level (i.e. you shouldn't need admin privileges to install it).

    d. Select the option to add Python to your PATH.

> You can always manually add things to the PATH variable.

> [What is the path variable, and how do you set it?](https://realpython.com/add-python-to-path/) In short, it's a list of directories that your computer searches through when you type a command into the command line. For example, when you type `python` into the command line, your computer will search through the directories in the PATH variable to find the `python` executable. If it finds it, it will run it. If it doesn't find it, it will throw an error.

> You may have multiple versions of `python` installed. If you don't select a specific version to run when you type `python`, your computer will run the first one it finds in the PATH variable.

<br>

5. Try **running the version of `python` you just installed.**

    a. Windows:

    ```commandline
    python
    ```
    If this launches the windows store, you need to [turn off "App execution aliases" for Python.](https://stackoverflow.com/questions/58754860/cmd-opens-windows-store-when-i-type-python)

    If it runs a version of `python` other than the one you just installed, it may be because you have multiple version of `python` installed and 3.10 is not the highest on the PATH variable. In that case, give the specific version of `python` to run. For example:
    
    ```commandline
    C:\Users\<username>\AppData\Local\Programs\Python\Python310\python.exe
    ```
    
    b. MacOS:

    ```terminal
    python3.10
    ```
<br>

## VS Code

VS Code is an IDE (Integrated Development Environment) that we will be using to write our code. It has a lot of useful features that make writing code easier, can be used for many different languages, and is free.

<br>

6. **Install [VS Code](https://code.visualstudio.com/)**

7. Familiarize yourself with the control panel on the left-hand side of VS Code. Go to the Extension tab and **install the following extensions** (some of these may auto-install when you install the others, just make sure that all of them end up being installed):

    a. Python

    b. Jupyter

    c. PowerShell

    d. Black Formatter

    e. Pylint

<br>

## Putting It All Together: Making a Scratch Repository

<br>

8. Go to the Rinehart Group GitHub page and **create a new repository** called `<yourname>Scratch`.

    a. Description: "Scratch repository for \<your name>"
    b. Select "Private" (only visible to others on the RinehartGroup org)

    c. Select "Add a README file" - a README file is always good practice.  Include your full name, position in group, and any other information so we can attribute things to you and make sure you know about it even             after you leave. (some ideas: ORCHID, Google Scholar profile, Twitter Handle, Linked In Profile, permanent email address).

    d. Select "Add .gitignore" and select "Python" from the dropdown menu

    e. Select "Add a license" and select "MIT License" from the dropdown menu

    f. Click "Create repository"

9. Go to the newly created repository and click the green "Code" button. **Copy the repository URL.**

10. **Clone the repository into VS Code.** Open a new window in VS Code. Open the command palette (Ctrl+Shift+P or Cmd+Shift+P) and type "Git: Clone" and select it. Paste the URL into the text box and hit enter. Select a location to save the repository and hit enter. If prompted, select "Open Repository".

    > The location you select will be the parent directory of the repository. This is where the local version of the repository will be saved. Git will then keep track of everything in that directory and all of its subdirectories.
    
11. **Create a virtual environment using Python 3.10** that you previously installed.

    > [Virtual environments](https://realpython.com/python-virtual-environments-a-primer/) are a way to isolate your Python environment from the rest of your computer. This is useful because different projects may require different versions of Python or different packages. Virtual environments allow you to have different versions of Python and different packages installed for different projects.

    a. Open a terminal in VS Code (Ctrl+Shift+` or Cmd+Shift+` or click "Terminal" in the top menu and then "New Terminal").

    b. **Use `venv` to create the virtual environment.** If Python 3.10 is your default version of Python, you can create a virtual environment with the following command:

    ```commandline
    python -m venv .scratch
    ```

    If Python 3.10 is not your default version of Python, you can create a virtual environment with the following command:

    ```commandline
    C:\Users\<username>\AppData\Local\Programs\Python\Python310\python.exe -m venv .scratch
    ```

    or 

    ```terminal
    python3.10 -m venv .scratch
    ```

    That command has 4 parts:
    - `python` is the command to run Python
    - `-m` tells Python to run a module
    - `venv` is the module that creates virtual environments
    - `.scratch` is the name of the virtual environment. You can name it whatever you want, but it's good practice to name it something that makes sense. In this case, we're creating a virtual environment for our scratch repository, so we're naming it `.scratch`. It's also good practice to name it with a leading period so that it's hidden from the file explorer.

    The virtual environment is stored in a folder called `.scratch` in the parent directory of the repository. This folder contains everything that is needed to run Python in the virtual environment. Within that folder is a folder called `Scripts` (Windows) or `bin` (MacOS) that contains the `python` executable. When you activate the virtual environment, it adds that folder to the PATH variable so that when you type `python` into the command line, it runs the `python` executable in the virtual environment.

    Also in `Scripts` is `Activate.ps1` -- the script that will activate the virtual environment.

    The folder `Lib` contains all of the packages that are installed in the virtual environment.

    c. Open the VS Code command palette (Ctrl+Shift+P or Cmd+Shift+P) and type "Python: Select Interpreter" and select it. **Select the virtual environment you just created as your default** (if you give it a moment it will likely find the virtual environment you just created and mark it with a star).

    d. **Activate the virtual environment.** You can do this manually in the terminal by typing (Windows):

    ```commandline
    .\.scratch\Scripts\Activate.ps1
    ```

    or (MacOS)

    ```terminal
    source .scratch/bin/activate
    ```

    Alternatively, since you've told VS Code where the default virtual environment is for this repository, you can restart the terminal in VS Code (Ctrl+Shift+` or Cmd+Shift+`) and VS Code will automatically activate the virtual environment.

    If you get an error relating to "execution of scripts is disabled on this system", you need to change your execution policy. You can do this by opening a PowerShell terminal as an administrator and typing:

    ```powershell
    Set-ExecutionPolicy RemoteSigned
    ```

    and then typing `Y` to confirm.

    e. **Ensure you're in the virtual environment.** The terminal should now have `(.scratch)` at the beginning of the line (or whatever you named your virtual environment).

<br>

12. **Install the packages you will need for this project.** In the terminal, type:

```commandline
pip install ipykernel git+https://github.com/RinehartGroup/MagnetoPy.git@v0.1.0
```

`pip` is a package manager for Python which allows you to install Python packages from the Python Package Index (PyPI). `pip` is installed with Python, so you should be able to run it from the command line. `pip` will install the packages you specify and any packages that those packages depend on.

The previous command installs two packages: `ipykernel` and `MagnetoPy`.
- `ipykernel` is a package that allows you to use Jupyter notebooks with virtual environments. It is required for using Jupyter notebooks in VS Code.
- `MagnetoPy` is a package on the RinehartGroup GitHub that contains classes and functions which assist in the parsing of .dat files and .rw.dat files, as well as some tools for plotting and analyzing the data. One advantage of `pip` over `conda` (another package manager) is that `pip` can install packages directly from GitHub. This is useful for installing packages that are not on PyPI (which will be the case for many of our work-in-progress packages). The `@v0.1.0` at the end of the URL tells `pip` to install version 0.1.0 of the package. If you don't specify a version, `pip` will install the latest version.

> Note: make sure you're in the virtual environment when you run `pip install`. If you're not, you'll be installing the packages globally, which is not what you want, and you'll run into a problem later.

<br>

13. **Run the sample code.** This package (`PythonTutorial`) contains an [`examples`](../examples/) folder which you can download and copy into your scratch repository. 
    
    a. Once the `examples` folder is in your scratch directory, open [example_of_raw.ipynb](../examples/example_of_raw.ipynb) in VS Code. This notebook demonstrates how to use `MagnetoPy` to look at voltage vs. position curves found in .rw.dat files.
    
    b. In the top right of the notebook will be a button that says "Select Kernel". Click it and select the virtual environment you just created. This will allow you to run the code in the notebook using the packages you just installed.
    
    > Here's an in-depth [introduction to Jupyter notebooks](https://realpython.com/jupyter-notebook-introduction/). Note that this intro (and most that you'll find online) assumes you're using Anaconda and/or JupyterLab. The process is a little different in VS Code, but the basic functionality is the same.

    c. Run each individual cell by pressing Shift+Enter. You can also run all of the cells at once by clicking the "Run All Cells" button in the top menu.

    > If you ran into an error running the first cell, you may not have installed the packages correctly; you likely added them to the global environment rather than your virtual one. If this is the case, you can fix it by deleting the `.scratch` folder and starting over from step 11.

<br>

14. **Sync the local and remote versions of your repositories** using VS Code's built-in Git functionality.

    a. **Find and click on the "Source Control" icon** on the left-hand side of VS Code.

    Git tracks the differences between files in a repository. When you make changes to a file, Git will show you the changes you've made and allow you to commit those changes. A commit is a snapshot of the repository at a given point in time. You can think of it as a save point. You can commit as often as you want, and you can go back to any commit at any time. This is useful if you make a change that breaks your code and you want to go back to a previous version.

    The default view of files in the source control tab lists all files in a list structure. This is not very useful for large repositories. You can change the view to a tree structure by clicking the "..." button in the top right of the source control tab and selecting "Group by Folder". There's also an icon in the top left of the source control tab that will toggle between the list and tree views.

    b. Some items you won't want to track with Git. When you created the repository on GitHub, you opted to add a '.gitignore' file. This file keeps track of things in your local repository that you don't want to track with Git. For example, you don't want to track the virtual environment you just created. You also don't want to track any files that are created when you run your code (e.g. .pyc files). You can add other files to the .gitignore file if you don't want to track them.

    **Right click on the .scratch folder (your virtual environment) and select "Add to .gitignore"**.

    c. **Stage your changes.** Staging is the process of telling Git which files you want to commit. You can stage individual files or entire folders. **Click the "+" button next to the examples folder** to stage everything in that folder.

    d. **Add a message to your commit and click the "commit" button.** If you don't add a message, a window will pop up asking you to add a message. The message should be a short description of the changes you made. For example, "Added examples folder" or "Fixed bug in example_of_raw.ipynb". Save and close that file to finish the commit.

    e. **Pull/Push your commit to GitHub.** Click the "..." button in the top right of the source control tab and select "Pull, Push", then "Sync". This will pull any changes that have been made to the repository on GitHub and push your changes to GitHub.

    Now your local version of the repository is up to date with the remote version on GitHub. You can go to the GitHub page for your repository and see that there is now an "examples" folder in the repository.

> WARNING: Because you're working with your own scratch repository, it's safe to make commits directly onto the main/master branch (the default branch). However, when you're working with a shared repository, you should never commit directly to the main/master branch. Instead, you should create a new branch for each feature you're working on. When you're done with the feature, you can merge the branch into the main/master branch. This is a more advanced topic, but it's important to know about. You can read more about it [here](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).

<br>

## Next Steps

You now have a working working Python development environment!! Use the scratch repository for... scratch work. Any packages that you install into the virtual environment will be available for any modules (.py files) or notebooks (.ipynb files) within the repository. For example, because you installed `MagnetoPy` into the virtual environment, you can import it into any module or notebook in the repository by typing `import magnetopy` at the top of the file (or `import magnetopy as mp` if you want to use the alias `mp` instead of `magnetopy`).
