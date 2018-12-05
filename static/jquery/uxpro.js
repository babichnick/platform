

document.addEventListener("DOMContentLoaded", function() {
  var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

  if ("IntersectionObserver" in window) {
    let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          let lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          lazyImage.srcset = lazyImage.dataset.srcset;
          lazyImage.classList.remove("lazy");
          lazyImageObserver.unobserve(lazyImage);
        }
      });
    });

    lazyImages.forEach(function(lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  } else {
    // Possibly fall back to a more compatible method here
  }
});



$(function(){

 $('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
   if (!$(this).next().hasClass('show')) {
     $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
   }
   var $subMenu = $(this).next(".dropdown-menu");
   $subMenu.toggleClass('show');


   $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
     $('.dropdown-submenu .show').removeClass("show");
   });
 

   return false;
 });


});