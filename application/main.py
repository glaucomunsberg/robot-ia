from tests.test_synapses import TestSynapses

testSynapses = TestSynapses()


def test():
    """ Test the synapses of sensors
    """
    testSynapses.test()


print(f"name {__name__}")
if __name__ == "__main__":
    test()
