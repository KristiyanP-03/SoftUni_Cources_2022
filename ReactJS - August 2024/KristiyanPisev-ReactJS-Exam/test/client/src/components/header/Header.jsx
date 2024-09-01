import { useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../../contexts/authContext';



export default function Header() {
    const {
        isAuthenticated,
        username,
    } = useContext(AuthContext);


    return (
        <header>
            <h1>
                <Link className="home gotvach" to="/">gotvach</Link>
                <Link className="home bg" to="/">.BG</Link>
            </h1>


            <nav>
                <Link to="/recipes">RECIPES</Link>
                {isAuthenticated && (
                    <div id="user">
                        <Link to="/recipes/create">CREATE</Link>
                        <Link to="/logout">LOGOUT</Link>
                        <span>| {username}</span>
                    </div>
                )}
                {!isAuthenticated && (
                    <div id="guest">
                        <Link to="/login">LOGIN</Link>
                        <Link to="/register">REGISTER</Link>
                    </div>
                )}
            </nav>
        </header>
    );
}
