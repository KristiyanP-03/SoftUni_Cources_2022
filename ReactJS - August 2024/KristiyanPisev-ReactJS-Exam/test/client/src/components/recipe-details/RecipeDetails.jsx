import { useContext, useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import * as recipeService from '../../services/recipeService';
import AuthContext from "../../contexts/authContext";
import { pathToUrl } from "../../utils/pathUtils";
import Path from "../../paths";



export default function RecipeDetails() {
    const navigate = useNavigate();
    const { email, userId } = useContext(AuthContext);
    const [recipe, setRecipe] = useState({});
    const { gameId } = useParams();


    useEffect(() => {
        recipeService.getOne(gameId)
            .then(setRecipe);

    }, [gameId]);



    const deleteButtonClickHandler = async () => {
        const hasConfirmed = confirm(`Are you sure you want to delete ${recipe.title}`);

        if (hasConfirmed) {
            await recipeService.remove(gameId);

            navigate('/');
        }
    }



    return (
        <section id="recipe-details">
            <h1>Recipe Details</h1>

            <div className="info-section">
                <div className="recipe-header">
                    <img className="recipe-img" src={recipe.imageUrl} alt={recipe.title} />
                    <h1>{recipe.title}</h1>
                    <h4 className="type">{recipe.category}</h4>
                </div>
                <p>Ingrediants/How to cook:</p>
                <p className="text">{recipe.ingrediants}</p>

                <p>Created by: {email}</p>

                {userId === recipe._ownerId && (
                    <div className="buttons">
                        <Link to={pathToUrl(Path.GameEdit, { gameId })} className="button">Edit</Link>
                        <button className="button" onClick={deleteButtonClickHandler}>Delete</button>
                    </div>
                )}
            </div>
        </section>
    );
}
