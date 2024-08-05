import '../node_modules/react/umd/react.production.min.js';
import '../node_modules/react-dom/umd/react-dom.production.min.js';

const rootDomElement = document.getElementById('root'); // HTML DOM

const root = ReactDOM.createRoot(rootDomElement); // REACT DOM

// --- JS (bad practice) --------------------------------------------------------------------------
// const reactHeadingElement = React.createElement('h1', {}, "Hello From JS!");
// const h2 = React.createElement('h2', {}, "Hello From JS! X2");
// const headerJS = React.createElement('header', {className: "site-header"}, reactHeadingElement, h2);

// root.render(headerJS);
// ----------------------------------------------------------------------------------------------

// --- JSX ------------------------------------------------------------------------------------------
const headerJSX = (
 <header className='site-header'> 
    <h1>Hello From JS!</h1>
 </header>
); 
//Error: "<"     "terminal": npm install babel-cli@6 babel-preset-react-app@3
   // и в package.json 
   /*
   "scripts": {
      "build": "npx babel --watch src --out-dir build --preset react-app/prod"
   },
   */
   //"terminal": npm run build

root.render(headerJSX);