import { useEffect, useState } from 'react';

import * as recipeService from '../../services/recipeService';
import RecipeListItem from './recipe-list-item/RecipeListItem';



export default function RecipeList() {
    const [recipes, setRecipes] = useState([]);


    useEffect(() => {
        recipeService.getAll()
            .then(result => setRecipes(result))
            .catch(err => {
                console.log(err);
            });
    }, []);


    
    return (
        <section>
            <h1>All Recipes</h1>

            {recipes.map(recipe => (
                <RecipeListItem key={recipe._id} {...recipe} />
            ))}

            {recipes.length === 0 && (
                <h3 className="no-recipes">No recipes</h3>
            )}
        </section>
    );
}
