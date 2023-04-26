/**
* Template Name: Medilab - v4.7.1
* Template URL: https://bootstrapmade.com/medilab-free-medical-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {

  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  let selectTopbar = select('#topbar')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.add('topbar-scrolled')
        }
      } else {
        selectHeader.classList.remove('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.remove('topbar-scrolled')
        }
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Initiate glightbox 
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Initiate Gallery Lightbox 
   */
  const galelryLightbox = GLightbox({
    selector: '.galelry-lightbox'
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 2,
        spaceBetween: 20
      }
    }
  });

  // Chart function / evaluation measures
  // const hello = "hello";
  // console.log("hello")
  // var ctx1 = document.getElementById("bar1").getContext('2d');
  // var myChart1 = new Chart(ctx1, {
  //   type: 'bar',
  //     data: {
  //         labels: ["Excellent", "Good", "Average", "Poor"],
  //         datasets: [{
  //             label: 'Overall how would you rate your physical health?',
  //             data: [3, 5, 4, 3],
  //             backgroundColor: [
  //               'rgba(255, 99, 132, 1)',
  //               'rgba(54, 162, 235, 1)',
  //               'rgba(153, 102, 255, 1)',
  //               'rgba(75, 192, 192, 1)'
  //             ],
  //             borderColor: [
  //               'rgba(255, 99, 132, 3)',
  //               'rgba(54, 162, 235, 3)',
  //               'rgba(153, 102, 255, 3)',
  //               'rgba(75, 192, 192, 3)'
  //             ],
  //             borderWidth: 1
  //         }]
  //     },
  //     options: {
  //         scales: {
  //             yAxes: [{
  //                 ticks: {
  //                     beginAtZero:true
  //                 }
  //             }]
  //         }
  //     }
  // });

  // var ctx2 = document.getElementById("bar2").getContext('2d');
  // var myChart2 = new Chart(ctx2, {
  //   type: 'bar',
  //     data: {
  //         labels: ["Very often", "Somewhat often", "Not so often", "Not at all"],
  //         datasets: [{
  //             label: 'Have you felt particularly low or down for more than 2 weeks in a row?',
  //             data: [1, 4, 7, 3],
  //             backgroundColor: [
  //               'rgba(255, 99, 132, 1)',
  //               'rgba(54, 162, 235, 1)',
  //               'rgba(153, 102, 255, 1)',
  //               'rgba(75, 192, 192, 1)'
  //             ],
  //             borderColor: [
  //               'rgba(255, 99, 132, 3)',
  //               'rgba(54, 162, 235, 3)',
  //               'rgba(153, 102, 255, 3)',
  //               'rgba(75, 192, 192, 3)'
  //             ],
  //             borderWidth: 1
  //         }]
  //     },
  //     options: {
  //         scales: {
  //             yAxes: [{
  //                 ticks: {
  //                     beginAtZero:true
  //                 }
  //             }]
  //         }
  //     }
  // });

  // var ctx3 = document.getElementById("bar3").getContext('2d');
  // var myChart3 = new Chart(ctx3, {
  //   type: 'bar',
  //     data: {
  //         labels: ["Single", "Married", "Divorced", "Widowed", "Separated"],
  //         datasets: [{
  //             label: 'What is your relationship status? ',
  //             data: [2, 5, 4, 2, 2],
  //             backgroundColor: [
  //               'rgba(255, 99, 132, 1)',
  //               'rgba(54, 162, 235, 1)',
  //               'rgba(153, 102, 255, 1)',
  //               'rgba(75, 192, 192, 1)',
  //               'rgba(255, 205, 86, 1)'
  //             ],
  //             borderColor: [
  //               'rgba(255, 99, 132, 3)',
  //               'rgba(54, 162, 235, 3)',
  //               'rgba(153, 102, 255, 3)',
  //               'rgba(75, 192, 192, 3)',
  //               'rgb(255, 205, 86, 3)'
  //             ],
  //             borderWidth: 1
  //         }]
  //     },
  //     options: {
  //         scales: {
  //             yAxes: [{
  //                 ticks: {
  //                     beginAtZero:true
  //                 }
  //             }]
  //         }
  //     }
  // });

  // var ctx4 = document.getElementById("bar4").getContext('2d');
  // var myChart4 = new Chart(ctx4, {
  //   type: 'bar',
  //     data: {
  //         labels: ["Less than 5", "5 to 7", "7 to 9", "More than 9"],
  //         datasets: [{
  //             label: 'How many hours do you sleep per day?',
  //             data: [4, 5, 4, 2],
  //             backgroundColor: [
  //               'rgba(255, 99, 132, 1)',
  //               'rgba(54, 162, 235, 1)',
  //               'rgba(153, 102, 255, 1)',
  //               'rgba(75, 192, 192, 1)'
  //             ],
  //             borderColor: [
  //               'rgba(255, 99, 132, 3)',
  //               'rgba(54, 162, 235, 3)',
  //               'rgba(153, 102, 255, 3)',
  //               'rgba(75, 192, 192, 3)'
  //             ],
  //             borderWidth: 1
  //         }]
  //     },
  //     options: {
  //         scales: {
  //             yAxes: [{
  //                 ticks: {
  //                     beginAtZero:true
  //                 }
  //             }]
  //         }
  //     }
  // });

})()

// function validate(){
//   var password = document.getElementById("psw1").value;
//         var confirmPassword = document.getElementById("psw2").value;
//         if (password != confirmPassword) {
//       //document.getElementById("hi").innerHTML="passwords do not match";
//           alert("Passwords do not match."); 
//             //return false;
//         }
//   }

// const labels = [
  //   'Excellent',
  //   'Good',
  //   'Average',
  //   'Poor'
  // ];

  // const data = {
  //     labels: labels,
  //     datasets: [{
  //     label: 'Q1',
  //     backgroundColor: [
  //         'rgba(255, 99, 132, 0.2)',
  //         'rgba(54, 162, 235, 0.2)',
  //         'rgba(153, 102, 255, 0.2)',
  //         'rgba(75, 192, 192, 0.2)'
  //     ],
  //     borderColor: [
  //         'rgb(255, 99, 132, 1)',
  //         'rgb(54, 162, 235, 1)',
  //         'rgb(153, 102, 255, 1)',
  //         'rgba(75, 192, 192, 1)',
  //     ],
  //     borderWidth: 2,
  //     data: ['{{q1_excellent}}', '{{q1_good}}', '{{q1_avg}}', '{{q1_poor}}'],
  //   }]
  // };
  // const config2 = {
  //     type: 'bar',
  //     data: data,
  //     maintainAspectRatio: false,
  //     options: {
  //         scales: {
  //             y: {
  //                 beginAtZero: true
  //             }
  //         }
  //     },
  // };

  // var bar = document.getElementById('bar').getContext('2d');
  // new Chart(bar).Line(riceData);
  // const bar = new Chart(
  //     document.getElementById('bar'),
  //     config2
  // ); 

  // end of evaluation measures