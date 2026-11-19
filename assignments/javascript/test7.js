// Create a Student class with name, marks, and a method to display student details.

// class student {
//   constructor(n, m) {
//     this.name = n;
//     this.mark = m;
//   }
//   display() {
//     console.log("studentname:", this.name);
//     console.log("studentmarks:", this.mark);
//   }
// }
// let s1 = new student("vikky", 90);
// // s1.display()

// // Create a private balance property with deposit and withdraw methods.
// class atm {
//   #balance;
//   constructor(b, d, w) {
//     this.#balance = b;
//   }
//   deposite() {
//     console.log("deposite");
//   }
//   withdraw() {
//     console.log("enter the amount");
//   }
// }
// let ac = new atm(5000);
// ac.deposite();
// ac.withdraw();

// Create an Employee parent class and Developer child class.
class Employee {
  display() {
    console.log(parent);
  }
}
class developer extends Employee() {
  dev() {
    console.log("print");
  }
}
let e = new developer();
e.display();
