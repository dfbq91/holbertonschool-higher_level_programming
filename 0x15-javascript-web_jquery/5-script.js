/* Add a <li> tag to UL tag in my_list
when the user does click in Add item div */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
