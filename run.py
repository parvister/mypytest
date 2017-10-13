from packy.arithmetic.complex import LinearEquation, QuadraticEquation
import logging
from time import sleep

FORMAT = '%(levelname)s %(asctime)s %(module)s %(funcName)s %(process)d %(pathname)s %(created)s %(relativeCreated)s %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%Y-%m-%d_%H:%M:%S')
log = logging.getLogger()

def run_linear_equation(m, b):
    eq = LinearEquation(m, b)
    print("linear euqation: y = %dx + %d" % (m, b))
    print("y(x=5) = %d" % eq.get_y(5))


def run_quadratic_equation(a, b, c):
    eq = QuadraticEquation(a, b, c)
    print("linear euqation: y = %dx^2 + %dx + %d" % (a, b, c))
    print("y(x=5) = %d" % eq.get_y(5))


def main():
    log.warning("this is good")

    run_linear_equation(4, 5)
    run_quadratic_equation(3, 10, -5)

    sleep(2.001)
    log.warning("this is good")


if __name__ == '__main__':
    main()