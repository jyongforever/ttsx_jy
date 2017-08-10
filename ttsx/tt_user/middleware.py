# -*- coding:utf-8 -*-
class UrlMiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(request.path)
        # print('process----')
        # 判断不在以下URL列表中的，记住urlsession里
        if request.path not in [
            '/user/register/',
            '/user/register_handle/',
            '/user/login/',
            '/user/register_username/',
            '/user/login_check/',
            '/user/logout/',
            '/user/islogin/',
        ]:
            request.session['url_path'] = request.get_full_path()
            print(request.session['url_path'])
