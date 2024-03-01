from ultralytics import YOLO

class YOLOModel:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(YOLOModel, cls).__new__(cls)
            # Load the YOLO model here
            # cls._instance.model = YOLO('./trained_models/best.pt')  

        return cls._instance

    def predict(self, image):
        # Perform YOLO inference here using self.model
        results = self.model(image,conf=0.5)  # Replace 'image' with the actual input image
        return results
    
    
