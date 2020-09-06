
// 선언식
function add(num1, num2){
    return num1+num2
}

add(2,7)

// 표현식

const sub = function(num1, num2){
    return num1-num2
}
sub(7,2)

// 화살표 함수 (익명함수)
const arrow = function(name){
    return `hello! ${name}`
}
// 를 
const arrow2 = (name) => {return `hello ${name}`}
const arrow3 = name => {return `hello ${name}`}

// 표현식 하나인 경우
const arrow4 = name => `hello ${name}`
// arrow4('kim')

square = num => num**2

let noArg = () => 'No args'
