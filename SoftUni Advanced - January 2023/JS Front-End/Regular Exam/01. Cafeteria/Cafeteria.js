function cafeteriaProblemSolution(inputArray) {
    // number of the baristas--------------------------------------------
    const numberOfBaristas = parseInt(inputArray[0]);
  
    // baristas into separated objects-----------------------------------
    let baristas = [];
  
    for (let index = 1; index <= numberOfBaristas; index++) {
      let currentBaristaDetails = inputArray[index].split(" ");
  
      let baristaAsObject = {
        baristaName: currentBaristaDetails[0],
        shift: currentBaristaDetails[1],
        coffeeType: currentBaristaDetails[2].split(","),
      };
  
      baristas.push(baristaAsObject);
    }
  
    // commands---------------------------------------------------------
    for (let index = numberOfBaristas + 1; index < inputArray.length; index++) {
      let command = inputArray[index].split(" / ");
  
      switch (command[0]) {
        //CASE ---------------------------------------------------------------------(1)
        case "Prepare":


          let prepareCoffe = baristas.find(
            (barista) =>
              barista.baristaName == command[1] &&
              barista.shift == command[2] &&
              barista.coffeeType.includes(command[3])
          );

  
          if (prepareCoffe) {
            console.log(
              `${prepareCoffe.baristaName} has prepared a ${command[3]} for you!`
            );
          } 
          else {
            console.log(
              `${command[1]} is not available to prepare a ${command[3]}.`
            );
          }


          break;
  


        //CASE----------------------------------------------------------------------------(2)
        case "Change Shift":


          let changeShift = baristas.find(
            (barista) => barista.baristaName == command[1]
          );
  

          if (changeShift) {
            changeShift.shift = command[2];

            console.log(
              `${changeShift.baristaName} has updated his shift to: ${command[2]}`
            );
          }

          break;
  
        

        //CASE----------------------------------------------------------------------------(3)
        case "Learn":


          let learnNewCoffeeType  = baristas.find(
            (barista) => barista.baristaName == command[1]
          );
  

          if (learnNewCoffeeType ) {

            if (learnNewCoffeeType.coffeeType.includes(command[2])) {
              console.log(
                `${learnNewCoffeeType.baristaName} knows how to make ${command[2]}.`
              );
            } 
            else {
                learnNewCoffeeType.coffeeType.push(command[2]);
              console.log(
                `${learnNewCoffeeType.baristaName} has learned a new coffee type: ${command[2]}.`
              );
            }

          }


          break;
  

        
        //CASE---------------------------------------------------------------------------------(END)
        case "Closed":
          break;
  
        default:
          break;
      }
    }
  


    //output--------------------------------------------------------------------------
    for (let barista of baristas) {
      console.log(
        `Barista: ${barista.baristaName}, Shift: ${barista.shift}, Drinks: ${barista.coffeeType.join(", ")}`
      );
    }
}