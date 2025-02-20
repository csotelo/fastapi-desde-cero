# FastAPI Desde Cero

This repository contains the code I developed while self-learning FastAPI through the course "FastAPI Desde Cero" available at [https://cosasdedevs.com/fastapi/](https://cosasdedevs.com/fastapi/).  The original code repository that served as a base for this learning is located at [https://github.com/albertorc87/fastapi-todo-api](https://github.com/albertorc87/fastapi-todo-api).

This project represents my personal journey in understanding and implementing FastAPI.  The course provided valuable insights, and I've incorporated those learnings into this repository. I found the course particularly interesting due to its use of updated libraries and best practices.

## Project Description

This project is a practical implementation of a FastAPI application.  It serves as a learning exercise, demonstrating various aspects of FastAPI development, including:

*   API endpoint creation and management
*   Data validation and serialization
*   Database interaction (if applicable, specify which database)
*   Asynchronous operations
*   Testing
*   Authentication and authorization (if included)

## Getting Started

### Prerequisites

Before running this project, ensure you have the following installed:

*   Python 3.x
*   Poetry (recommended for dependency management) or pip
*   FastAPI
*   Uvicorn (or another ASGI server)

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/csotelo/fastapi-desde-cero.git](https://www.google.com/search?q=https://github.com/YOUR_GITHUB_USERNAME/fastapi-desde-cero.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd fastapi-desde-cero
    ```

3.  Install dependencies using Poetry (recommended):

    ```bash
    poetry install
    ```

    Or, using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the FastAPI application, use Uvicorn:

```bash
uvicorn main:app --reload
```
