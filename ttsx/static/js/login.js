

































// $(function () {
//     // var error_uname = false;
//     // var error_upwd = false;
//     // 标记错误状态，初始为false，没有错误
//     var error_info = false;
//     // 定义空对象，用来存储数据
//     var oList = null;
//
//     // 从视图函数获取包含数据库用户信息的JsonResponse对象
//     $.get('/user/login_userinfo/',function (data) {
//         // 通过key'list'获取列表数据赋值给oList
//         oList = data.list;
//     })
//             // 添加失去焦点事件
//             $('.name_input').blur(function () {
//                 // 循环遍历oList，判断输入框中用户名和数据库中用户名是否一致
//                 $.each(oList,function (n,user) {
//                     var uname = user[0];
//                     var name_input = $('.name_input').val();
//                     if(uname==name_input)
//                 {
//                     // error_uname=false;
//                     $('.user_error').hide();
//                     return false;
//                 }
//                 else{
//                     // error_uname=true;
//                     $('.user_error').show();
//                     $('.pwd_error').hide();
//                     $('.pass_input').prop('value','')
//                     return true;
//                 }
//
//                 })
//
//             })
//
//             $('.pass_input').blur(function () {
//                 $.each(oList,function (n,user) {
//                     var upwd = user[1];
//                     var sha = hex_sha1($('.pass_input').val());
//                     if(upwd==sha)
//                 {
//                     // error_upwd=false;
//                     $('.pwd_error').hide();
//                     return false;
//                 }
//                 else{
//                     // error_upwd=true;
//                     $('.pwd_error').show();
//                     return true;
//                 }
//
//                 })
//             })
//
//
//             $('#reg_form').submit(function () {
//
//                 $.each(oList,function (n,user) {
//                 var uname = user[0];
//                 var name_input = $('.name_input').val();
//                 var upwd = user[1];
//                 var sha = hex_sha1($('.pass_input').val());
//                 if(uname==name_input && upwd==sha)
//                 {
//                     error_info = false;
//                     return false;
//                 }
//                 else{
//                     error_info = true;
//                     return true;
//                 }
//  })
//
//                 if(error_info==false)
//                 {
//                     return true;
//                 }
//                 else
//                 {
//                     return false;
//                 }
//             })
//
//
// })