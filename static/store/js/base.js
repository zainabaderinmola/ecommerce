$(window).on('load', function(){
    $(".preloader").fadeOut("slow");
   });
       $(document).ready(function () {
           $("#orangeModalSubscription").modal('show');
       });
       // popovers Initialization
       $(document).ready(function () {
           $('.dropdown-toggle').dropdown()
       });
       
       $(".hover").mouseleave(
   function () {
   $(this).removeClass("hover");
   }
   );
   
   $(function () {
             $('[data-toggle="tooltip"]').tooltip()
           })
          const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
          function switchTheme(e) {
               if (e.target.checked){
              document.documentElement.setAttribute('data-theme', 'dawn');
              localStorage.setItem('theme', 'dawn');
          }
          else {
              document.documentElement.setAttribute('data-theme', 'dark');
              localStorage.setItem('theme', 'dark');
          }
          }
          toggleSwitch.addEventListener('change', switchTheme, false);
   
          const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
          if (currentTheme){
              document.documentElement.setAttribute('data-theme', currentTheme);
              if (currentTheme === 'dawn'){
                  toggleSwitch.checked = true;
              }
          }
          var scroll = document.getElementById("top")
          window.addEventListener("scroll", function(){
              scroll.style.transform = "rotate("+window.pageYOffset+"deg)";
          })
   