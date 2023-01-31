/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let count = 0; sum = 0;
    for (const x of s){
        if (x=='L') ++count;
        else --count;
        if (count==0) ++sum
    }
    return sum;
};

// OR
var balancedStringSplit = function(s) {
    let count = 0; sum = 0;
    for (const x of s){
        count += (x=='L' ? -1 : 1);
        if (count==0) ++sum
    }
    return sum;
};
