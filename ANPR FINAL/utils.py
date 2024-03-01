def get_license_plate_coordinates(results):
        max_confidence = 0
        best_coordinates = None
        class_names = ["car","license_plate","bike","bus"]

        for result in results:
            boxes = result.boxes.xyxy.cpu()
            clss = result.boxes.cls.cpu().tolist()
            confs = result.boxes.conf.float().cpu().tolist()

            for box, cls, conf in zip(boxes, clss, confs):
                class_name = class_names[int(cls)]

                if class_name == 'license_plate' and conf > 0.5:
                    if conf > max_confidence:
                        max_confidence = conf
                        best_coordinates = box

        return best_coordinates