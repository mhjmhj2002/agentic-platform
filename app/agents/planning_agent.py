# app/agents/planning_agent.py

from app.core.logger import logger


async def generate_plan(
        issue_title: str,
        context
):

    logger.info(
        "Generating plan with context awareness"
    )

    language = context.language
    framework = context.framework
    build_tool = context.build_tool

    return {
        "summary": {
            "language": language,
            "framework": framework,
            "build_tool": build_tool
        },
        "steps": [
            {
                "id": 1,
                "type": "controller",
                "description": (
                    f"Create endpoint for issue: "
                    f"{issue_title}"
                )
            },
            {
                "id": 2,
                "type": "service",
                "description": (
                    f"Implement business logic using "
                    f"{framework or language}"
                )
            },
            {
                "id": 3,
                "type": "repository",
                "description": (
                    f"Create persistence layer with "
                    f"{build_tool}"
                )
            }
        ]
    }