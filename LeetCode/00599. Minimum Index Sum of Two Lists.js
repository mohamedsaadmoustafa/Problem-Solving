/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let a = []
    let mn = list1.length + list2.length-2;
    for(let x=0; x < list1.length; x++){
        y = list2.indexOf(list1[x])
        if (y === -1) y = list2.length-1
        if (x + y < mn && list1[x]===list2[y] ) 
        {
            a = []
            mn = x + y;
            a.push(list1[x]);
        }
        else if (x + y === mn)
        {
            a.push(list1[x]);
        }
    }
    return a;
};


// A way better solution
/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let a = []
    let mn = list1.length + list2.length; 
    for(let x=0; x < mn; x++){
        for(let y=0; y < x+1; y++){
            if (y<list1.length && x-y<list2.length && list1[y]==list2[x-y]){
                a.push(list1[y]);
            }
        }
        if (a.length > 0) break
    }
    return a;
};
