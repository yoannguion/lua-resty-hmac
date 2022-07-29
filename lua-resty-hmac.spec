%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.1/resty

Name: lua-resty-hmac
Summary: HMAC functions for ngx_lua and LuaJIT
Version: 1.0
Release: 1
URL: https://github.com/yoannguion/lua-resty-hmac
License: BSD license
Requires: compat-lua-libs
Provides: HMAC functions for ngx_lua and LuaJIT
BuildArch: noarch

%description
HMAC functions for ngx_lua and LuaJIT


%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/hmac.lua $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/hmac.lua

%changelog
* Fri Jul 29 2022 Yoann GUION <yoann.guion@gmail.com> - 1.0-1
- Initial release 1.0
