// 연산자
// 할당 연산자
let c = 0
c += 10
console.log(c)
c-=3

c *= 10

c++
console.log(c)
c--
console.log(c)
++c
console.log(c)
--c
console.log(c)

// 비교 연산자

3>2
// true
3<2
// false


'A'<'B'
// true
'A'<'a'
// true
'Z'<'a'
// true
'가'<'나'
// true

// 동등 연산자
// ==
// 가급적 지양

// 일치 연산자
// ===

const a = 1
const b = '1'
console.log(a == b)
console.log(a == Number(b))

console.log(8 * null)

// null : 0의 의미

console.log('5'-1)
// 숫자 4 나온다

console.log('5'+1)
// 문자열 51 나온다

console.log('five' * 2)
// 문자열은 NaN

console.log(a === b)
// false

console.log(a === Number(b))
// true

true && true
// true

true && false
// false

1 && 0
// 0
0 && 1
// 0
4 && 7
// 7

false || true
// true
false || false
// false
1 || 0
// 1
0 || 1
// 1
4 || 7
// 4

!true
// fasle

!false
// true


true?1:2
// 1
// 표현식 ? 참일때 값 : 거짓일때 값
false?1:2
// 2

const result = Math.PI > 4? 'Yep':"Nope"
console.log(result)

const result2 = Math.PI < 4? 'Yep':"Nope"
console.log(result2)

// (ans > new)? ans:new 
// 이런 것에 활용


