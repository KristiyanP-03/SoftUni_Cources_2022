import '../node_modules/react/umd/react.production.min.js';
import '../node_modules/react-dom/umd/react-dom.production.min.js';

var rootDomElement = document.getElementById('root'); // HTML DOM

var root = ReactDOM.createRoot(rootDomElement); // REACT DOM

// --- JS (bad practice) --------------------------------------------------------------------------
// const reactHeadingElement = React.createElement('h1', {}, "Hello From JS!");
// const h2 = React.createElement('h2', {}, "Hello From JS! X2");
// const headerJS = React.createElement('header', {className: "site-header"}, reactHeadingElement, h2);

// root.render(headerJS);
// ----------------------------------------------------------------------------------------------

// --- JSX ------------------------------------------------------------------------------------------
var headerJSX = React.createElement(
   'header',
   { className: 'site-header' },
   React.createElement(
      'h1',
      null,
      'Hello From JS!'
   )
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