# -*- coding:utf-8 -*-
class UrlMiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.path)
        print('process----')
        if request.path not in [
            '/user/regiser/',
            '/user/register_handle/',
            '/user/login/',
            '/user/register_username/',
            '/user/login_check/',
            '/user/logout/',
        ]:
            request.session['url_path'] = request.get_full_path()
