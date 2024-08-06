import '../node_modules/react/umd/react.production.min.js';
import '../node_modules/react-dom/umd/react-dom.production.min.js';

var rootDomElement = document.getElementById('root'); // HTML DOM

var root = ReactDOM.createRoot(rootDomElement); // REACT DOM


var headerJSX = React.createElement(
   'header',
   { className: 'site-header' },
   React.createElement(
      'h1',
      null,
      'Hello From JS!'
   )
);

root.render(headerJSX);