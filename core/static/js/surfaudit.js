$('td').filter(function() {
  return $(this).text() == 'fair';
}).css("background-color", "#00cc00").css("color", "white").next().css("background-color", "#00cc00").css("color", "white");

$('td').filter(function() {
  return $(this).text() == 'poor to fair';
}).css("background-color", "#3399ff").css("color", "white").next().css("background-color", "#3399ff").css("color", "white");

$('td').filter(function() {
  return $(this).text() == 'False';
}).css("background-color", "red").css("color", "white");


$('td').filter(function() {
  return $(this).text() == 'True';
}).css("background-color", "purple").css("color", "white");