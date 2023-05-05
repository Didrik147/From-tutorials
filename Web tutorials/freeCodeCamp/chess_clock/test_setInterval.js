let count = 1;

// Assign a timed event to variable timerId

const timerId = setInterval(() => {
    console.log(`Executing function for ${count} seconds.`);

    // Increment the count variable by one.
    count++;

    if (count === 4){
        // Stop event by calling clearInterval on timerId.
        clearInterval(timerId);
        console.log('Timing event cleared.')
    }

}, 1000); // Execute event every second (1000 ms = 1 s)


