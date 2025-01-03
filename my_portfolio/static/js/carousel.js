// carousel.js
$(document).ready(function () {
  var carouselImages = $("#carousel img");
  var currentIndex = 0;

  function showImage(index) {
    carouselImages.hide();
    carouselImages.eq(index).show();
  }

  showImage(currentIndex);

  setInterval(function () {
    currentIndex = (currentIndex + 1) % carouselImages.length;
    showImage(currentIndex);
  }, 3000); // Change image every 3 seconds
});
