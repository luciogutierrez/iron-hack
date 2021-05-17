from flask import Flask, render_template, jsonify, request
from http import HTTPStatus
from os import environ

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Taquitos',
        'description': 'Unos taquitos asi bien ricos'
    },
    {
        'id': 2,
        'name': 'Chilaquiles',
        'description': 'MMm pa la cruda'
    }
]


@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'recipe not found'}, HTTPStatus.NOT_EXTENDED)


@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }
    recipes.append(recipe)
    return (jsonify(recipe), HTTPStatus.CREATED)

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    recipe.update(
        {
            'name': name,
            'description': description
        }
    )
    return jsonify(recipe), HTTPStatus.OK

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    recipes.remove(recipe)
    return '', HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run(debug=True)
