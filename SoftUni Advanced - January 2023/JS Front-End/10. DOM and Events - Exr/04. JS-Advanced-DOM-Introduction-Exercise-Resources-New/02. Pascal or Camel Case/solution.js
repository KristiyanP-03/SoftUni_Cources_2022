function solve() {
  let text = document.getElementById("text").value;
  text = text.toLowerCase();
  let textIntoArray = text.split(" ");

  const textType = document.getElementById("naming-convention").value;

  let result = "";



  switch (textType) {
    case "Camel Case":
      result += textIntoArray[0];
      for (let index = 1; index < textIntoArray.length; index++) {
        textIntoArray[index] = textIntoArray[index][0].toUpperCase() + textIntoArray[index].slice(1);
        result += textIntoArray[index];
      }
      break;

    case "Pascal Case":
      for (let index = 0; index < textIntoArray.length; index++) {
        textIntoArray[index] = textIntoArray[index][0].toUpperCase() + textIntoArray[index].slice(1);
        result += textIntoArray[index];
      }
      break;
  
    default:
      result = "Error!";
      break;
  }

  document.getElementById("result").textContent = result;
}