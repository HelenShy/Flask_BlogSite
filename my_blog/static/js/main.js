document.addEventListener('DOMContentLoaded', function() {
    showPopUpBox("flashes")
  }, false);

 function showPopUpBox(id) {
       var e = document.getElementById(id);
       e.classList.add("show");
       setTimeout(function() {
         document.getElementById( "flashes" ).classList.remove('show');
         document.getElementById( "flashes" ).classList.add('hide');
       }, 5000);
    };



