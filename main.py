import requests
import base64
import re

# Replace 'YOUR_GITHUB_USERNAME' with your actual GitHub username
github_username = 'mirolaukka'

# Replace 'YOUR_GITHUB_ACCESS_TOKEN' with your actual GitHub access token
access_token = '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'


def get_recent_projects(username, access_token):
    url = f'https://api.github.com/users/{username}/repos?sort=created&direction=desc&type=public'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to fetch projects: {response.status_code} - {response.json()}")
        return []


def generate_recent_projects_section(projects):
    content = ""

    excluded_repo = 'mirolaukka'
    listed_projects = 0

    for project in projects:
        if project['name'] != excluded_repo:
            content += f"- [{project['name']}]({project['html_url']}) - {project['description']}\n"
            listed_projects += 1

        if listed_projects == 5:
            break

    content += "\n\nThese are just a few of my recent projects. For a complete list, please check out my [GitHub repositories](https://github.com/mirolaukka?tab=repositories).\n\n"
    #   print(content)
    return content


def update_readme_in_repo(username, repo, access_token, content):
    url = f'https://api.github.com/repos/{username}/{repo}/contents/README.md'
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_data = response.json()
        sha = file_data['sha']

        # Find and replace the "Recent Projects" section in the existing content
        existing_content = base64.b64decode(file_data['content']).decode()

        pattern = r"(?s)## 🚀 Recent Projects.*?## 🌱 Currently Exploring"
        updated_content = re.sub(
            pattern, f"## 🚀 Recent Projects\n\n{content}\n\n## 🌱 Currently Exploring", existing_content)

        # Encode the updated content in Base64 and send it to update the file
        encoded_content = base64.b64encode(updated_content.encode()).decode()
        data = {
            'message': 'Update README.md with recent projects',
            'content': encoded_content,
            'sha': sha
        }
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200:
            print("README.md updated successfully.")
        else:
            print(
                f"Failed to update README.md: {response.status_code} - {response.json()}")
    else:
        print(
            f"Failed to fetch README.md details: {response.status_code} - {response.json()}")


if __name__ == "__main__":
    recent_projects = get_recent_projects(github_username, access_token)
    if recent_projects:
        readme_content = generate_recent_projects_section(
            recent_projects)  # Generate "Recent Projects" section
        repo_name = 'mirolaukka'  # Replace with your repository name
        update_readme_in_repo(github_username, repo_name,
                              access_token, readme_content)
    else:
        print("No projects found or error occurred.")
