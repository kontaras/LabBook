import subprocess
import sys
import os

code_files = "unit_tests regression_tests integ_tests ./app.py"


def update_pip():
    call("pip install --upgrade pip")


def install_requirements_runtime():
    call("pip install -r requirements.txt")


def install_requirements_dev():
    call("pip install -r requirements-dev.txt")


def depends(*trgs):
    def run():
        for target in trgs:
            execute_target(target)
    return run


def call(command):
    cmd = get_flag("PYTHON_HOME") + command
    subprocess.check_call(cmd, shell=True)


def execute_target(target):
    targets[target]()


def flake():
    call("flake8 " + code_files)


def lint():
    call("pylint " + code_files +
         " --disable=no-member --disable=too-many-locals")


def run_test(test_dir, tag):
    def run():
        test_cmd = "pytest app.py "
        if get_flag("COVERAGE") != "":
            call("codecov -f coverage.xml -F " + tag)
            test_cmd += " --cov-report xml --cov=app "
        call(test_cmd + " -s " + test_dir)
    return run


def get_flag(flag):
    return os.environ.get("BUILD_FLAG_" + flag, "")


targets = {
    "updatepip": update_pip,
    "reqs-dev": install_requirements_dev,
    "reqs-run": install_requirements_runtime,
    "reqs": depends("updatepip", "reqs-dev", "reqs-run"),
    "flake": flake,
    "lint": lint,
    "quality": depends("flake", "lint"),
    "test_unit": run_test("unit_tests", "unittests"),
    "test_reg": run_test("regression_tests", "regresiontests"),
    "test_integ": run_test("integ_tests", "integrationtests"),
    "test": depends("test_unit", "test_reg", "test_integ")
}

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        execute_target(arg)
