function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj === undefined || obj === null || classFunction === undefined) return false
    while (obj !== null) {
        if (obj.constructor === classFunction) return true
        obj = Object.getPrototypeOf(obj);
    }
    return false;
};
