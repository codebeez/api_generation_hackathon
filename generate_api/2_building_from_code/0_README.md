# Generating an OpenAPI specification from code
Here we would do the opposite from the previous part. We already have Python code and we want to create an interface for others to interact with it.

Given is a CRUD application for the human resources table for shifts. Use that to generate an Open API spec.
You can start the API with `uvicorn 1_shift:app --reload` in `/workspace/generate_api/2_building_from_code`

FastAPI can show you the API documentation on `127.0.0.1:8000/docs` but where does it store the needed spec?
Look into this link to read about extending this FastAPI feature https://fastapi.tiangolo.com/advanced/extending-openapi/

The example is written in FastAPI but you can also choose to use Django for this. You would need to add the package yourself to the devcontainer.

## Bonus
Check what happens when you redo step 1 using the generated API from the spec. Does using that code generate the same spec as you started with? 
If not, what would need to change to have it match? And if you generate the code from that spec, does it still match?