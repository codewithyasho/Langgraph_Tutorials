from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# defining the schema for the file to be created or modified
class File_schema(BaseModel):
    path: str = Field(
        description="The path to the file to be created or modified")

    purpose: str = Field(
        description="The purpose of the file, e.g. 'main application logic', 'data processing module', 'styling' etc.")


# defining the schema for plans for building the app
class Plan_schema(BaseModel):
    name: str = Field(
        description="The name of app to be built")

    description: str = Field(
        description="A oneline description of the app to be built, e.g. 'A web application for managing personal finances'")

    techstack: str = Field(
        description="The tech stack to be used for the app, e.g. 'python', 'javascript', 'react', 'nodejs', etc.")

    features: list[str] = Field(
        description="A list of features that the app should have, e.g. 'user authentication', 'form handling', 'routing', 'paging' etc.")

    files: list[File_schema] = Field(
        description="A list of files to be created, each with a 'path' and 'purpose'")


# defining the schema for the implementation for task
class ImplementationTask(BaseModel):
    filepath: str = Field(
        description="The path to the file to be created or modified, e.g. 'app.py', 'templates/index.html'")

    task_description: str = Field(
        description="A comprehensive description of what to implement in this file. Include: exact functions/classes to define, variables, imports needed, integration with other files, and implementation details. This should be a detailed paragraph.")


# defining the schema for the implementation plan for the task, which includes a list of implementation tasks
class TaskPlan_schema(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(
        description="A list of implementation tasks, one per file. Order by dependencies (requirements.txt first, then core files, then UI files).")

    model_config = ConfigDict(extra="allow")
