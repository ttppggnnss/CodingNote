let x = 1
console.log(x)
// let x = 3
x = 3
console.log(x)

if (x===3) {
    let x = 2
    console.log(x)
}
console.log(x)

// const myFav
const myFav = 7

// const 로 하면 재정의 안된다
// myFav = 20
// const myFav = 10

console.log(myFav)

if (myFav===7){
    const myFav=20
    console.log(myFav)
}

// ES6 이전에는 변수 선언할 대 var
// var 지양
num = 1
// 이렇게 하면 var 로 선얺사는걸로 인식한다
//  var num = 1
// 과 같은 동작
// var 로 선언한 변수는
// 같은 var 로 재 선언 가능하다


var a = 1
let b = 1
if (a===1){
 var a = 11
 let b = 22

 console.log(a)
 console.log(b)
 }
console.log(a)
// 11
console.log(b)
// 1

// var 사용하면 꼬일 수 있다

// 식별자는 일반적으로 camel case

let dog
let variableNmae

// 배열 선언
// 이름 복수형태
const cats = []

function getPropertyName() {}
// camelCase 활용

// boolean 값으로 반환되는 함수 혹은 변수는 is 앞에 붙여서 활용
let isAvailable = false

// class 는 대문자 시작
// upper Camel Case
// Pascal Case
class User {
    constructor(options){
        this.name = options.name
    }
}
// 생성자로 만들 때
const good = new User({
    name: '김원정'
})

// 대문자 snake case
const API_KEY = '#!WEF$E^%@#'

