/*Write a JavaScript program to move all zeros to the end of an array
 while maintaining the relative order of non-zero elements.
 Input: let numbers = [0, 5, 0, 3, 8, 0, 2]; Expected Output: [5, 3, 8, 2, 0, 0, 0] */

 /*let numbers=[0,5,0,3,8,0,2];
 for (let i=0; i<numbers.length; i++){
        if (numbers[i]===0){
            numbers.splice(i,1);
            numbers.push(0);
        }
 }
 console.log(numbers);*/


 /*Write a JavaScript program to find the missing number from an array
  containing distinct numbers from 1 to N.
  Input: let numbers = [1, 2, 4, 5, 6]; Expected Output: Missing Number: 3    
  let numbers = [1,2,4,5,6];
  for (let i=1; i<=numbers.length+1; i++){
    if (!numbers.includes(i)){
        console.log("missing number:"+i);
    }
  }*/

 /*   
Write a JavaScript program to identify all duplicate elements in an 
array without using Set. Input: 
let numbers = [4, 2, 7, 2, 8, 4, 9, 7]; Expected Output: Duplicate Elements: [4, 2, 7]*/
/*
let numbers = [4,2,7,2,8,4,9,7];
let duplicates =[];
for (let i=0; i<numbers.length; i++){
    for (let j=i+1; j<numbers.length; j++){
        if (numbers[i]===numbers[j] && !duplicates.includes(numbers[i])){
            duplicates.push(numbers[i]);
        }           
    }}
    console.log("Duplicate Elements: [" + duplicates.join(", ") + "]");*/

/*
Write a JavaScript program to find the maximum difference between two elements where the
 larger element must appear after the smaller element
.Input: let numbers = [7, 1, 5, 3, 6, 4]; Expected Output: Maximum Difference: 5

let numbers = [7, 1, 5, 3, 6, 4];
let maxDiff = -1;
for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
        let diff = numbers[j] - numbers[i];
        if (diff > maxDiff) {
            maxDiff = diff;
        }
    }
}
console.log("Maximum Difference: " + maxDiff);
*/