import compileall


def py2pyc(path="."):
    compileall.compile_dir(path, legacy=True)


if __name__ == '__main__':
    py2pyc()
