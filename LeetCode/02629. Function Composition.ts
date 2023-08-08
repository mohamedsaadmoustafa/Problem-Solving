type F = (x: number) => number;

function compose(functions: F[]): F {
    const reversedFunctions = functions.slice().reverse();
    return function(x) {
        for (let f of reversedFunctions){
            x = f(x);
        }
        return x;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
