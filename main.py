def app(environ, start_response):
        data = b"Hello, KONDI CODE !\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
