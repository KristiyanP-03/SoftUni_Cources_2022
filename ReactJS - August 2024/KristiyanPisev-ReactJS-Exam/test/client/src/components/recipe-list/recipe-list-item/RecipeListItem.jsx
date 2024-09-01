import { Link } from "react-router-dom";



export default function RecipeListItem({
    _id,
    title,
    imageUrl,
}) {


    return (
        <div className="allRecipes">
            <div className="allRecipes-info">
                <Link to={`/games/${_id}`}><img src={imageUrl} /></Link>
                <Link to={`/games/${_id}`} className="details-button">{title}</Link>
            </div>
        </div>
    );
}
