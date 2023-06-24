# Python Environment Management: pyenv and virtual environments

## Why is Python Version and Environment Management Important?

As our Python projects continue to grow and diversify, we will run into the need for testing with different versions of Python and/or packages to run successfully. Depending on the importance of the code and how widely we want to make it available, we will want to make it as compatible as possible; however, this is not necessary for everything -- as long as we know which versions it works with we can still run the code. Also, different projects might need different versions of Python and packages, which can conflict if installed globally.

That's why we need to manage Python versions and isolate our project environments.

## Using pyenv for Python Version Management

[pyenv](https://github.com/pyenv/pyenv) is a tool that lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

Follow the instructions on the [pyenv-installer](https://github.com/pyenv/pyenv-installer) page (for Mac and Linux users), the [pyenv-win](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md) page (for Windows users), or see below for detailed instructions.

Once pyenv is installed, you may need to update it to get it to recognize newer versions of python:

<pre>
   pyenv update
</pre>

To check the versions available for use with pyenv:

<pre>
  pyenv install --list
</pre>

<details>
<summary>Extended Installation Instructions for pyenv</summary>

<details>
<summary style="margin-left: 20px;">For macOS users:</summary>

If you're using [Homebrew](https://brew.sh/), you can install pyenv very easily:

<pre>
brew update
brew install pyenv
</pre>

After installing, add pyenv to bash so the command line knows where to find installed Python versions:

<pre>
echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$(pyenv init -)"; fi' >> ~/.bash_profile
</pre>

Then restart your shell:

<pre>
exec "$SHELL"
</pre>

</details>

<details>
<summary style="margin-left: 20px;">For Ubuntu users:</summary>

Firstly, update the package lists for upgrades for packages that need upgrading, as well as new packages that have just come to the repositories:

<pre>
sudo apt-get update
</pre>

Install prerequisites:

<pre>
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
</pre>

Install pyenv:

<pre>
curl https://pyenv.run | bash
</pre>

After installing, add [pyenv] to bash so the command line knows where to find installed [python] versions:

<pre>
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
</pre>

Then restart your shell:

<pre>
exec "$SHELL"
</pre>

</details>

<details>
<summary style="margin-left: 20px;">For Windows users:</summary>

For Windows, there is a fork of pyenv named pyenv-win. It can be installed using [pip]:

<pre>
pip install pyenv-win --target C:/Users/[INSERT_YOUR_USERNAME_HERE]/.pyenv
</pre>

Note: you may change the installation directory but is usually your HOME directory path.
   
# Adding pyenv-win to PATH on Windows

`pyenv-win` is a Python version manager for Windows. To make it work properly, we need to add a few of its directories to the system PATH.

<details>
<summary>Directories to Add</summary>

1. `pyenv-win\bin`: This directory contains the `pyenv` executable files.
2. `pyenv-win\shims`: This directory contains 'shims' for all Python versions that `pyenv` manages. These shims redirect commands to the appropriate Python version based on your `pyenv` settings.

So, the directories to add to the PATH are:

- `$HOME/.pyenv/pyenv-win/bin`
- `$HOME/.pyenv/pyenv-win/shims`

**Note:** `$HOME` is a placeholder for your actual home directory path.

</details>
</details>
</details>

<details>
<summary>Adding to PATH</summary>

There are two methods to add these directories to PATH:

**Method 1: PowerShell**

Please run the following commands in PowerShell:

`[Environment]::SetEnvironmentVariable('PYENV_HOME', "$HOME/.pyenv/pyenv-win", 'User')
[Environment]::SetEnvironmentVariable('PATH', "$HOME/.pyenv/pyenv-win/bin;$HOME/.pyenv/pyenv-win/shims;" + [Environment]::GetEnvironmentVariable('PATH', 'User'), 'User')`

You should replace `$HOME` with your actual home directory path if it's not automatically recognized. Remember to open a new PowerShell session for the changes to take effect.

**Method 2: Windows GUI Environment**

Please follow these steps:

1. Press `Win + X` and choose 'System'.
2. Click on 'Advanced system settings'.
3. Click on 'Environment Variables'.
4. In the 'User variables' section, click on 'New'.
5. Add `PYENV_HOME` as the variable name and `$HOME/.pyenv/pyenv-win` as the variable value.
6. In the 'User variables' section, find the variable named 'Path' and click 'Edit'.
7. Click 'New', then add these two paths one by one:
   - `$HOME/.pyenv/pyenv-win/bin`
   - `$HOME/.pyenv/pyenv-win/shims`
8. Click 'OK' on each window to save the changes.

Again, you should replace `$HOME` with your actual home directory path.

After you have finished adding the directories to the PATH, you may need to restart your computer for the changes to take effect in all contexts.

</details>

Here's a simple workflow using pyenv:

1. **Install pyenv**:

   - Follow the instructions on the [pyenv-installer](https://github.com/pyenv/pyenv-installer) page.

2. **Install a Python version**:

   - List all available Python versions with: `pyenv install --list`
   - Install a specific version, e.g., Python 3.8.10: `pyenv install 3.8.10`

3. **Set the Python version**:
   - For your global environment: `pyenv global 3.8.10`
   - For a particular project, navigate to the project's directory, then: `pyenv local 3.8.10`

You can verify your Python version with: `python --version`.

## Using Virtual Environments for Isolating Project Environments

Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally.

Here's how to set up a virtual environment:

1. **Create a virtual environment**:

   - Navigate to your project directory.
   - Create a new virtual environment inside your project directory: `python -m venv env`

2. **Activate the virtual environment**:
   - On Windows: `env\Scripts\activate`
   - On Unix or MacOS: `source env/bin/activate`

You should see `(env)` at the start of your terminal line indicating you are in a virtual environment named "env".

## Managing Python Packages

Maintaining a list of all packages (with their respective versions) used in your project is important for reproducibility and consistency across different setups.

1. **Install packages**:

   - Use [pip] to install packages, for example: `pip install numpy`

2. **Freeze dependencies**:
   - After you've installed all packages needed for your project, you can create a `requirements.txt` file which lists these packages and their versions: `pip freeze > requirements.txt`

This `requirements.txt` file can be committed and pushed to the GitHub repository.

To recreate the same environment with these exact packages, someone can use: `pip install -r requirements.txt` in their own virtual environment.

With this workflow, we can maintain consistency and reproducibility across different computers and instruments as well as between generations of group members and those outside the group who would like to use code we develop!

<details>

<summary> Appendix A: Standard Operating Procedure (SOP) for Poetry with pyenv-win </summary>

## Setting up a new project with Poetry

1. Open a new PowerShell terminal.

2. Set your Python version for the new project using pyenv-win. Replace `3.x.x` with your desired version.

   ```
   pyenv local 3.x.x
   ```

3. Create a new project directory and navigate into it (do not make a directory if you already have one)

   ```
   mkdir [yourproject]
   cd [yourproject]
   ```

4. Initialize a new Poetry project:

```
poetry new .
```

Using Poetry's shell: Poetry has a shell command that spawns a shell within the virtual environment. If you're using pyenv with Poetry, you might need to prefix this command with `pyenv exec` to ensure the correct Python version is used:

```
pyenv exec poetry
```

5. Open the project in VS Code:

```
code .
```

## Adding and updating dependencies

1. To add a new dependency to your project, use the `poetry add` command. Replace `package-name` with the name of the package:

```
poetry add [package-name]
```

2. To add a package as a development-only dependency, use the `-D` flag:

```
poetry add -D [package-name]
```

3. To update a package, use the `poetry update` command. Replace `package-name` with the name of the package:

```
poetry update [package-name]
```

 ## How to Continue Working with a Poetry Project in VS Code

When you want to continue working with a Poetry project in Visual Studio Code, follow these steps:

1. **Open the Project in VS Code**: 
    Open Visual Studio Code, then select `File -> Open Workspace...` from the menu. Navigate to your project directory and select the `.code-workspace` file. This will open your project workspace.

2. **Open the Integrated Terminal**:
    Once your project is open, open the integrated terminal by selecting `Terminal -> New Terminal` from the menu.

3. **Activate the Virtual Environment**:
    Poetry manages the virtual environment for your project, so you don't need to manually activate it. When you use a command like `poetry run python`, Poetry will automatically use the virtual environment.

    If you want to work within the virtual environment, use the command `poetry shell`. This will open a new shell session with the virtual environment activated.

    If you need to know the path to the virtual environment, you can use the command `poetry env info --path`.

4. **Install Additional Dependencies**:
    To install additional dependencies, use the command `poetry add package-name`, replacing `package-name` with the name of the package you want to install. This will add the package to your `pyproject.toml` file and install it in the virtual environment.

5. **Run Your Python Scripts**:
    You can run your Python scripts with the command `poetry run python script.py`, replacing `script.py` with the name of your script. This will run the script using the Python interpreter in the virtual environment, with access to all the dependencies you've installed.

Remember to save your work often, and commit changes so our code stays current.
   
## Testing your project

1. Before running your tests, ensure all dependencies are installed:

poetry install


2. Run your tests (for example, if you're using pytest):

```shell
poetry run pytest
```

## Building and publishing your project

1. To build your project, run:

```shell
poetry build
```

2. Before publishing, make sure you have an account on PyPI.

3. Then, publish your project:

```shell
poetry publish
```

## Using GitHub for version control

1. Initialize a new Git repository in your project directory:

```shell
git init
```

2. Add all files to the repository:

```shell
git add .
```

3. Commit your changes:

```shell
git commit -m "Initial commit"
```

4. Create a new repository on GitHub. Do not initialize it with a README, .gitignore, or License.

5. Link your local repository to the GitHub repository. Replace `username` and `repository-name` with your GitHub username and repository name:

```shell
git remote add origin https://github.com/username/repository-name.git
```

6. Push your changes to GitHub:

```shell
git push -u origin master
```

Remember, this is a very basic SOP. There are many other commands and features available in Poetry, pyenv, and Git.

</details>

<details>

<summary>  Appendix B: Best Practices for Package Version Maintenance </summary>

## 1. Explicitly specify versions

Always specify the version of each package. This ensures that your project will run consistently across different environments.

For example:

```plaintext
numpy==1.21.0     # This will allow for the installation of only version 1.21.0 of numpy
numpy>=1.21.0     # This will allow for the installation of version 1.21.0 or any later version
numpy<=1.21.0     # This will allow for the installation of version 1.21.0 or any earlier version
```

## 2. Keep the file updated

Whenever you add, update, or remove a dependency, make sure the package dependencies are updated. This is crucial to keep your project reproducible and allowing others to quickly understand, troubleshoot, and contribute to the project. Errors and incomplete analysis are only problematic in science if they are obscured by poorly documented methods and lack of data availability. If someone builds a new model by incorporating your data or is able to fix an error in your analysis it makes our data and methods that much stronger and more valuable.

## 3. Separate production and development dependencies

We will want to formalize our process further by having separate requirement files for production and development environments as more of our code is made available publicly. For example, a tool like [pytest] might not be needed in the production environment but is essential for development and testing.

## 4. Avoid unnecessary packages

Only include the packages that are directly imported in your project. There's no need to include packages that are dependencies of your dependencies; these will be installed automatically.

## 5. Comment your dependencies

If a dependency is not self-explanatory, or if it's important to use a specific version for some reason, add a comment explaining this. This helps others (and future you) understand why that dependency is in the file. We want to make things as simple and broadly useable as possible.

```
numpy==1.21.0  # Numpy is used for numerical computations
```

## 6. Use tools to manage your dependencies

Tools like pip-tools or [poetry] can help you manage your dependencies and make your `requirements.txt` file easier to maintain. See Appendix A for SOP on [poetry].

## 7. Pin all dependencies for production

In production, you should pin your dependencies to specific versions (i.e., using `==`) to avoid unexpected changes when a dependency is updated. This can help prevent a situation where your code suddenly stops working in production because of a dependency update.

## 8. Consider security and licensing implications

Be aware that including a package as a dependency means you're comfortable with its security and licensing implications. It's important to review and keep an eye on these aspects. We want to think hard before including anything that restricts our ability to provide free and open access to our data and analysis.

</details>
   
<details>
   <summary> Appendix C: Standard Operating Procedure (SOP) for Incorporating Pytest into Workflow </summary>

## Prerequisites

1. Ensure that `pyenv-win`, `Poetry`, `Git`, and `VS Code` are installed and properly configured on your Windows machine.

## Setting up the Project

1. Clone the project repository from GitHub:

    ```shell
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Navigate to the project directory:

    ```shell
    cd your-repo
    ```

3. Set the Python version for the project using `pyenv`. Replace `3.x.x` with your desired version:

    ```shell
    pyenv local 3.x.x
    ```

4. Initialize a new Poetry project:

    ```shell
    poetry init
    ```

## Installing Pytest and Dependencies

1. Add pytest as a development dependency:

    ```shell
    poetry add --dev pytest
    ```

2. Install the project dependencies:

    ```shell
    poetry install
    ```

## Writing and Running Tests

1. Create a directory named `tests` at the root of your project.

2. Write your test functions or classes using the pytest framework in the `tests` directory. For example:

    ```python
    # tests/test_example.py
    def test_addition():
        assert 1 + 1 == 2
    ```

3. Run your tests using the `pytest` command:

    ```shell
    poetry run pytest
    ```

## Continuous Integration (CI) with GitHub Actions

1. Create a file named `.github/workflows/ci.yml` in your project repository.

2. Add the following content to the `ci.yml` file:

    ```yaml
    name: Continuous Integration

    on: [push, pull_request]

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: 3.x

          - name: Install dependencies
            run: poetry install

          - name: Run tests
            run: poetry run pytest
    ```

3. Commit and push the `.github/workflows/ci.yml` file to the repository.

4. GitHub Actions will now automatically run the tests on every push and pull request.

## Code Coverage with pytest-cov

1. Install the `pytest-cov` plugin:

    ```shell
    poetry add --dev pytest-cov
    ```

2. Run your tests with code coverage:

    ```shell
    poetry run pytest --cov=myproject
    ```

## Integrating with VS Code

1. Open your project in VS Code:

    ```shell
    code .
    ```

2. Install the Python extension for VS Code (if not already installed).

3. Create a `.vscode` directory at the root of your project.

4. Inside the `.vscode` directory, create a file named `settings.json`.

5. Add the following content to the `settings.json` file to configure the test runner:

    ```json
    {
      "python.testing.pytestEnabled": true,
      "python.testing.pytestArgs": [
        "--color=yes",
        "-v",
        "--cov=myproject",
        "--cov-report=term-missing"
      ]
    }
    ```

## Finalizing the Workflow

1. Commit and push all the changes to your project repository.

2. Ensure that the CI workflow runs successfully on your repository in GitHub.
</details>
