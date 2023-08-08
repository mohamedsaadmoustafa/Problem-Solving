function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let resultArr = [];
    for (let [i, n] of arr.entries()){
        resultArr[i] = fn(n, i)
    }
    return resultArr;
};
