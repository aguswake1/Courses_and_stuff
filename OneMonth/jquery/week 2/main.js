// $("#q1").click(function(){
//     $("#a1").slideToggle("fast", function(){
//         console.log("este segundo parametro es opcional pero checkeamos que funcione bien");
//     });
//     $("#arrow1-down, #arrow1-up").toggleClass("collapse");
// });

$(".question").click(function(){
    //console.log($(this));
    $(this).next().slideToggle("fast")
    $(this).children().toggleClass("collapse");
    $( "#animate" ).animate({
        opacity: 0.50,
        left: "+=50",
        height: "toggle"
    }, 3000, function() {
      // Animation complete.
    });
});
