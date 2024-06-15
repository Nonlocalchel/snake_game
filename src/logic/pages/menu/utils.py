from src.logic.app_elements.elements.interactionBox import InteractionBox


def get_available_box(*boxs) -> InteractionBox:
    for box in boxs:
        if box.is_lock:
            continue

        return box
