function astroAdventure(arrayInput) {
    // number of astronauts
    const numberOfAstronauts = parseInt(arrayInput[0]);
    const astronauts = [];
  
    // each astronaut described as an object
    for (let index = 1; index <= numberOfAstronauts; index++) {
      let currentAstronautDetails = arrayInput[index].split(" ");
  
      let astronautAsObject = {
        astronautName: currentAstronautDetails[0],
        oxygenLevel: parseInt(currentAstronautDetails[1]),
        energyReserves: parseInt(currentAstronautDetails[2]),
      };
  
      astronauts.push(astronautAsObject);
    }
  
    // astronaut's actions
    for (let index = numberOfAstronauts + 1; index <= arrayInput.length; index++) {
      let action = arrayInput[index].split(" - ");
  
      switch (action[0]) {
        case "Explore":
          let astronautIndexExplore = astronauts.findIndex(
            (a) => a.astronautName === action[1]
          );
          let energyNeeded = parseInt(action[2]);
  
          if (astronauts[astronautIndexExplore].energyReserves >= energyNeeded) {
            astronauts[astronautIndexExplore].energyReserves -= energyNeeded;
            console.log(
              `${action[1]} has successfully explored a new area and now has ${astronauts[astronautIndexExplore].energyReserves} energy!`
            );
          } else {
            console.log(`${action[1]} does not have enough energy to explore!`);
          }
          break;
  
        case "Refuel":
          let astronautIndexRefuel = astronauts.findIndex(
            (a) => a.astronautName === action[1]
          );
          let amountRecoveredRefuel = Math.min(
            200 - astronauts[astronautIndexRefuel].energyReserves,
            parseInt(action[2])
          );
  
          astronauts[astronautIndexRefuel].energyReserves += amountRecoveredRefuel;
          console.log(
            `${action[1]} refueled their energy by ${amountRecoveredRefuel}!`
          );
          break;
  
        case "Breathe":
          let astronautIndexBreathe = astronauts.findIndex(
            (a) => a.astronautName === action[1]
          );
          let amountRecoveredBreathe = Math.min(
            100 - astronauts[astronautIndexBreathe].oxygenLevel,
            parseInt(action[2])
          );
  
          astronauts[astronautIndexBreathe].oxygenLevel += amountRecoveredBreathe;
          console.log(
            `${action[1]} took a breath and recovered ${amountRecoveredBreathe} oxygen!`
          );
          break;
  
        case "End":
          astronauts.forEach((a) => {
            console.log(
              `Astronaut: ${a.astronautName}, Oxygen: ${a.oxygenLevel}, Energy: ${a.energyReserves}`
            );
          });
          index = arrayInput.length + 1;
          break;
  
        default:
          break;
      }
    }
  }