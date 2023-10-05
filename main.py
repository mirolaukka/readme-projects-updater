import requests
import base64
import re
import logging
from dotenv import dotenv_values
from datetime import datetime

# Load environment variables from a .env file
config = dotenv_values('.env')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


current_time = datetime.now()

time = current_time.strftime('%B %d, %Y, %H:%M')


def get_recent_projects(username, access_token):
    try:
        url = f"https://api.github.com/users/{username}/repos?sort=updated&direction=desc&type=public"
        headers = {"Authorization": f"token {access_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except Exception as e:
        logger.error(f"Failed to fetch projects: {str(e)}")
        return []


def generate_recent_projects_section(projects):
    content = ""

    excluded_repo = github_username
    listed_projects = 0

    for project in projects:
        if project["name"] != excluded_repo and project['description'] is not None:
            content += f"- [{project['name']}]({project['html_url']}) - {project['description']}\n"
            listed_projects += 1

        if listed_projects == 5:
            break

    return content


def update_readme_content(readme_content, projects_content):
    # Replace the [[PROJECTS]] placeholder with the recent projects content
    updated_content = re.sub(
        r'\[\[PROJECTS\]\]', projects_content, readme_content)

    updated_content += f"\n\n ------\n_Last updated: {time} by [Readme Project Updater](https://github.com/mirolaukka/readme-projects-updater)_"

    return updated_content


def update_readme_in_repo(username, repo, access_token, content):
    try:
        url = f"https://api.github.com/repos/{username}/{repo}/contents/README.md"
        headers = {
            "Authorization": f"token {access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        file_data = response.json()
        sha = file_data["sha"]

        # Encode the updated content in Base64 and send it to update the file
        encoded_content = base64.b64encode(content.encode()).decode()
        data = {
            "message": "Update README.md with recent projects",
            "content": encoded_content,
            "sha": sha,
        }
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        logger.info("README.md updated successfully.")
    except Exception as e:
        logger.error(f"Failed to update README.md: {str(e)}")


if __name__ == "__main__":
    github_username = config['GITHUB_USERNAME']
    access_token = config['ACCESS_TOKEN']

    recent_projects = get_recent_projects(github_username, access_token)
    if recent_projects:
        with open('template_readme.md', 'r', encoding='utf-8') as readme_file:
            readme_content = readme_file.read()
        projects_content = generate_recent_projects_section(
            recent_projects)  # Generate "Recent Projects" section
        updated_readme_content = update_readme_content(
            readme_content, projects_content)
        repo_name = github_username  # Replace with your repository name
        update_readme_in_repo(github_username, repo_name,
                              access_token, updated_readme_content)
    else:
        logger.info("No projects found or error occurred.")
