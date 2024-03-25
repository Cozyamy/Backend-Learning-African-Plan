# Path Parameters:
## What are path parameters in FastAPI?
- In FastAPI, path parameters are parts of the URL path that can change and are used to capture specific values provided by the client. They are denoted by curly braces {} within the route definition. Path parameters allow you to define routes that accept dynamic values, making your API more flexible and powerful.
``` from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
- In this example, {item_id} is a path parameter. When a request is made to /items/123, FastAPI will capture 123 as the value for item_id and pass it to the read_item function.

## How are path parameters defined in FastAPI route declarations?
- In FastAPI route declarations, path parameters are defined by including them directly within the URL path as part of the route's endpoint definition. Path parameters are enclosed in curly braces {}.
Here's the general syntax for defining a route with path parameters in FastAPI:
``` from fastapi import FastAPI

app = FastAPI()

@app.method("/route/{parameter_name}")
async def endpoint_name(parameter_name: parameter_type):
```

## Can path parameters have default values? If yes, how can they be set?
- No, path parameters do not have default values. Path parameters are typically used to capture dynamic values from the URL path, and they must be provided in the request URL.
- But you can define multiple endpoints with different routes. Each endpoint can have its own logic and handle different scenarios. By defining endpoints with and without path parameters, you can simulate having default values for path parameters.

## Provide an example of a FastAPI route with path parameters.
``` from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
- The route is defined using @app.get("/items/{item_id}").
{item_id} is the path parameter. It's a placeholder that captures the value provided in the URL.
item_id is the name of the path parameter as it will be referenced in the function signature.
int specifies the type of the path parameter. In this case, it expects an integer value.
When a request is made to a URL like /items/123, FastAPI will capture 123 as the value for item_id, convert it to an integer, and pass it to the read_item function. You can then use this value within the function to perform whatever logic you need and return a response.


# Query Parameters:
## What are query parameters in FastAPI?
- Query parameters are additional parameters appended to the URL after a question mark ? and separated by ampersands &. They are used to provide optional data to an endpoint and are typically used for filtering, sorting, or providing additional options to the client.
``` from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = None, page: int = 1, sort: str = None):
    return {"category": category, "page": page, "sort": sort}
```

`/items/ is the route for the endpoint.
category, page, and sort are query parameters.
Each parameter has a default value specified (None for category and sort, and 1 for page).
FastAPI will automatically parse any query parameters provided in the request URL and pass them to the read_items function as arguments. If a query parameter is not provided, it will use the default value specified in the function signature.
- example: ```http://example.com/items?category=electronics&page=1&sort=price
```

## How are query parameters defined in FastAPI route declarations?
- Query parameters are defined as function parameters in the endpoint function signature. Here's how you define query parameters in FastAPI route declarations:
``` from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = None, page: int = 1, sort: str = None):
    """
    Endpoint to retrieve items with optional query parameters.
    """
``` When a request is made to the endpoint /items/, FastAPI will automatically parse any query parameters provided in the URL and pass them to the read_items function as arguments. If a query parameter is not provided in the request, the default value specified in the function signature will be used. ```

## What is the difference between path parameters and query parameters?

| Aspect                  | Path Parameters                                         | Query Parameters                                         |
|-------------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Location in URL         | Part of the URL path                                    | Appended to the end of the URL after a `?`                |
| Syntax                  | Enclosed in curly braces `{}` within the URL path        | Key-value pairs separated by `&` after a `?`              |
| Usage                   | Identifies specific resources or endpoints              | Provides additional data for filtering, sorting, etc.     |
| Requirement             | Required in the URL path for endpoint matching           | Optional, can be omitted from the URL                     |
| Example URL             | `/users/{user_id}`                                      | `/search?query=term&page=1`                               |
| Example Usage in Python | ```python                                                | ```python                                                |
|                         | @app.get("/users/{user_id}")                            | @app.get("/search")                                      |
|                         | async def get_user(user_id: int):                       | async def search_items(query: str, page: int = 1):       |
|                         |     # Endpoint logic                                    |     # Endpoint logic                                    |
| ```                     | ```                                                     | ```                                                       |

This table summarizes the key differences between path parameters and query parameters in terms of their location in the URL, syntax, usage, requirement, and provides examples of their usage in FastAPI route declarations.

## Can query parameters have default values? If yes, how can they be set?

- Yes, query parameters in FastAPI can have default values, and they are set by providing default values in the function signature of the endpoint.
- You can set default values for query parameters in FastAPI by simply providing the default value in the function signature, similar to how you set default values for regular function parameters in Python.
``` from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = "electronics", page: int = 1, sort: str = "name"):
    """
    Endpoint to retrieve items with optional query parameters.
    """
    return {"category": category, "page": page, "sort": sort}
```

## Provide an example of a FastAPI route with query parameters.
``` from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = None, page: int = 1, sort: str = None):
    """
    Endpoint to retrieve items with optional query parameters.
    """
    return {"category": category, "page": page, "sort": sort}
```
- category, page, and sort are query parameters defined as function parameters in the read_items function signature.