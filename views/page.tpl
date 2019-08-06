<!DOCTYPE html>
<html>
    <head>
        <title>{{path}}</title>
        <meta charset="utf-8" />
        <script>
            if(window.location.pathname != "/{{path}}") {
                history.replaceState("", "", "/{{path}}");
                if("{{offset}}" !== "") {
                    window.location = "#{{offset}}"
                }
            }
        </script>
    </head>
    <body>
        {{!breadcrumb}}

        {{!subpages}}

        {{!contents}}
    </body>
</html>