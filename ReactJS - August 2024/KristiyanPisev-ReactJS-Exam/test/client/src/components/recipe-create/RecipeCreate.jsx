import { useNavigate } from 'react-router-dom';

import * as recipeService from '../../services/recipeService';



export default function RecipeCreate() {
    const navigate = useNavigate();

    
    const createRecipeSubmitHandler = async (e) => {
        e.preventDefault();

        const recipeData = Object.fromEntries(new FormData(e.currentTarget));

        try {
            await recipeService.create(recipeData);

            navigate('/recipes');
        } catch (err) {
            console.log(err);
        }
    }



    return (
        <section id="create-page" className="auth">
            <form id="create" onSubmit={createRecipeSubmitHandler}>
                <div className="container">
                    <h1>Create Recipe</h1>
                    <label htmlFor="title">Food title:</label>
                    <input type="text" id="title" name="title" placeholder="--- food title ---" />

                    <label htmlFor="category">Category:</label>
                    <input type="text" id="category" name="category" placeholder="--- food category ---" />

                    <label htmlFor="game-img">Image:</label>
                    <input type="text" id="imageUrl" name="imageUrl" placeholder="--- photo URL ---" />

                    <label htmlFor="ingrediants">Ingrediants:</label>
                    <textarea name="ingrediants" id="ingrediants"></textarea>
                    <input className="btn submit" type="submit" value="Create Recipe" />
                </div>
            </form>
        </section>
    );
}
