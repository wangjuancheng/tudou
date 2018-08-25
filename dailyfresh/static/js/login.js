$(function(){

//    error_name = false;
//    error_pwd = false;
//


     $(".name_input").blur(function(){
            if($(".name_input").val().length == 0){
                $(".user_error").html("请输入用户名").show();
                error_name = true;
            }else{
                $(".user_error").html("请输入用户名").hide();
                error_name = false;
            }
	});

    $(".pass_input").blur(function(){
        if($(".pass_input").val().length == 0){
            $(".pwd_error").html("请填写密码").show();
            error_pwd = true;
        }else{
            $(".pwd_error").html("请填写密码").hide();
            error_pwd = false;
        }
     });

//        error_name = 1;
//    if( {{error_name}} == 1){
//        $(".user_error").html("用户名错误").show();
//        }

//    if({{error_pwd}} == 1){
//        $(".pwd_error").html("密码错误").show();
//    }

//    $(".input_submit").click(function(){
//        if(error_name = true && error_pwd = true){
//            return false;
//        }else{
//            return true;
//        }
//
//    });

});