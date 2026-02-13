import unittest
from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector_function(self):
        # Test case 1
        result = emotion_detection.emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")
        # Test case 2
        result = emotion_detection.emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")
        # Test case 3
        result = emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")
        # Test case 4
        result = emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")
        # Test case 5
        result = emotion_detection.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()