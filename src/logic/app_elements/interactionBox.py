from abc import abstractmethod

from .base.lock import Lock
from .base.box import Box


class InteractionBox(Box, Lock):
    def __init__(self, *args, access=True, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        Lock.__init__(self, access=access)

    @property
    def clickable_elements(self):
        filtered_iter = filter(self.is_clickable, self.elements)
        return list(filtered_iter)

    def get_real_element_pos(self, element: any) -> tuple[float, float]:
        """
        обойти рекурсивно с помощью реализованного в этом классе breath_first_search
        который будет проходиться по лементам в контейнере
        """
        # if element not in self.elements:
        #     way = self.breath_first_search(self, element)
        #     if way:
        #         select_conteiner = way[element]
        #         pos = element.pos
        #         while element != select_conteiner:
        #             pos = select_conteiner.get_real_element_pos(element)
        #             select_conteiner = way[select_conteiner]
        #
        #         return pos

        return super().get_real_element_pos(element)

    @abstractmethod
    def handle_input(self, key) -> None:
        pass

    @abstractmethod
    def put_elements(self) -> None:
        pass

    @staticmethod
    def is_clickable(element: any) -> bool:
        return hasattr(element, 'is_hover')
