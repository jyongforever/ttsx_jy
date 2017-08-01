$(function () {
    // var error_uname = false;
    // var error_upwd = false;
    var error_info = false;
    var oList = null;


    $.get('/user/login_userinfo/',function (data) {
        oList = data.list;
    })

            $('.name_input').blur(function () {

                $.each(oList,function (n,user) {
                    var uname = user[0];
                    var name_input = $('.name_input').val();
                    if(uname==name_input)
                {
                    // error_uname=false;
                    $('.user_error').hide();
                    return false;
                }
                else{
                    // error_uname=true;
                    $('.user_error').show();
                    return true;
                }

                })

            })

            $('.pass_input').blur(function () {
                $.each(oList,function (n,user) {
                    var upwd = user[1];
                    var sha = hex_sha1($('.pass_input').val());
                    if(upwd==sha)
                {
                    // error_upwd=false;
                    $('.pwd_error').hide();
                    return false;
                }
                else{
                    // error_upwd=true;
                    $('.pwd_error').show();
                    return true;
                }

                })
            })


            $('#reg_form').submit(function () {

                $.each(oList,function (n,user) {
                var uname = user[0];
                var name_input = $('.name_input').val();
                var upwd = user[1];
                var sha = hex_sha1($('.pass_input').val());
                if(uname==name_input && upwd==sha)
                {
                    error_info = false;
                    return false;
                }
                else{
                    error_info = true;
                    return true;
                }
 })

                if(error_info==false)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            })


})