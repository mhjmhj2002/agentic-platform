# app/workflows/workflow_router.py

from app.workflows.issue_workflow import handle_issue_opened


async def route_workflow(event: dict):

    event_type = event.get("event")
    action = event.get("action")

    # ISSUE OPENED
    if event_type == "issues" and action == "opened":
        return await handle_issue_opened(event)

    return {
        "status": "ignored",
        "reason": "event not supported"
    }