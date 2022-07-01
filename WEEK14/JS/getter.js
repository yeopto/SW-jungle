const number = {
    a: 1,
    b: 2,
    get sum() {
        console.log('sum 함수가 실행 됩니다');
        return this.a + this.b;
    }
};

console.log(number.sum);
number.b = 5;
console.log(number.sum);