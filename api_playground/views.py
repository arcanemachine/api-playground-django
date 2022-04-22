from django.http import HttpResponse


def project_root(request):
    return HttpResponse("""
<html lang="en">
  <head>
  <meta charset="utf-8">
    <title></title>
  </head>
  <body>

<h1 style="text-align: center">API Playground</h1>

<p>
  <a href="/api">View the API</a>
</p>

  </body>
</html>""")
