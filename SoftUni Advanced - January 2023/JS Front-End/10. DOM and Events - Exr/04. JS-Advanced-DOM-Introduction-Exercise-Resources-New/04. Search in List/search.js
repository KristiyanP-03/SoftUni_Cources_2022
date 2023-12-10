function search() {
   const listOfElements = Array.from(document.querySelectorAll("li"));
   const searchText = document.getElementById("searchText").value;
   let matches = 0;

   const regex = new RegExp(searchText, "gi");

   listOfElements.forEach(element => {
       regex.lastIndex = 0;

       if (regex.test(element.textContent)) {
           element.style.fontWeight = "bold";
           element.style.textDecoration = "underline";
           matches += 1;
       } else {
           element.style.fontWeight = "normal";
           element.style.textDecoration = "none";
       }
   });

   document.getElementById("result").textContent =  `${matches} matches found`;
}