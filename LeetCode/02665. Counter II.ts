type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    let change = 0;
    return {
        increment: () => init + ++change,
        decrement: () => init + --change,
        reset: () =>  {
            change = 0;
            return init;
        }
    }
  
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
