(function($){
		        $(window).load(function(){
		            $(".consoleList").mCustomScrollbar({theme:"minimal",autoHideScrollbar:true});
		        });
		    })(jQuery);


function courseSelected(el)
{
	$('.course').removeClass('active');
	$(el).addClass('active');
	var course = $(el).text();
	$("#console2").html("<span id='title' class='mainTitle'>"+course+"</span>");
	$('.middleConsoleDiv').removeClass('activeDiv');
	$('#courseDiv').addClass('activeDiv');
}
function studentSelected(el)
{
	$('.student').removeClass('active');
	$(el).addClass('active');
}
function examSelected(el)
{
	$('.exam').removeClass('active');
	$(el).addClass('active');
}
function objectiveSelected(el)
{
	$('.objective').removeClass('active');
	$(el).addClass('active');
}