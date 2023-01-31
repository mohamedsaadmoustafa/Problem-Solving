var heightChecker = function(heights) {
    const sorted = [...heights].sort((a,b) => a-b);
    let count = 0;

    for (let index in sorted) {
        if (heights[index] !== sorted[index]) {
            count++;
        }
    }
    return count
}
