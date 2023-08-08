function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    let filteredArr = [];
    for (let [i, n] of arr.entries()){
        if(fn(n, i)) filteredArr.push(n)
    }
    return filteredArr;
};
