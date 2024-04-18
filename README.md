
## User Management
1. **Register a new user**
    - **Endpoint:** POST /api/register/
    - **URL:** http://127.0.0.1:8000/api/register/
    - **Body:** username: user123, email: user@g.com, password: user123

2. **Log in an existing user**
    - **Endpoint:** POST /api/login/
    - **URL:** http://127.0.0.1:8000/api/login/
    - **Body:** username: user123, password: user123

3. **Refresh the authentication token**
    - **Endpoint:** POST /api/refresh/
    - **URL:** http://127.0.0.1:8000/api/refresh/
    - **Body:** refresh_token: [Refresh Token]

## Snippet Management
1. **Create a new snippet**
    - **Endpoint:** POST /api/snippets/create/
    - **URL:** http://127.0.0.1:8000/api/snippets/create/
    - **Headers:** Authorization: Bearer [Access Token]
    - **Body (JSON):**
        ```json
        {
            "title": "Example Snippet new",
            "text": "This is an example snippet content.",
            "timestamp": "2024-04-19T08:00:00Z",
            "tags": [
                {"title": "Tag4"}
            ]
        }
        ```

2. **Retrieve details of a specific snippet**
    - **Endpoint:** GET /api/snippets/{snippet_id}/
    - **URL:** http://127.0.0.1:8000/api/snippets/10/

3. **Update a specific snippet**
    - **Endpoint:** PUT /api/snippets/{snippet_id}/update/
    - **URL:** http://127.0.0.1:8000/api/snippets/10/update/
    - **Body (JSON):**
        ```json
        {
            "title": "Updated Title",
            "text": "Updated content"
        }
        ```

4. **Delete a specific snippet**
    - **Endpoint:** DELETE /api/snippets/{snippet_id}/delete/
    - **URL:** http://127.0.0.1:8000/api/snippets/10/delete/

## Tag Management
1. **List all available tags**
    - **Endpoint:** GET /api/tags/
    - **URL:** http://127.0.0.1:8000/api/tags/

2. **Retrieve details of a specific tag**
    - **Endpoint:** GET /api/tags/{tag_id}/
    - **URL:** http://127.0.0.1:8000/api/tags/12/

## Overview
1. **Retrieve an overview**
    - **Endpoint:** GET /api/overview/
    - **URL:** http://127.0.0.1:8000/api/overview/

2. **Retrieve overview details of a specific snippet**
    - **Endpoint:** GET /api/snippets/{snippet_id}/overview/
    - **URL:** http://127.0.0.1:8000/api/snippets/11/overview/
