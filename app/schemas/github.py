# app/schemas/github.py

from pydantic import BaseModel


class GitHubIssue(BaseModel):
    number: int
    title: str


class GitHubRepository(BaseModel):
    name: str


class GitHubWebhookPayload(BaseModel):
    action: str | None = None
    repository: GitHubRepository | None = None
    issue: GitHubIssue | None = None