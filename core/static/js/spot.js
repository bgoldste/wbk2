var $container = $("#container").isotope({
  getSortData: {
    date: '.date',
    WVHT: '.WVHT',
  }
});
// sort items on button click
$('#sorts').on( 'click', 'button', function() {
  var sortByValue = $(this).attr('data-sort-by');
  $container.isotope({ sortBy: sortByValue });
});


$('#filters').on('click', 'button', function(){

	$container.isotope({
  // filter element with numbers greater than 50
  filter: function() {
  	var filterByValue = $(this).attr('data-sort-by');
    // `this` is the item element. Get text of element's .number
    var number = $(this).find('.WVHT').text();
    console.log(number);
    // return true to show, false to hide
    return parseInt( number, 10 ) > filterByValue;
  }
})

});

