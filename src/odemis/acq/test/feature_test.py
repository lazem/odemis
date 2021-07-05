import json
import logging
import unittest

from odemis import model
from odemis.acq.feature import CryoFeature, FeaturesEncoder, FeaturesDecoder

logging.getLogger().setLevel(logging.DEBUG)


class TestFeatuerEncoderDecoder(unittest.TestCase):
    """
    Test the json encoder and decoder of the CryoFeature class
    """
    test_str = """{"feature_list": [{"name": "Feature-1", "pos": [0, 0, 0], "milling_angle": 10.0, "status": "Active"}, {"name": "Feature-2", "pos": [0.001, 0.001, 0.002], "milling_angle": 20.0, "status": "Active"}]}"""

    def test_feature_encoder(self):
        feature1 = CryoFeature("Feature-1", 0, 0, 0, 10)
        feature2 = CryoFeature("Feature-2", 1e-3, 1e-3, 2e-3, 20)

        features = model.ListVA([feature1, feature2])
        json_str = json.dumps(features, cls=FeaturesEncoder)
        self.assertEqual(json_str, self.test_str)

    def test_feature_decoder(self):
        features = json.loads(self.test_str, cls=FeaturesDecoder)
        self.assertTrue(len(features), 2)
        self.assertTrue(features[0].name.value, "Feature-1")
        self.assertTrue(features[0].status.value, "Active")
        self.assertTrue(features[1].pos.value, (1e-3, 1e-3, 2e-3))
        self.assertTrue(features[1].milling_angle.value, 20.0)