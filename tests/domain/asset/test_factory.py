import unittest
from domain.asset.factory import AssetFactory


class TestAssetFactory(unittest.TestCase):
    def test_make_new(self):
        factory = AssetFactory()
        asset = factory.make_new('MSFT')
        self.assertEqual(asset.ticker, 'MSFT')
        self.assertEqual(asset.units, 0)
        self.assertEqual(asset.country, 'United States')
        self.assertEqual(asset.name, 'Microsoft Corporation')


if __name__ == "__main__":
    unittest.main()
