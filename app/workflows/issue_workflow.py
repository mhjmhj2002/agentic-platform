# app/workflows/issue_workflow.py

from app.core.logger import logger

from app.agents.planning_agent import generate_plan

from app.project_context.context_builder import (
    build_project_context
)

from app.project_context.context_registry import (
    get_project_path
)


async def handle_issue_opened(event: dict):

    repository = event.get("repository")
    issue_title = event.get("issue_title")

    logger.info(
        f"Starting workflow for repo={repository}"
    )

    # =========================
    # VALIDATE REPOSITORY
    # =========================

    if not repository:
        logger.error("Repository missing in event payload")

        return {
            "status": "error",
            "reason": "repository missing"
        }

    # =========================
    # LOAD PROJECT PATH
    # =========================

    repo_path = get_project_path(repository)

    if not repo_path:
        logger.error(
            f"Repository not registered: {repository}"
        )

        return {
            "status": "error",
            "reason": f"repository not mapped: {repository}"
        }

    # =========================
    # BUILD CONTEXT
    # =========================

    context = build_project_context(
        repo_path=repo_path,
        repository=repository
    )

    logger.info(f"Project context: {context}")

    # =========================
    # GENERATE PLAN
    # =========================

    plan = await generate_plan(
        issue_title=issue_title,
        context=context
    )

    return {
        "status": "planning_completed",
        "repository": repository,
        "issue": issue_title,
        "context": context,
        "plan": plan
    }