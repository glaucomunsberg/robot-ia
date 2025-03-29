from tests.synapses import TestSynapses

testSynapses = TestSynapses()


def test():
    """ Test the synapses of sensors
    """
    testSynapses.test()
    testSynapses.test_motor()


if __name__ == "__main__":
    test()
