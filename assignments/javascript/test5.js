// 1.Scenario: A customer visits a movie booking website and books a movie ticket.
// Perform the following operations in sequence using Asynchronous JavaScript :
// Operation:
// Open movie booking website - 2 sec
// Search for a movie - 3 sec
// Select a movie - 1 sec
// Check available seats - 2 sec
// Select seats - 1 sec
// Process ticket booking - 3 sec
// Watch movie (simulate) - 5 sec
// Submit movie review - 1 sec
// Return to homepage - 5 sec

// function movieweb(callback) {
//   setTimeout(() => {
//     console.log("movie tickets booking website ");
//     callback();
//   }, 2000);
// }

// function moviesearch(callback) {
//   setTimeout(() => {
//     console.log("search the movie");
//     callback();
//   }, 1000);
// }

// function avabileseats(callback) {
//   setTimeout(() => {
//     console.log("seat avabile");
//     callback();
//   }, 2000);
// }

// function slectedseats(callback) {
//   setTimeout(() => {
//     console.log("select the  seats");
//     callback();
//   }, 1000);
// }

// // Process ticket booking - 3 sec
// function ticketbooking(callback) {
//   setTimeout(() => {
//     console.log("processing the ticket booking");
//     callback();
//   }, 3000);
// }

// // Watch movie (simulate) - 5 sec
// function watchmovie(callback) {
//   setTimeout(() => {
//     console.log("watch the movie");
//     callback();
//   }, 5000);
// }

// // Submit movie review - 1 sec
// function review(callback) {
//   setTimeout(() => {
//     console.log("submit the review");
//     callback();
//   }, 1000);
// }

// // Return to homepage - 5 sec
// function homepage() {
//   setTimeout((callback) => {
//     console.log("return to homepage");
//   }, 5000);
// }

// movieweb(() => {
//   moviesearch(() => {
//     avabileseats(() => {
//       slectedseats(() => {
//         ticketbooking(() => {
//           watchmovie(() => {
//             review(() => {
//               homepage(() => {});
//             });
//           });
//         });
//       });
//     });
//   });
// });

// 2.A customer visits an online shopping website, searches for a mobile phone, purchases it, and tracks the order.
// Perform the following operations in sequence using Asynchronous JavaScript:
// Operation:
// 1. Open shopping website – 2 sec
// 2. Search for a mobile phone – 3 sec
// 3. Display product details – 2 sec
// 4. Select a mobile phone – 1 sec
// 5. Check product availability – 2 sec
// 6. Add product to cart – 1 sec
// 7. Apply discount coupon – 2 sec
// 8. Process payment – 4 sec
// 9. Generate order ID – 2 sec
// 10. Send order confirmation – 3 sec
// 11. Track order status – 5 sec
// 12. Return to homepage – 2 sec

// 1. Open shopping website – 2 sec
function shoppingwebsite(callback) {
  setTimeout(() => {
    console.log("open shopping website");
    callback();
  }, 2000);
}

// 2. Search for a mobile phone – 3 sec
function serachmobile(callback) {
  setTimeout(() => {
    console.log("search for mobile phone");
    callback();
  }, 3000);
}

// 3. Display product details – 2 sec

function productdetail(callback) {
  setTimeout(() => {
    console.log("display product details");
    callback();
  }, 2000);
}
// 4. Select a mobile phone – 1 sec
function selectmobile(callback) {
  setTimeout(() => {
    console.log("select mobile phone");
    callback();
  }, 1000);
}
// 5. Check product availability – 2 sec
function checkproduct(callback) {
  setTimeout(() => {
    console.log("check product availability");
    callback();
  }, 2000);
}
// 6. Add product to cart – 1 sec
function cartproduct(callback) {
  setTimeout(() => {
    console.log("add product to cart");
    callback();
  }, 1000);
}
// 7. Apply discount coupon – 2
function applydiscount(callback) {
  setTimeout(() => {
    console.log("apply discount coupon");
    callback();
  }, 2000);
}

// 8. Process payment – 4 sec
function payment(callback) {
  setTimeout(() => {
    console.log("process payment");
    callback();
  }, 4000);
}
// 9. Generate order ID – 2 sec
function generate(callback) {
  setTimeout(() => {
    console.log("generate order id");
    callback();
  }, 2000);
}
// 10. Send order confirmation – 3 sec
function sendorders(callback) {
  setTimeout(() => {
    console.log("send order confirmation");
    callback;
  }, 3000);
}
// 11. Track order status – 5 sec
function trackorder(callback) {
  setTimeout(() => {
    console.log("track the order status");
    callback();
  }, 5000);
}
// 12. Return to homepage – 2 sec
function home() {
  setTimeout(() => {
    console.log("reeturn to home page");
  }, 2000);
}

shoppingwebsite(() => {
  serachmobile(() => {
    productdetail(() => {
      selectmobile(() => {
        checkproduct(() => {
          cartproduct(() => {
            applydiscount(() => {
              payment(() => {
                generate(() => {
                  sendorders(() => {
                     trackorder(() => {
                       home(() => {});
                    });
                  
                  });
                });
              });
            });
          });
        });
      });
    });
  });
});
