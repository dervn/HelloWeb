点击run.bat运行web.py的内置server

ngnix

url.rewrite-once = (
“^/favicon.ico$” => “/static/favicon.ico”,
“^/static/(.*)$” => “/static/$1″,
“^/(.*)$” => “/code.py/$1″,
)

