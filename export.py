from ultralytics import YOLO

# Load a model
# model = YOLO("yolo11s.pt")  # load an official model
model = YOLO("best.pt")  # load a custom trained model

# Export the model
# 'cpu' 
model.export(format='ncnn', device='cpu', imgsz=640, batch=1) 
