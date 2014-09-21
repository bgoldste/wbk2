$('#container').isotope({
  getSortData : {
  
    WVHT : function ( $elem ) {
      return $elem.find('.WVHT').text();
    }
  }
});



$('#container').isotope({ 
  sortBy : 'WVHT',
  sortAscending : false
});