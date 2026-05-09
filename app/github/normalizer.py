from app.core.logger import logger


def normalize_github_event(event: str, payload: dict):

    logger.info(f"Normalizing GitHub event: {event}")

    normalized = {
        "event": event,
        "action": payload.get("action"),
        "repository": payload.get("repository", {}).get("name"),
        "issue_number": payload.get("issue", {}).get("number"),
        "issue_title": payload.get("issue", {}).get("title")
    }

    return normalized