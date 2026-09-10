function slowFunction() {
    let total = 0;

    for (let i = 0; i < 50000000; i++) {
        total += i;
    }

    return total;
}

function fastFunction() {
    let total = 0;

    for (let i = 0; i < 1000; i++) {
        total += i;
    }

    return total;
}

function main() {
    console.log("Application started");

    fastFunction();

    slowFunction();

    console.log("Application finished");
}

main();