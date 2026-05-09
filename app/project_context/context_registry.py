# app/project_context/context_registry.py

PROJECTS = {
    "agentic-ms-user": "/home/mhj/git/agentic-ms-user",
    "agentic-ms-order": "/home/mhj/git/agentic-ms-order"
}


def get_project_path(repository: str):

    return PROJECTS.get(repository)