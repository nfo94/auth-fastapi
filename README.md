## FastAPI auth with JWT

This is a study project for authentication and authorization with JWT, FastAPI and also
PyJWT. It lacks password hashing still.

### Installing dependencies

Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for the
project, activate it and run:

```bash
pip install -r requirements
```

### Running the app

After installing dependencies, run:

```bash
uvicorn main:app --reload
```

### Documentation

Go to https://localhost:8000/docs to see the documentation and to test endpoints.
