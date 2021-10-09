from pylama.main import check_path, parse_options


def lint():
    options = parse_options(["../"])
    errors = check_path(options, rootdir=".")
    if errors:
        raise BaseException(*errors)
