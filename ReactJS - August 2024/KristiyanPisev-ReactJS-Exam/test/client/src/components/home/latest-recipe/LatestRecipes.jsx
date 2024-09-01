import { Link } from "react-router-dom";
import Path from "../../../paths";
import { pathToUrl } from "../../../utils/pathUtils";



export default function LatestRecipe({
    _id,
    imageUrl,
    title,
}) {


    return (
        <div className="recipe">         
            <div className="data-buttons">
                <Link to={pathToUrl(Path.GameDetails, { gameId: _id })} className="btn details-btn">
                <div className="image-wrap">
                    <img src={imageUrl} />
                </div>
                <h3>{title}</h3>          
                </Link>
            </div>
        </div>
    );
}
