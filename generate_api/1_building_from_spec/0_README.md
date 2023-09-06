# Generating an API from an OpenAPI specification
Use the supplied specification to generate a CRUD skeleton in Python.
You can use an online generator or packages such as 
- [FastAPI Code Generator](https://pypi.org/project/fastapi-code-generator/) Setup by default
- [OpenAPI Python Client](https://github.com/openapi-generators/openapi-python-client)

to generate the code. The FastAPI and OpenAPI Python packages both use Pydantic for the models but are on different versions. If you want to try both you would have to remove one and add the other one to Poetry in the `.devcontainer`. Some of the packages build the api skeleton and others can also generate some basic CRUD code. I suggest to try them all and see which gives you the best result. 

JSON and YAML templates are provided for a Person CRUD API. This is based on the person table from the AdventureWorks database.
You can use these files as input for the above packages 

## fastapi code generator
Run `fastapi-codegen --input 1_person.yaml --output person` in this directory
cd into `person/` and run `uvicorn main:app --reload`. Check the API out on `127.0.0.1:8000/docs`
This does not generate any code for the routes, just the models and the routes

## OpenAPI Generator
Command for OpenAPI Generator in Docker, you can run it in `1_building_from_spec`
```
docker run --rm -v ${PWD}:/generate_api openapitools/openapi-generator-cli:latest generate -i /generate_api/1_person.yaml -g python-fastapi -o /generate_api/out
```



