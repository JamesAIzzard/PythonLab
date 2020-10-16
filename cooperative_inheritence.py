import abc
from typing import Dict, List


class SupportsPersistence(abc.ABC):
    def __init__(self, **kwds):
        super().__init__(**kwds)

    @property
    @abc.abstractmethod
    def persistence_data(self) -> Dict:
        raise NotImplementedError


class SupportsName(abc.ABC):
    def __init__(self, name: str, **kwds):
        self.name: str = name
        super().__init__(**kwds)


class SupportsNameSetting(SupportsName, abc.ABC):
    def __init__(self, **kwds):
        super().__init__(**kwds)

    def set_name(self, name: str):
        self.name = name


class SupportsBulk(SupportsName, abc.ABC):
    def __init__(self, bulk_data: float, **kwds):
        self.bulk: float = bulk_data
        super().__init__(**kwds)


class HasNutrients(SupportsBulk, abc.ABC):
    def __init__(self, nutrients: Dict[str, float], **kwds):
        self.nutrients: Dict[str, float] = nutrients
        super().__init__(**kwds)


class HasFlags(SupportsBulk, abc.ABC):
    def __init__(self, flags: List[str], **kwds):
        self.flags = flags
        super().__init__(**kwds)


class HasQuantity(SupportsBulk, abc.ABC):
    def __init__(self, quantity: float, **kwds):
        self.quantity = quantity
        super().__init__(**kwds)


class HasQuantityTolerance(HasQuantity, abc.ABC):
    def __init__(self, quantity_tolerance: float, **kwds):
        self.quantity = quantity_tolerance
        super().__init__(**kwds)


# Notice how the next two classes don't add any functionality, they just combine the functionality of the classes they
# are inheriting from. They don't strip any arguments from **kwds.
class Ingredient(HasNutrients, HasFlags, SupportsPersistence):
    def __init__(self, **kwds):
        super().__init__(**kwds)

    def persistence_data(self) -> Dict:
        return {"data": 123}


class IngredientAmount(Ingredient, HasQuantityTolerance):
    def __init__(self, **kwds):
        super().__init__(**kwds)

    def persistence_data(self) -> Dict:
        raise NotImplementedError


i = Ingredient(name='Cheese', bulk_data=4.5, nutrients={"protein": 3.2}, flags=['vegan', 'veggie'])
ia = IngredientAmount(name='Bread', bulk_data=4.5, nutrients={"protein": 11.4}, flags=['caffiene-free'], quantity=3.6,
                      quantity_tolerance=10)
breakpoint(i, ia)
