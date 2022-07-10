'use strict';

// promise is a javascript object for asynchronous operation.

// 1. producer
// When new Promise is created, the executor runs automatically.
const promise = new Promise((resolve, reject) => {
    // doing some heavy work (network, read files)
    console.log('doing someting...');
    setTimeout(() => {
        resolve('ellie');
        // reject(new Error('no network'));
    }, 2000);
});

// 2. Consumers: then, catch, finally
promise
    .then((value) => { // then은 결국 똑같은 promise를 리턴함.
        console.log(value);
    })
    .catch(error => { // 그 return 된 promise에 catch를 다시 호출할 수 있는 것. 이것이 체이닝
        console.log(error);
    })
    .finally(() => { // then 이든 catch든 그 이후에 또 뭘 실행하고 싶을 때 쓰는 finally
        console.log('finally');
    });

// 3. chaning and handling
const getHen = () => 
    new Promise((resolve, reject) => {
        setTimeout(() => resolve('닭'), 1000);
    });
const getEgg = hen => 
    new Promise((resolve, reject) => {
        // setTimeout(() => resolve(`${hen} => 알`), 1000);
        setTimeout(() => reject(new Error(`error! ${hen} => 알`)), 1000);
    });
const cook = egg => 
    new Promise((resolve, reject) => {
        setTimeout(() => resolve(`${egg} => 후라이`), 1000);
    });

getHen()
    .then(getEgg) // hen => getEgg(hen) 와 같음
    .catch(error => {
        return '빵';
    })
    .then(egg => cook(egg))
    .then(meal => console.log(meal))
    .catch(console.log);

