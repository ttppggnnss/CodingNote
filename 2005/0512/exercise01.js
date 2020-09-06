// 타입

const a = 13
const b = -5
const c = 3.14
const d = 2.009e9
const e = Infinity
const f = -Infinity
const g = NaN

console.log(a,b,c,d,e,f,g)

typeof(g)

const sentence1 = 'hlelo'
const sentence2 = "hi"

console.log(sentence1)
console.log(sentence2)

const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName

console.log(fullName)

// const word = "안녕
// 하세요"
// 줄바꿈은 허용되지 않는다

const word1 = "안녕 \n하세요"
// escape sequence 활용하면 가능하다
console.log(word1)

const word2 = `안녕들
하세요`
// back tik ` 으로 는 개행 가능
console.log(word2)

const age = 32
const message = `원정님은 사실 $${age}살입니다.`
console.log(message)

// boolean 값 
// 소문자
true
false

let abc
// undefined
console.log(abc)
// undefined

let def = null
// undefined
// 개발자들의 의도적으로 값 없음을 보여주는 것

console.log(def)
// null
// undefined

typeof null
// object
typeof undefined
// undefined

// 연산자

// 할당 연산자
