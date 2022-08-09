"""The blueprint related to the /pets/ endpoint functionality."""
from datetime import datetime

import marshmallow as ma
from flask.views import MethodView
from flask_smorest import abort
from flask_smorest import Blueprint

from src import db

TABLE_NAME = "pets"


class PetSchema(ma.Schema):
    """Pet schema for API requests/responses."""

    id = ma.fields.Int(dump_only=True, required=False)
    name = ma.fields.String()
    created = ma.fields.DateTime(format="%Y-%m-%d %H:%M:%S", required=False, missing=datetime.now)
    updated = ma.fields.DateTime(format="%Y-%m-%d %H:%M:%S", required=False, missing=datetime.now)


pets_blueprint = Blueprint("pets", "pets", url_prefix="/pets", description="Operations on pets")


@pets_blueprint.route("/")
class Pets(MethodView):
    @staticmethod
    @pets_blueprint.response(200, PetSchema(many=True))
    def get():
        """Finds all pets in the database."""
        return db.select_all(TABLE_NAME)

    @staticmethod
    @pets_blueprint.arguments(PetSchema)
    @pets_blueprint.response(201, PetSchema)
    def post(data):
        """Adds a new pet."""
        if not data.get("name"):
            abort(400, message="The pet name is empty. Empty names are not allowed.")
        if db.is_exists(TABLE_NAME, "name", data["name"]):
            abort(400, message=f"Item with the name '{data['name']}' is already exists.")
        inserted_id = db.insert(TABLE_NAME, ["name"], [data["name"]])
        if not inserted_id:
            abort(500, message="Insert failed for unkown reasons.")
        return db.select_by_id(TABLE_NAME, inserted_id)


@pets_blueprint.route("/id/<pet_id>")
class PetsById(MethodView):
    @staticmethod
    @pets_blueprint.response(200, PetSchema)
    def get(pet_id):
        """Gets pet by ID."""
        item = db.select_by_id(TABLE_NAME, pet_id)
        if item:
            return item
        return {}

    @staticmethod
    @pets_blueprint.arguments(PetSchema)
    @pets_blueprint.response(200, PetSchema)
    def put(data, pet_id):
        """Updates an existing pet."""
        if not data.get("name"):
            abort(400, message="The pet name is empty. Empty names are not allowed.")
        if not db.is_exists(TABLE_NAME, "id", pet_id):
            abort(400, message=f"Item with the name '{data['name']}' does not exists.")
        is_updated = db.update(
            TABLE_NAME,
            ["name", "updated"],
            [data["name"], datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            f"id={pet_id}",
        )
        if not is_updated:
            abort(500, message="Update failed for unkown reasons.")
        return db.select_by_id(TABLE_NAME, pet_id)

    @staticmethod
    @pets_blueprint.response(204)
    def delete(pet_id):
        """Deletes a pet."""
        if not db.is_exists(TABLE_NAME, "id", pet_id):
            abort(400, message="Item does not exists.")
        is_deleted = db.delete(TABLE_NAME, f"id={pet_id}")
        if not is_deleted:
            abort(500, message="Delete failed for unkown reasons.")


@pets_blueprint.route("/name/<pet_name>")
class PetsByName(MethodView):
    @staticmethod
    @pets_blueprint.response(200, PetSchema)
    def get(pet_name):
        """Gets pet by name."""
        item = list(db.select_all(TABLE_NAME, where=f"name='{pet_name}' COLLATE NOCASE"))
        if item:
            return item[0]
        return {}
