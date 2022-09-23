
document.addEventListener('DOMContentLoaded', function() {
  const options={}
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, options);
});
// $(document).ready(function(){
//   $('.sidenav').sidenav();
// });
document.addEventListener('DOMContentLoaded', function() {
  let options={indicators:false}
  var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, options);
  });

var tabOptions ={swipeable:true}
var el= document.querySelector('.tabs')
var instance = M.Tabs.init(el, tabOptions);
  
document.addEventListener('DOMContentLoaded', function() {
  options={}
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function() {
  var options={}
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, options);
});
var check = function() {
  let password = document.getElementById('password')
  let confirm_password = document.getElementById('confirm_password')
  if (password.value ==
    confirm_password.value & password.value.length > 0 )  {
    password.classList.add('valid')
    confirm_password.classList.add('valid')
    password.classList.remove('invalid')
    confirm_password.classList.remove('invalid')
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'Passwords are matching';
    document.getElementById('register').disabled=false
  } else {
    password.classList.add('invalid')
    confirm_password.classList.add('invalid')
    password.classList.remove('valid')
    confirm_password.classList.remove('valid')
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'Passwords are not matching';
    document.getElementById('register').disabled=true

  }
}
// Initialise Carousel
const mainCarousel = new Carousel(document.querySelector("#mainCarousel"), {
  Dots: false,
});

// Thumbnails
const thumbCarousel = new Carousel(document.querySelector("#thumbCarousel"), {
  Sync: {
    target: mainCarousel,
    friction: 0,
  },
  Dots: false,
  Navigation: false,
  center: true,
  slidesPerPage: 1,
  infinite: false,
});

// Customize Fancybox
Fancybox.bind('[data-fancybox="gallery"]', {
  Carousel: {
    on: {
      change: (that) => {
        mainCarousel.slideTo(mainCarousel.findPageForSlide(that.page), {
          friction: 0,
        });
      },
    },
  },
});