from __future__ import annotations

from typing import List, TYPE_CHECKING

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: List[Item] = []

    def drop(self, item: Item) -> None:
        """
        Removes an item from the inventory and restores it to the game map, at the player's current location.
        """
        self.items.remove(item)
        item.place(self.parent.x, self.parent.y, self.gamemap)

        self.engine.message_log.add_message(f"You dropped the {item.name}.")

    def unique_item(self) -> List[Item]:
        unique_item: List[Item] = []
        for i in self.items:
            is_counted = False
            for j in unique_item:
                if i.name == j.name:
                    if self.parent.equipment.item_is_equipped(i):
                        is_counted = False
                        break
                    else:
                        is_counted = True
                        break
            if not is_counted:
                unique_item.append(i)
        return unique_item

    def item_occurrence(self, item: Item) -> int:
        occ: int = 0
        if self.parent.equipment.item_is_equipped(item):
            return 1
        else:
            for i in self.items:
                if item.name == i.name:
                    occ += 1
        return occ
