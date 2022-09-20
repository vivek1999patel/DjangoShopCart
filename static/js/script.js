const options={indicators:false}
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, options);
  });


  var tabOptions ={swipeable:true}
  el= document.querySelector('.tabs')
  var instance = M.Tabs.init(el, tabOptions);
  

