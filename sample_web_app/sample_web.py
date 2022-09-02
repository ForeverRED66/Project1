import time
import random
from flask import Flask
from flask import request
from prometheus_flask_exporter import PrometheusMetrics

sample = Flask (__name__)

PrometheusMetrics(sample)
endpoints = ("one", "two", "three", "four", "five", "error")

@sample.route("/")
def main():
    return "Hello, World!" + request.remote_addr + "\n"

@sample.route("/one")
def first_route():
    time.sleep(random.random() * 0.2)
    return "test ok"

@sample.route("/two")
def the_second():
    time.sleep(random.random() * 0.4)
    return "test ok"

@sample.route("/three")
def test_3rd():
    time.sleep(random.random() * 0.6)
    return "test ok"

@sample.route("/four")
def fourth_one():
    time.sleep(random.random() * 0.8)
    return "test ok"


@sample.route("/error")
def oops():
    return "test error", 500

if __name__ == "__main__":
    sample.run(host = "0.0.0.0", port=8080)
