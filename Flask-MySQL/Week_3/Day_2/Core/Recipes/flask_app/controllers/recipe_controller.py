from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipe')
def recipe():
    if 'user_id' not in session:
        return redirect('/')
    recipes = Recipe.get_all()  
    logged_user = User.get_by_id({"id": session['user_id']})  
    return render_template("recipe.html", recipes=recipes, logged_user=logged_user)

@app.route("/recipe/new", methods=["GET", "POST"])
def now():
    if request.method == "POST":
        id = request.form.get("id")  
        data = {
            "id": id
        }
        return render_template("new.html", user=User.get_one(data))
    else:
        return render_template("new.html")

@app.route("/recipe/create", methods=["POST"])
def add_recipe():
    if Recipe.validate(request.form):
        data = {
            **request.form,
            "user_id": session['user_id']
        }
        Recipe.create(data)  
        return redirect("/recipe")
    return redirect("/recipe/new")

@app.route('/recipes/<int:id>')
def show_one_recipe(id): 
    if not 'user_id' in session:
        return redirect('/')
    
    recipe = Recipe.get_by_id({"id": id})
    return render_template("recipe.html", recipe=recipe)

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):  
    recipe = Recipe.get_by_id({"id": id})
    return render_template("edit.html", recipe=recipe)

@app.route("/recipes/<int:id>/update", methods=["POST"]) 
def update_recipe(id): 
    if Recipe.validate(request.form):
        data = { 
            **request.form, 
            "id": id
        } 
        Recipe.update(data)  
        return redirect("/recipes")
    
    return redirect(f"/recipes/{id}/edit")

