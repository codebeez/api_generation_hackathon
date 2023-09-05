## Generating OpenAPI specs from the database
Use the models in the database or in the SQL file to create specs. You are free to choose whatever method you want to use for creating these specs.
The fastest way would be to use an LLM Model such as ChatGPT, Bard, Starcoder or any others that you know.

Another method is to find a package that can create the spec from a Python model. For this you would need to generate the model from the database.
The package https://github.com/awtkns/fastapi-crudrouter could help with creating the code afterwards
