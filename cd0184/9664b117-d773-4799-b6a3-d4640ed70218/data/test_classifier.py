
# Imports classifier function for using pretrained CNN to classify images
from classifier import classifier

# Defines a dog test image from pet_images folder
test_image = "pet_images/Collie_03797.jpg"

# Defines a model architecture to be used for classification
# NOTE: this function only works for model architectures:
#      'vgg', 'alexnet', 'resnet'
model = "vgg"

# Demonstrates classifier() functions usage
# NOTE: image_classication is a text string - It contains mixed case(both lower
# and upper case letter) image labels that can be separated by commas when a
# label has more than one word that can describe it.
image_classification = classifier(test_image, model)

# prints result from running classifier() function
print("\nResults from test_classifier.py\nImage:", test_image, "using model:",
      model, "was classified as a:", image_classification)
