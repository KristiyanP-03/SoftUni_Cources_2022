import '../node_modules/react/umd/react.production.min.js';
import '../node_modules/react-dom/umd/react-dom.production.min.js';

const rootDomElement = document.getElementById('root'); // HTML DOM

const root = ReactDOM.createRoot(rootDomElement); // REACT DOM



const headerJSX = (
    <header className='site-header'> 
       <h1>Hello From JS!</h1>
    </header>
); 
   
root.render(headerJSX);