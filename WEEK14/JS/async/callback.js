'use strict'

// JavaScript is synchronous
// 호이스팅이 된 이후부터 코드가 우리가 작성한 순서에 맞춰서 하나하나씩 동기적으로 시작된다.

console.log('1'); // 1 출력
setTimeout(() => { // 바로 실행 되는 것이 아님 단지 콜백함수를 브라우저로 전달 해줄뿐. 브라우저야 1초 뒤에 실행시켜줘라.
    console.log('2');
}, 1000);
console.log('3'); // 3을 두번째로 출력

// synchronous callback
function printImmediately(print) {
    print();
}
printImmediately(() => console.log('hello'));

// Asynchronous callback
function printWithDelay(print, timeout) {
    setTimeout(print, timeout);
}
printWithDelay(()=>console.log('async callback'), 2000);

//callback hell example
class UserStorage {
    loginUser(id, password, onSuccess, onError) {
        setTimeout(() => {
            if (
            (id === 'ellie' && password === 'dream') ||
            (id === 'coder' && password === 'academy')
            ) {
                onSuccess(id);
            } else {
                onError(new Error('not found'));
            }
        }, 2000);
    }

    getRoles(user, onSuccess, onError) {
        setTimeout(() => {
            if (user === 'ellie') {
                onSuccess({name: 'ellie', role: 'admin'});
            } else {
                onError(new Error('no access'));
            }
        }, 1000);
    }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
    id,
    password,
    user => {
        userStorage.getRoles(
            user,
            userWithRole => {
                alert(
                    `Hello ${userWithRole.name}, you have a ${userWithRole.role} role`
                );
            },
            error => {
                console.log(error);
            }
        );
    },
    error => {
        console.log(error);
    }
);