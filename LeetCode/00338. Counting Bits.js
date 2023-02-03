/**
 * @param {number} n
 * @return {number[]}
 */

var countBits = function(n) {
    return [...Array(n+1).keys()].map(function(dec) { return (dec >>> 0).toString(2).split("1").length-1})
};


// Better Solution
var countBits = function(n) {
    let arr = [...Array(n+1).keys()], offset = 1;
    for (let index = 1; index < n+1; ++index){
        if (offset*2 == index) offset *= 2;
        arr[index] = arr[index-offset]+1;
    }
    return arr
};
