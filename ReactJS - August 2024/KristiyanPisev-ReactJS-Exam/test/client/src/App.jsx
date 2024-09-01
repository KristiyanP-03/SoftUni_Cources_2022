import { Routes, Route } from 'react-router-dom';


import { AuthProvider } from './contexts/authContext';
import Path from './paths';


import Header from "./components/header/Header"
import Home from "./components/home/Home"
import RecipeList from './components/recipe-list/RecipeList';
import RecipeCreate from './components/recipe-create/RecipeCreate';
import Login from './components/login/Login';
import Logout from './components/logout/Logout';
import Register from './components/register/Register';
import RecipeDetails from './components/recipe-details/RecipeDetails';
import GameEdit from './components/recipe-edit/RecipeEdit';
import AuthGuard from './components/guards/AuthGuard';
import NotFound from './components/NotFound';




function App() {
    return (
            <AuthProvider>

                <div id="box">
                    <Header />
                    <Routes>
                        <Route path={Path.Home} element={<Home />} />
                        <Route path="/recipes" element={<RecipeList />} />
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                        <Route path="/games/:gameId" element={<RecipeDetails />} />
                        <Route element={<AuthGuard />}>
                            <Route path="/recipes/create" element={<RecipeCreate />} />
                            <Route path={Path.GameEdit} element={<GameEdit />} />
                            <Route path={Path.Logout} element={<Logout />} />
                        </Route>
                    <Route path="*" element={<NotFound />} />
                </Routes>
            </div>

        </AuthProvider>
    );
}



export default App;