# GitHub Profile README Updater

This Python script allows you to dynamically update your GitHub profile README's "Recent Projects" list by fetching your latest public repositories from GitHub and inserting them into your README file.

## Features

- Automatically fetches your latest public repositories from GitHub.
- Replaces the `[[PROJECTS]]` placeholder in your README file with the list of recent projects.
- Customizable to show a specific number of recent projects.

## Getting Started

These instructions will help you set up and use the script on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- A GitHub account with a profile README where you want to display recent projects.
- A GitHub Personal Access Token with the `repo` scope. You can create one [here](https://github.com/settings/tokens).

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/mirolaukka/readme-projects-updater.git
   ```

2. Navigate to the project directory:

   ```
   cd readme-projects-updater
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

### Usage

1. Create a `.env` file in the project directory and add the following:

   ```
   GITHUB_USERNAME=yourgithubusername
   ACCESS_TOKEN=youraccesstoken
   ```

   Replace `yourgithubusername` with your GitHub username and `youraccesstoken` with your GitHub Personal Access Token.

2. Open the `template_readme.md` file in the project directory. Customize this file to update other portions of your profile README as needed.

3. Run the script:

   ```
   python main.py
   ```

   The script will fetch your recent projects, read the `template_readme.md` file, and push the `template_readme.md` file with the recent project list.

4. Check your GitHub profile README, and you should see the updated "Recent Projects" section along with your customized content from `template_readme.md`.

Customization
-------------

You can customize the number of recent projects displayed by editing the `generate_recent_projects_section` function in the `main.py` script. Adjust the `listed_projects` variable to control how many projects are listed.

```python
# Limit the number of displayed projects to 5
if listed_projects == 5:
    break
```

Automate updating
------------
1. Create a Batch Script
    First create a batch script (`.bat`) that runs your python script. Open a text editor, paste the following code, and save it as `run_github_updater.bat` (or any name you prefer):
    ```batch
    @echo off
    cd path\to\readme-projects-updater
    python main.py
    ```

    Replace `path\to\readme-projects-updater` with the actual path to your project directory where the `main.py` script is located.

2. Press Win+R and type `shell:startup`

3. Copy and Paste the `.bat` file you created here.

4. Now, every time you open your computer, the GitHub Profile README Updater script will be automatically executed, ensuring that your profile README is always up to date with your recent projects.


## Disclaimer

Before using this script to update your GitHub profile README, it is highly recommended that you review and understand the code thoroughly. The script interacts with your GitHub account and may modify your profile README, which is publicly visible to others.

**Please take the following precautions:**

1. Review the Code: Open the `main.py` script and understand how it works. Ensure that it meets your requirements and does not perform any actions you are not comfortable with.

2. Protect Sensitive Information: Ensure that sensitive information, such as your GitHub Personal Access Token, is handled securely. Avoid sharing or exposing this information unintentionally.

3. Customize the Template: The script uses a `template_readme.md` file as a template for your profile README. Customize this file to include any additional information or sections you want in your profile README.

4. Backup Your README: Before running the script, make a backup of your existing profile README if you have one. This can be helpful in case you need to revert to the previous state.

5. Test in a Safe Environment: If possible, test the script in a safe environment or on a test GitHub account before using it on your main profile.

By using this script, you acknowledge and accept the responsibility for any changes it makes to your GitHub profile README. The maintainers of this project are not responsible for any unintended consequences or issues that may arise from its use.

If you have any concerns or questions, please reach out for assistance or clarification before proceeding.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
