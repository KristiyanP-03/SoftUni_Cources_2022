import { useNavigate, useParams } from 'react-router-dom';

import * as recipeService from '../../services/recipeService';
import { useEffect, useState } from 'react';



export default function RecipeEdit() {
    const navigate = useNavigate();
    const { gameId } = useParams();
    const [recipe, setRecipe] = useState({
        title: '',
        category: '',
        imageUrl: '',
        ingrediants: '',
    });


    useEffect(() => {
        recipeService.getOne(gameId)
            .then(result => {
                setRecipe(result);
            });
    }, [gameId]);


    const editRecipeSubmitHandler = async (e) => {
        e.preventDefault();

        const values = Object.fromEntries(new FormData(e.currentTarget));

        try {
            await recipeService.edit(gameId, values);

            navigate('/');
        } catch (err) {
            console.log(err);
        }
    }


    const onChange = (e) => {
        setRecipe(state => ({
            ...state,
            [e.target.name]: e.target.value
        }));
    };


    
    return (
        <section id="create-page" className="auth">
            <form id="create" onSubmit={editRecipeSubmitHandler}>
                <div className="container">
                    <h1>Your recipe</h1>
                    <label htmlFor="leg-title">Dish:</label>
                    <input type="text" id="title" name="title" value={recipe.title} onChange={onChange} placeholder="Enter game title..." />

                    <label htmlFor="category">Category:</label>
                    <input type="text" id="category" name="category" value={recipe.category} onChange={onChange} placeholder="Enter game category..." />
                    
                    <label htmlFor="game-img">Image:</label>
                    <input type="text" id="imageUrl" name="imageUrl" value={recipe.imageUrl} onChange={onChange} placeholder="Upload a photo..." />

                    <label htmlFor="ingrediants">Ingrediants:</label>
                    <textarea name="ingrediants" value={recipe.ingrediants} onChange={onChange} id="ingrediants"></textarea>
                    <input className="btn submit" type="submit" value="Edit Recipe" />
                </div>
            </form>
        </section>
    );
}
