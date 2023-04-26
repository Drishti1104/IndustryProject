
    const hello = "hello";
    console.log(hello)
    var ctx1 = document.getElementById("bar1").getContext('2d');
    var myChart1 = new Chart(ctx1, {
      type: 'bar',
        data: {
            labels: ["Excellent", "Good", "Average", "Poor"],
            datasets: [{
                label: 'Overall how would you rate your physical health?',
                data: [3, 5, 4, 3],
                backgroundColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(75, 192, 192, 1)'
                ],
                borderColor: [
                  'rgba(255, 99, 132, 3)',
                  'rgba(54, 162, 235, 3)',
                  'rgba(153, 102, 255, 3)',
                  'rgba(75, 192, 192, 3)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
  
    var ctx2 = document.getElementById("bar2").getContext('2d');
    var myChart2 = new Chart(ctx2, {
      type: 'bar',
        data: {
            labels: ["Very often", "Somewhat often", "Not so often", "Not at all"],
            datasets: [{
                label: 'Have you felt particularly low or down for more than 2 weeks in a row?',
                data: [1, 4, 7, 3],
                backgroundColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(75, 192, 192, 1)'
                ],
                borderColor: [
                  'rgba(255, 99, 132, 3)',
                  'rgba(54, 162, 235, 3)',
                  'rgba(153, 102, 255, 3)',
                  'rgba(75, 192, 192, 3)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
  
    var ctx3 = document.getElementById("bar3").getContext('2d');
    var myChart3 = new Chart(ctx3, {
      type: 'bar',
        data: {
            labels: ["Single", "Married", "Divorced", "Widowed", "Separated"],
            datasets: [{
                label: 'What is your relationship status? ',
                data: [2, 5, 4, 2, 2],
                backgroundColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(255, 205, 86, 1)'
                ],
                borderColor: [
                  'rgba(255, 99, 132, 3)',
                  'rgba(54, 162, 235, 3)',
                  'rgba(153, 102, 255, 3)',
                  'rgba(75, 192, 192, 3)',
                  'rgb(255, 205, 86, 3)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
  
    var ctx4 = document.getElementById("bar4").getContext('2d');
    var myChart4 = new Chart(ctx4, {
      type: 'bar',
        data: {
            labels: ["Less than 5", "5 to 7", "7 to 9", "More than 9"],
            datasets: [{
                label: 'How many hours do you sleep per day?',
                data: [4, 5, 4, 2],
                backgroundColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(75, 192, 192, 1)'
                ],
                borderColor: [
                  'rgba(255, 99, 132, 3)',
                  'rgba(54, 162, 235, 3)',
                  'rgba(153, 102, 255, 3)',
                  'rgba(75, 192, 192, 3)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });


// (function(){
//     console.log("hello")
// // "use strict";
//     const labels = [
//       'Excellent',
//       'Good',
//       'Average',
//       'Poor'
//     ];
  
//     const data = {
//       labels: labels,
//       datasets: [{
//         label: 'Q1',
//         backgroundColor: [
//             'rgba(255, 99, 132, 0.2)',
//             'rgba(54, 162, 235, 0.2)',
//             'rgba(153, 102, 255, 0.2)',
//             'rgba(75, 192, 192, 0.2)'
//         ],
//         borderColor: [
//             'rgb(255, 99, 132)',
//             'rgb(54, 162, 235)',
//             'rgb(153, 102, 255)',
//             'rgba(75, 192, 192, 0.2)',
//         ],
//         borderWidth: 1,
//         data: ['{{q1_excellent}}', '{{q1_good}}', '{{q1_avg}}', '{{q1_poor}}'],
//       }]
//     };
//     const config2 = {
//         type: 'bar',
//         data: data,
//         maintainAspectRatio: false,
//         options: {
//             scales: {
//                 y: {
//                     beginAtZero: true
//                 }
//             }
//         },
//     };

//     const line = new Chart(
//         document.getElementById('line'),
//         config2
//     ); 
// });