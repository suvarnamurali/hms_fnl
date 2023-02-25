$(document).ready(function(){
        
    //-- Click on terms and conditions
    $(".term").click(function(){
        var ctrl = $(this).find("i");
        if (ctrl.hasClass("fa-check-square-o")){
            ctrl.attr("class","fa fa-square-o");
        }else{
            ctrl.attr("class", "fa fa-check-square-o");
        }
    }) 

    $("input").blur(function(){
        if ($(this).val() != ""){
            $(this).parent().css({"color":"black"});
            $(this).css({"border-bottom":"1px solid silver","color":"gray"});                 
        }
    })
    
    //--- CONTINUE ---
    $("form > p > a").click(function(){
        //-- Detect terms and conditions
        var term = false;
        if ($(".term > i").hasClass('fa-check-square-o')){
            term = true;
        }
        
        //-- only example
        var user = {};
        user.name = $("input[name='name']").val();
        user.id = $("input[name='id']").val();
        user.phone = $("input[name='phone']").val();
        user.email = $("input[name='email']").val();
        user.term = term;

        //-- Validator            
        $("input").each(function(e, valor){
            var error = false;
            if ($(this).val() == ""){
                error = true;
            }
            if (error === true){
                //-- with errors
                $(this).parent().css({"color":"red"});
                $(this).css({"border-bottom":"1px solid red"});
            }else{
                //-- without errors
                $(this).parent().css({"color":"black"});
                $(this).css({"border-bottom":"1px solid silver","color":"gray"}); 
            }
        })

        //-- msg example
        $("body").append(JSON.stringify(user) + "<br>");
    })
})