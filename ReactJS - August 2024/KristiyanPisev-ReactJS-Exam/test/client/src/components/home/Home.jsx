import { useEffect, useState } from "react";
import withAuth from "../../HOC/withAuth";
import * as recipeService from '../../services/recipeService';
import LatestRecipe from "./latest-recipe/LatestRecipes";




function Home({
    _id,
    accessToken,
    email,
}) {
    const [latestRecipes, setLatestRecipes] = useState([]);


    useEffect(() => {
        recipeService.getLatest()
            .then(result => setLatestRecipes(result));
    }, [])


    return (
        <section>
            <div>
                {latestRecipes.map(recipe => <LatestRecipe {...recipe} />)}
                {!latestRecipes.length && <p className="no-articles">No recipes yet</p>}
            </div>



            <footer className="footer">
                <div className="container">
                    <p>Created by Kristiyan Pisev for ReactJS Exam Project 18/8/2024</p>
                    <p>Github link: <a href="https://github.com/KristiyanP-03/KristiyanPisev-ReactJS-Exam" target="_blank" rel="noopener noreferrer">https://github.com/KristiyanP-03/KristiyanPisev-ReactJS-Exam</a></p>
                </div>
            </footer>
        </section>

        
    );
}


const EnhancedHome = withAuth(Home);


export default EnhancedHome;
