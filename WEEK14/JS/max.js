function max(...rest) {
    return rest.reduce(
        (a, b) => (a < b ? b : a), 
        rest[0]
    );
}
const result = max(1, 2, 3, 4, 10, 5, 6, 7);
console.log(result);