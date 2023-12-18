function motoGPRace(input) {
    // Riders number
    const numberOfRiders = parseInt(input[0]);

    let riders = [];

    // Riders info
    for (let index = 1; index <= numberOfRiders; index++) {
        let riderInfo = input[index].split('|');

        let riderObject = {
            riderName: riderInfo[0],
            fuelCapacity: parseInt(riderInfo[1]),
            position: parseInt(riderInfo[2])
        };

        if (riderObject.fuelCapacity > 100) {
            riderObject.fuelCapacity = 100;
        }

        riders.push(riderObject);
    }

    // Riders actions
    for (let index = numberOfRiders + 1; index < input.length; index++) {
        let action = input[index].split(" - ");

        switch (action[0]) {
            case "StopForFuel":
                let rider = action[1];
                let minimumFuel = parseInt(action[2]);
                let newPosition = parseInt(action[3]);

                riders.forEach(element => {
                    if (element.riderName == rider) {
                        if (element.fuelCapacity < minimumFuel) {
                            element.position = newPosition;
                            console.log(`${element.riderName} stopped to refuel but lost his position, now he is ${element.position}.`);
                        } else {
                            console.log(`${element.riderName} does not need to stop for fuel!`);
                        }
                    }
                });
                break;

            case "Overtaking":
                let rider1 = action[1];
                let rider2 = action[2];

                let indexRider1 = riders.findIndex(r => r.riderName === rider1);
                let indexRider2 = riders.findIndex(r => r.riderName === rider2);

                if (riders[indexRider1].position < riders[indexRider2].position) {
                    [riders[indexRider1].position, riders[indexRider2].position] = [riders[indexRider2].position, riders[indexRider1].position];
                    console.log(`${rider1} overtook ${rider2}!`);
                }
                break;

            case "EngineFail":
                let failedRider = action[1];
                let lapsLeft = parseInt(action[2]);

                console.log(`${failedRider} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`);

                // Remove the failed rider from the array
                riders = riders.filter(r => r.riderName !== failedRider);
                break;

            case "Finish":
                // Print final positions
                riders.sort((a, b) => a.position - b.position)
                    .forEach(r => console.log(`${r.riderName}\n  Final position: ${r.position}`));
                break;

            default:
                break;
        }
    }
}