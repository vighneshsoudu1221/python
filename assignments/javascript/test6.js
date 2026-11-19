// Create a promise that returns "Task Completed" after 2 seconds.
//  Expected output: Task Completed

// let task = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve("task completeed");
//   }2000);
// });
// task
//   .then((msg) => {
//     console.log(msg);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

// Create a promise that rejects with the message "Invalid Password".
//  Handle the error using .catch(). Expected output: Invalid Password
// let task = new Promise((resolve, reject) => {
//   reject("invalid");
// }).catch((error) => {
//   console.log(error);
// });

// Create a promise that takes a number. - If the number is greater than 10,
//  resolve with "Valid Number". - Otherwise, reject with "Invalid Number".
// let num = 25;
// let task = new Promise((resolve, reject) => {
//   if (num > 10) {
//     resolve("valid number");
//   } else {
//     reject("invalid number");
//   }
// });
// task
//   .then((msg) => {
//     console.log(msg);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

// Create an async function that returns "Hello Students" and print the result using .then().
