# Generate the CRUD API via on of the specs in this folder

# openapi-python-client generate --path 1_person.json
# For more options see https://github.com/openapi-generators/openapi-python-client

# Test the API with the following code

from person_api_client import Client

# Create an instance of the API client
api_client = Client(base_url='localhost:5432')

# Create a new resource
new_resource = {"name": "New Item"}
created_item = api_client.create_item(body=new_resource)
print("Created Item:", created_item)

# Retrieve a resource by ID
retrieved_item = api_client.get_item(item_id=created_item["id"])
print("Retrieved Item:", retrieved_item)

# Update the resource
updated_item = api_client.update_item(item_id=retrieved_item["id"], body={"name": "Updated Item"})
print("Updated Item:", updated_item)

# Delete the resource
deleted_item = api_client.delete_item(item_id=updated_item["id"])
print("Deleted Item:", deleted_item)
